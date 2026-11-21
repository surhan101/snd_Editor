import frappe, re

def clean_all_headers_footers():
    templates = frappe.get_all("Sanad Document Template", fields=["name", "template_content"])
    for t in templates:
        content = t.template_content or ""
        # 1. إزالة ترويسات الهيدر العلوية (الجمهورية / الشعار / الترويسات الحكومية)
        content_new = re.sub(r'<div[^>]*text-align:\s*center[^>]*>[\s\S]*?الجمهورية اليمنية[\s\S]*?</div>', '', content, flags=re.IGNORECASE)
        content_new = re.sub(r'<div[^>]*text-align:\s*center[^>]*border-bottom:[^>]*>[\s\S]*?</div>', '', content_new, flags=re.IGNORECASE)
        # 2. إزالة التذييلات السفلية الخارجية (أرقام الهواتف والتواقيع المكررة السفلية)
        content_new = re.sub(r'<div[^>]*margin-top:\s*40px[^>]*text-align:\s*left[^>]*>[\s\S]*?</div>\s*$', '', content_new, flags=re.IGNORECASE)
        content_new = content_new.strip()
        if content_new != content.strip():
            frappe.db.set_value("Sanad Document Template", t.name, "template_content", content_new, update_modified=False)
            print(f"Cleaned headers/footers from: {t.name}")

    frappe.db.commit()
    print("Done cleaning all templates!")

if __name__ == "__main__":
    clean_all_headers_footers()

