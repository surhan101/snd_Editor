frappe.query_reports["Sanad Template Usage Summary"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": __("من تاريخ"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1)
        },
        {
            "fieldname": "to_date",
            "label": __("إلى تاريخ"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today()
        },
        {
            "fieldname": "department",
            "label": __("الإدارة / الدائرة"),
            "fieldtype": "Link",
            "options": "Sanad Department"
        },
        {
            "fieldname": "template",
            "label": __("النموذج"),
            "fieldtype": "Link",
            "options": "Sanad Document Template"
        },
        {
            "fieldname": "category",
            "label": __("التصنيف"),
            "fieldtype": "Select",
            "options": "\nخطاب رسمي\nمذكرة داخلية\nقرار إداري\nعقد واتفاقية\nتقرير إداري\nإشعار رسمي\nمحضر فحص واستلام\nطلب إداري/مالي\nأخرى"
        },
        {
            "fieldname": "user",
            "label": __("المستخدم"),
            "fieldtype": "Link",
            "options": "User"
        }
    ]
};

