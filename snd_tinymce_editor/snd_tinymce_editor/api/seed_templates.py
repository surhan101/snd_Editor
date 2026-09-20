import frappe

def seed():
    templates = [
        {
            "template_name": "خطاب رسمي موجه (معتمد)",
            "category": "خطاب رسمي",
            "description": "نموذج خطاب رسمي قياسي مع الترويسة، الديباجة، وجدول بيانات وصندوق الاعتماد",
            "template_content": "<p style='text-align: center; font-size: 16pt; font-weight: bold;'>بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ</p><p><strong>التاريخ:</strong> {{ frappe.utils.today() }}<br><strong>الرقم الإشاري:</strong> {{ doc.name }}</p><p><strong>سعادة / ..................................................................... المحترم</strong><br>السلام عليكم ورحمة الله وبركاته ،،،</p><p><strong>الموضوع:</strong> ..................................................................</p><p style='text-indent: 30px;'>بالإشارة إلى الموضوع أعلاه، نود إحاطة عنايتكم بأنه قد تقرر الآتي:</p><ol><li>البند الأول: ..................................................................</li><li>البند الثاني: ..................................................................</li></ol><p>وتقبلوا منا فائق الاحترام والتقدير ،،،</p><table style='width: 100%; margin-top: 40px;'><tr><td style='width: 50%; text-align: right;'><strong>المسؤول:</strong><br>{{ frappe.session.user_fullname or frappe.session.user }}</td><td style='width: 50%; text-align: left;'><strong>التوقيع:</strong><br>...........................................</td></tr></table>"
        },
        {
            "template_name": "مذكرة داخلية إدارية",
            "category": "مذكرة داخلية",
            "description": "نموذج مذكرة عرض داخلية بين الإدارات والأقسام",
            "template_content": "<div style='border: 2px solid #333; padding: 15px; border-radius: 6px;'><h3 style='text-align: center; margin-top: 0;'>مذكرة داخلية (Internal Memo)</h3><hr><p><strong>إلى:</strong> ...........................................................<br><strong>من:</strong> {{ frappe.session.user_fullname or frappe.session.user }}<br><strong>التاريخ:</strong> {{ frappe.utils.today() }}<br><strong>رقم المعاملة:</strong> {{ doc.name }}</p></div><h4 style='margin-top: 20px;'>الموضوع: ......................................................................</h4><p>يرجى التكرم بالاطلاع واتخاذ اللازم حيال الموضوع الموضح أدناه:</p><p style='background-color: #f9f9f9; padding: 12px; border-right: 4px solid #007bff;'>............................................................................................................................................</p><p>شاكرين ومقدرين حسن تعاونكم الدائم.</p>"
        },
        {
            "template_name": "قرار إداري داخلي",
            "category": "قرار إداري",
            "description": "نموذج قرار إداري رسمي صادر من الإدارة العليا",
            "template_content": "<p style='text-align: center; font-size: 16pt; font-weight: bold;'>بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ</p><h2 style='text-align: center; text-decoration: underline;'>قرار إداري رقم ( &nbsp;&nbsp;&nbsp;&nbsp; ) لسنة 2026م</h2><p><strong>إن المدير العام،،،</strong><br>بناءً على الصلاحيات المخولة له نظاماً،،</p><h3 style='text-align: center; margin: 20px 0;'>// قــرر //</h3><p><strong>مادة (1):</strong> .................................................................</p><p><strong>مادة (2):</strong> .................................................................</p><p><strong>مادة (3):</strong> يُبلّغ هذا القرار لكافة الإدارات المعنية لتنفيذه من تاريخ صدوره.</p><p style='text-align: left; margin-top: 45px;'><strong>المدير العام:</strong> ...................................<br><strong>التاريخ:</strong> {{ frappe.utils.today() }}</p>"
        },
        {
            "template_name": "محضر اجتماع رسمي",
            "category": "تقرير إداري",
            "description": "توثيق رسمي للاجتماعات وجدول الأعمال والقرارات",
            "template_content": "<h2 style='text-align: center;'>محضر اجتماع رسمي</h2><table style='width: 100%; border-collapse: collapse;' border='1'><tr><td style='padding: 8px; width: 25%; background: #f2f2f2;'><strong>عنوان الاجتماع:</strong></td><td style='padding: 8px;'>.........................................</td></tr><tr><td style='padding: 8px; background: #f2f2f2;'><strong>التاريخ والوقت:</strong></td><td style='padding: 8px;'>{{ frappe.utils.today() }}</td></tr><tr><td style='padding: 8px; background: #f2f2f2;'><strong>الحضور:</strong></td><td style='padding: 8px;'>1- .................... &nbsp; 2- .................... &nbsp; 3- ....................</td></tr></table><h3>جدول الأعمال والتوصيات:</h3><ul><li><strong>البند الأول:</strong> ...................................................................</li><li><strong>القرارات المنبثقة:</strong> ...................................................................</li></ul>"
        }
    ]

    for t in templates:
        if not frappe.db.exists("Sanad Document Template", t["template_name"]):
            doc = frappe.get_doc({
                "doctype": "Sanad Document Template",
                "template_name": t["template_name"],
                "category": t["category"],
                "description": t["description"],
                "template_content": t["template_content"],
                "is_active": 1
            })
            doc.insert(ignore_permissions=True)
            print(f"✅ Template created: {t['template_name']}")
        else:
            print(f"⏭️  Template exists: {t['template_name']}")
    frappe.db.commit()
    print("Done.")
