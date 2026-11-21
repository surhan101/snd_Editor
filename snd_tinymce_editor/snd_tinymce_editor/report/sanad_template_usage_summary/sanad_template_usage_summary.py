import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data, chart, report_summary = get_data(filters)
    return columns, data, None, chart, report_summary

def get_columns():
    return [
        {
            "label": _("اسم النموذج"),
            "fieldname": "template_name",
            "fieldtype": "Link",
            "options": "Sanad Document Template",
            "width": 240
        },
        {
            "label": _("التصنيف"),
            "fieldname": "category",
            "fieldtype": "Data",
            "width": 140
        },
        {
            "label": _("الإدارة / الدائرة"),
            "fieldname": "department",
            "fieldtype": "Link",
            "options": "Sanad Department",
            "width": 200
        },
        {
            "label": _("نطاق النموذج"),
            "fieldname": "scope",
            "fieldtype": "Data",
            "width": 110
        },
        {
            "label": _("مرات الاستخدام"),
            "fieldname": "total_usage",
            "fieldtype": "Int",
            "width": 130
        },
        {
            "label": _("المستخدمون الفريدون"),
            "fieldname": "unique_users",
            "fieldtype": "Int",
            "width": 140
        },
        {
            "label": _("آخر مستخدم"),
            "fieldname": "last_user",
            "fieldtype": "Data",
            "width": 160
        },
        {
            "label": _("آخر تاريخ استخدام"),
            "fieldname": "last_used",
            "fieldtype": "Datetime",
            "width": 160
        },
        {
            "label": _("أكثر مستند مرتبط"),
            "fieldname": "top_doctype",
            "fieldtype": "Data",
            "width": 150
        }
    ]

def get_data(filters):
    conditions = []
    values = {}

    if filters.get("from_date"):
        conditions.append("DATE(l.usage_timestamp) >= %(from_date)s")
        values["from_date"] = filters.get("from_date")

    if filters.get("to_date"):
        conditions.append("DATE(l.usage_timestamp) <= %(to_date)s")
        values["to_date"] = filters.get("to_date")

    if filters.get("department"):
        conditions.append("l.department = %(department)s")
        values["department"] = filters.get("department")

    if filters.get("template"):
        conditions.append("l.template = %(template)s")
        values["template"] = filters.get("template")

    if filters.get("category"):
        conditions.append("l.category = %(category)s")
        values["category"] = filters.get("category")

    if filters.get("user"):
        conditions.append("l.user = %(user)s")
        values["user"] = filters.get("user")

    where_clause = (" WHERE " + " AND ".join(conditions)) if conditions else ""

    query = f"""
        SELECT 
            l.template as template_name,
            l.category,
            COALESCE(l.department, 'عام لجميع الإدارات') as department,
            CASE WHEN l.is_public = 1 THEN 'عام (الجميع)' ELSE 'خاص بالإدارة' END as scope,
            COUNT(l.name) as total_usage,
            COUNT(DISTINCT l.user) as unique_users,
            MAX(l.user_fullname) as last_user,
            MAX(l.usage_timestamp) as last_used,
            COALESCE(MAX(l.target_doctype), 'غير محدد') as top_doctype
        FROM `tabSanad Template Usage Log` l
        {where_clause}
        GROUP BY l.template, l.category, l.department, l.is_public
        ORDER BY total_usage DESC, last_used DESC
    """

    data = frappe.db.sql(query, values, as_dict=True)

    # حساب الإحصائيات العامة ومخطط الرسم البياني
    total_usages = sum(d.get("total_usage", 0) for d in data)
    dept_usage = {}
    top_template = data[0].get("template_name") if data else _("لا يوجد بعد")

    for d in data:
        dept = d.get("department") or _("عام")
        dept_usage[dept] = dept_usage.get(dept, 0) + d.get("total_usage", 0)

    # إعداد المخطط البياني (Chart)
    chart_labels = list(dept_usage.keys())[:7]
    chart_values = [dept_usage[k] for k in chart_labels]

    chart = {
        "data": {
            "labels": chart_labels,
            "datasets": [
                {
                    "name": _("مرات الاستخدام"),
                    "values": chart_values
                }
            ]
        },
        "type": "bar",
        "colors": ["#0f4c81", "#2563eb", "#10b981", "#f59e0b", "#8b5cf6"]
    } if chart_labels else None

    # بطاقات الملخص الإحصائي (KPI Summary Cards)
    top_dept = max(dept_usage, key=dept_usage.get) if dept_usage else _("لا يوجد")
    report_summary = [
        {
            "value": total_usages,
            "label": _("إجمالي استخدامات النماذج"),
            "datatype": "Int",
            "indicator": "Blue"
        },
        {
            "value": len(data),
            "label": _("عدد النماذج المفعلة المستخدمة"),
            "datatype": "Int",
            "indicator": "Green"
        },
        {
            "value": top_dept,
            "label": _("أكثر الإدارات استخداماً"),
            "datatype": "Data",
            "indicator": "Purple"
        },
        {
            "value": top_template,
            "label": _("النموذج الأكثر طلباً"),
            "datatype": "Data",
            "indicator": "Orange"
        }
    ]

    return data, chart, report_summary

