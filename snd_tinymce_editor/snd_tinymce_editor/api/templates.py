import frappe
from frappe import _

@frappe.whitelist()
def get_templates(target_doctype=None, category=None):
    """جلب النماذج المتاحة والمفعلة مع إمكانية التصفية"""
    filters = {"is_active": 1}
    if category:
        filters["category"] = category

    templates = frappe.get_all(
        "Sanad Document Template",
        filters=filters,
        fields=["name", "template_name", "category", "target_doctype", "description", "template_content"]
    )
    
    if target_doctype:
        templates = [t for t in templates if not t.target_doctype or t.target_doctype == target_doctype]
        
    return templates

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

    # قائمة افتراضية احتياطية
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

