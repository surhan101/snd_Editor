import frappe
from frappe import _

def get_current_user_departments(user=None):
    """جلب قائمة أسماء الإدارات/الدوائر التابع لها المستخدم الحالي"""
    if not user:
        user = frappe.session.user

    if user in ("Administrator", "Guest"):
        return []

    dept_names = set()

    # 1. البحث في جدول أعضاء الإدارة المخصص Sanad Department User
    member_depts = frappe.db.sql("""
        SELECT DISTINCT parent 
        FROM `tabSanad Department User` 
        WHERE user = %s AND parenttype = 'Sanad Department'
    """, (user,), as_dict=True)
    for d in member_depts:
        if d.parent:
            dept_names.add(d.parent)

    # 2. البحث عما إذا كان المستخدم مديراً لأي إدارة
    manager_depts = frappe.db.get_all("Sanad Department", filters={"manager": user, "is_active": 1}, pluck="name")
    for d in manager_depts:
        dept_names.add(d)

    # 3. محاولة الربط التلقائي عبر ملف الموظف في النظام (Employee) إن وجد
    if frappe.db.exists("DocType", "Employee"):
        employee_depts = frappe.db.sql("""
            SELECT e.department, sd.name as sanad_dept
            FROM `tabEmployee` e
            LEFT JOIN `tabSanad Department` sd ON (sd.department_link = e.department OR sd.department_name = e.department)
            WHERE e.user_id = %s AND e.status = 'Active'
        """, (user,), as_dict=True)
        for ed in employee_depts:
            if ed.sanad_dept:
                dept_names.add(ed.sanad_dept)
            elif ed.department and frappe.db.exists("Sanad Department", ed.department):
                dept_names.add(ed.department)

    return list(dept_names)

def is_user_template_manager(user=None):
    """التحقق هل المستخدم أدمن أو يمتلك صلاحية إدارة النماذج"""
    if not user:
        user = frappe.session.user

    if user == "Administrator":
        return True

    roles = frappe.get_roles(user)
    if "System Manager" in roles or "Sanad Template Manager" in roles:
        return True

    return False

@frappe.whitelist()
def get_user_template_permissions():
    """معلومات صلاحيات المستخدم الحالي والإدارات المتاحة له"""
    user = frappe.session.user
    is_admin = is_user_template_manager(user)
    user_depts = get_current_user_departments(user)

    all_departments = frappe.get_all(
        "Sanad Department",
        filters={"is_active": 1},
        fields=["name", "department_name", "code"],
        order_by="department_name asc"
    )

    return {
        "user": user,
        "is_admin_or_manager": is_admin,
        "user_departments": user_depts,
        "all_departments": all_departments
    }

@frappe.whitelist()
def get_templates(target_doctype=None, category=None, department=None, only_public=0):
    """
    جلب النماذج المتاحة والمفعلة مع التصفية الذكية حسب الإدارة والصلاحيات:
    - النماذج العامة تظهر للجميع.
    - نماذج الإدارة تظهر لموظفي تلك الإدارة فقط.
    - الأدمن أو مدير النماذج يمكنه استعراض كل النماذج أو تصفيتها بحسب الإدارة.
    """
    user = frappe.session.user
    is_admin = is_user_template_manager(user)
    user_depts = get_current_user_departments(user)

    filters = {"is_active": 1}
    if category:
        filters["category"] = category

    raw_templates = frappe.get_all(
        "Sanad Document Template",
        filters=filters,
        fields=[
            "name", "template_name", "category", "target_doctype",
            "is_public", "department", "description", "template_content", "usage_count"
        ],
        order_by="is_public desc, usage_count desc, template_name asc"
    )

    # جلب الإدارات المصرح بها من الجدول الفرعي Sanad Template Department لكل النماذج
    template_allowed_depts = {}
    allowed_records = frappe.get_all(
        "Sanad Template Department",
        fields=["parent", "department"]
    )
    for r in allowed_records:
        template_allowed_depts.setdefault(r.parent, []).append(r.department)

    filtered_templates = []
    for t in raw_templates:
        # 1. تصفية المستند الهدف إن وجد
        if target_doctype and t.target_doctype and t.target_doctype != target_doctype:
            continue

        # 2. فحص هل هو عام
        is_pub = bool(t.is_public)

        # 3. الصلاحيات حسب الإدارة
        if is_admin:
            # الأدمن يرى كل شيء، ويمكنه التصفية بحسب إدارة معينة إذا طلب ذلك
            if department:
                allowed_for_t = template_allowed_depts.get(t.name, [])
                if t.department != department and department not in allowed_for_t and not is_pub:
                    continue
            filtered_templates.append(t)
        else:
            # المستخدم العادي:
            # يرى النماذج العامة
            # أو النماذج الخاصة بإدارته
            if is_pub:
                filtered_templates.append(t)
            else:
                allowed_for_t = template_allowed_depts.get(t.name, [])
                # هل الإدارة الأساسية للنموذج تتبع إدارات المستخدم؟
                has_access = (t.department in user_depts) or any(d in user_depts for d in allowed_for_t)
                if has_access:
                    if department and t.department != department and department not in allowed_for_t:
                        continue
                    filtered_templates.append(t)

    # إضافة وسوم مساعدة للواجهة
    for t in filtered_templates:
        t["allowed_depts"] = template_allowed_depts.get(t.name, [])
        t["department_label"] = t.department or (_("عام لجميع الإدارات") if t.is_public else _("غير محدد"))

    return filtered_templates

@frappe.whitelist()
def log_template_usage(template_name, target_doctype=None, target_docname=None):
    """تسجيل حركة استخدام النموذج في السجل التفصيلي Sanad Template Usage Log وزيادة العداد"""
    if not template_name or not frappe.db.exists("Sanad Document Template", template_name):
        return {"success": False, "message": "Template does not exist"}

    tpl = frappe.get_doc("Sanad Document Template", template_name)
    user = frappe.session.user
    user_fullname = frappe.utils.get_fullname(user)

    # جلب إدارة المستخدم إن أمكن
    user_depts = get_current_user_departments(user)
    department = tpl.department or (user_depts[0] if user_depts else None)

    # إنشاء سجل الاستخدام
    try:
        log_doc = frappe.get_doc({
            "doctype": "Sanad Template Usage Log",
            "template": tpl.name,
            "template_name": tpl.template_name,
            "category": tpl.category,
            "is_public": tpl.is_public,
            "department": department,
            "user": user,
            "user_fullname": user_fullname,
            "target_doctype": target_doctype,
            "target_docname": target_docname,
            "usage_timestamp": frappe.utils.now_datetime()
        })
        log_doc.flags.ignore_permissions = True
        log_doc.insert()

        # تحديث عداد مرات الاستخدام في النموذج
        tpl.db_set("usage_count", (tpl.usage_count or 0) + 1, update_modified=False)
        return {"success": True, "log_id": log_doc.name}
    except Exception as e:
        frappe.log_error(f"Error logging template usage: {str(e)}", "Sanad Template Usage Log")
        return {"success": False, "error": str(e)}

@frappe.whitelist()
def get_doctype_fields(target_doctype):
    """جلب قائمة الحقول القابلة للدمج لمستند محدد"""
    if not target_doctype or not frappe.db.exists("DocType", target_doctype):
        return []

    meta = frappe.get_meta(target_doctype)
    excluded_fieldtypes = ["Section Break", "Column Break", "Tab Break", "HTML", "Fold", "Heading"]

    fields = [
        {"label": _("Document ID (رقم القيد/المستند)"), "value": "{{ doc.name }}"},
        {"label": _("Creation Date (تاريخ الإنشاء)"), "value": "{{ doc.creation }}"},
        {"label": _("Owner / User (المستخدم المنشئ)"), "value": "{{ doc.owner }}"},
        {"label": _("Current User Full Name"), "value": "{{ frappe.session.user_fullname or frappe.session.user }}"},
        {"label": _("Today's Date (تاريخ اليوم)"), "value": "{{ frappe.utils.today() }}"}
    ]

    for df in meta.fields:
        if df.fieldtype not in excluded_fieldtypes and df.fieldname:
            label = f"{df.label or df.fieldname} ({{ doc.{df.fieldname} }})"
            fields.append({
                "label": label,
                "value": f"{{{{ doc.{df.fieldname} }}}}"
            })

    return fields

@frappe.whitelist()
def get_quick_snippets(target_doctype=None, category=None):
    """جلب المقتطفات السريعة والمفعلة من دوكتايب Sanad Document Snippet"""
    filters = {"is_active": 1}
    if category:
        filters["category"] = category

    try:
        snippets = frappe.get_all(
            "Sanad Document Snippet",
            filters=filters,
            fields=["name", "snippet_name", "category", "target_doctype", "description", "snippet_content"],
            order_by="category asc, idx asc, creation asc"
        )

        if target_doctype:
            snippets = [s for s in snippets if not s.target_doctype or s.target_doctype == target_doctype]

        if snippets:
            return [
                {
                    "title": s.snippet_name,
                    "category": s.category or "عام",
                    "description": s.description or "",
                    "content": s.snippet_content
                }
                for s in snippets
            ]
    except Exception as e:
        frappe.log_error(f"Error fetching snippets: {str(e)}", "SND TinyMCE Snippets")

    return [
        {
            "title": "البسملة الرسمية (وسط)",
            "category": "مقدمات وافتتاحيات",
            "description": "البسملة بالخط العربي في المنتصف",
            "content": "<p style='text-align: center; font-size: 16pt; font-weight: bold; font-family: Cairo, Arial, sans-serif; margin-bottom: 25px;'>بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ</p>"
        },
        {
            "title": "افتتاحية توجيه خطاب رسمي",
            "category": "مقدمات وافتتاحيات",
            "description": "توجيه الخطاب للجهة مع التحية",
            "content": "<p style='font-size: 13pt; line-height: 1.8;'><strong>سعادة / ................................................................ المحترم</strong><br>السلام عليكم ورحمة الله وبركاته ،،، وبعد:</p>"
        },
        {
            "title": "خاتمة واعتماد رسمي",
            "category": "خواتم واعتمادات",
            "description": "خاتمة مع توقيع وختم",
            "content": "<p style='font-size: 13pt; line-height: 1.8; margin-top: 30px;'>وتقبلوا خالص التحية والتقدير ،،،</p><table style='width: 100%; margin-top: 40px; border: none;'><tr><td style='width: 50%; text-align: right;'><strong>الاسم والصفة:</strong> ..............................</td><td style='width: 50%; text-align: left;'><strong>التوقيع والختم:</strong> ..............................</td></tr></table>"
        }
    ]
