import frappe

def after_migrate():
    """تهيئة البيانات الافتراضية والتصنيفات والإعدادات بعد التثبيت أو الترحيل"""
    setup_settings()
    setup_categories()
    setup_default_snippets()

def setup_settings():
    if not frappe.db.exists("DocType", "SND Editor Settings"):
        return
    try:
        doc = frappe.get_single("SND Editor Settings")
        if not doc.apply_on_all_default_editors:
            doc.apply_on_all_default_editors = 1
            doc.save(ignore_permissions=True)
            frappe.db.commit()
    except Exception:
        pass

def setup_categories():
    if not frappe.db.exists("DocType", "Sanad Snippet Category"):
        return

    categories = [
        ("مقدمات وافتتاحيات", "صيغ وافتتاحيات الخطابات والمراسلات والعقود الرسمية"),
        ("خواتم واعتمادات", "خواتم الخطابات ونماذج التوقيع والاعتماد والأختام"),
        ("شروط وأحكام التعاقد", "البنود القانونية وشروط التعاقد والالتزامات العامة"),
        ("بنود التوريد والدفع", "شروط التوريد ومواعيد التسليم وآليات السداد والدفع"),
        ("الضمان والصيانة", "بنود فترات الضمان وخدمات ما بعد البيع والصيانة"),
        ("جداول ونماذج بيانات", "هياكل جداول فارغة ومنسقة لحصر المواد والمواصفات والدفعات"),
        ("أخرى", "مقتطفات وبنود متنوعة أخرى")
    ]

    for name, desc in categories:
        if not frappe.db.exists("Sanad Snippet Category", name):
            doc = frappe.get_doc({
                "doctype": "Sanad Snippet Category",
                "category_name": name,
                "description": desc
            })
            doc.insert(ignore_permissions=True)
    frappe.db.commit()

def setup_default_snippets():
    if not frappe.db.exists("DocType", "Sanad Document Snippet"):
        return

    snippets = [
        {
            "snippet_name": "البسملة الرسمية (وسط)",
            "category": "مقدمات وافتتاحيات",
            "description": "البسملة بالخط العربي بخط عريض في منتصف الصفحة",
            "snippet_content": '<p style="text-align: center; font-size: 16pt; font-weight: bold; font-family: Cairo, Arial, sans-serif; margin-bottom: 25px;">بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ</p>'
        },
        {
            "snippet_name": "افتتاحية توجيه خطاب رسمي",
            "category": "مقدمات وافتتاحيات",
            "description": "توجيه الخطاب للجهة أو الشخص مع التحية الرسمية",
            "snippet_content": '<p style="font-size: 13pt; line-height: 1.8;"><strong>سعادة / ................................................................ المحترم</strong><br><strong>السلام عليكم ورحمة الله وبركاته ،،، وبعد:</strong></p>'
        },
        {
            "snippet_name": "ديباجة عقد اتفاق وشراكة",
            "category": "مقدمات وافتتاحيات",
            "description": "ديباجة افتتاحية لعقد اتفاق بين طرفين",
            "snippet_content": '<p style="text-align: justify; line-height: 1.8;">بعون الله وتوفيقه تم في يوم ........... الموافق .../.../202... م، الاتفاق والتراضي بين كل من:<br><strong>الطرف الأول:</strong> .................................... وسجله التجاري / هويته: (....................)<br><strong>الطرف الثاني:</strong> .................................... وسجله التجاري / هويته: (....................)<br>وقد اتفق الطرفان وهما بكامل الأهلية المعتبرة شرعاً ونظاماً على ما يلي:</p>'
        },
        {
            "snippet_name": "خاتمة وتوقيع واعتماد رسمي",
            "category": "خواتم واعتمادات",
            "description": "عبارة شكر وتوقيع وختم معتمد للطرفين",
            "snippet_content": '<p style="font-size: 13pt; line-height: 1.8; margin-top: 30px;">وتقبلوا خالص التحية والتقدير والامتنان ،،،</p><table style="width: 100%; margin-top: 35px; border: none; font-size: 12pt;"><tr><td style="width: 50%; text-align: right; border: none;"><strong>الاسم والصفة:</strong> ....................<br><strong>التوقيع:</strong> ....................</td><td style="width: 50%; text-align: left; border: none;"><strong>الختم الرسمي:</strong> ....................</td></tr></table>'
        },
        {
            "snippet_name": "جدول توقيعات الأطراف والشهود",
            "category": "خواتم واعتمادات",
            "description": "توقيع الطرف الأول والثاني مع الشهود",
            "snippet_content": '<table style="width: 100%; margin-top: 35px; border-collapse: collapse;"><thead><tr style="background-color: #f1f5f9;"><th style="width: 50%; text-align: center;">الطرف الأول</th><th style="width: 50%; text-align: center;">الطرف الثاني</th></tr></thead><tbody><tr><td style="height: 80px; vertical-align: top; padding: 10px;">الاسم:<br>التوقيع:<br>الختم:</td><td style="height: 80px; vertical-align: top; padding: 10px;">الاسم:<br>التوقيع:<br>الختم:</td></tr></tbody></table>'
        },
        {
            "snippet_name": "بند السرية وعدم الإفصاح",
            "category": "شروط وأحكام التعاقد",
            "description": "التزام الطرفين بسرية البيانات والمعلومات",
            "snippet_content": '<p style="text-align: justify; line-height: 1.8;"><strong>بند السرية:</strong> يلتزم الطرفان بالمحافظة التامة على سرية كافة البيانات والمعلومات الفنية والتجارية المتبادلة بينهما بموجب هذا الاتفاق، ولا يحق لأي طرف الإفصاح عنها لأي طرف ثالث دون موافقة خطية مسبقة من الطرف الآخر، ويسري هذا الالتزام أثناء سريان العقد وبعد انتهائه.</p>'
        },
        {
            "snippet_name": "بند فض النزاعات والاختصاص القضائي",
            "category": "شروط وأحكام التعاقد",
            "description": "آلية حل النزاعات والقضاء المختص",
            "snippet_content": '<p style="text-align: justify; line-height: 1.8;"><strong>فض النزاعات:</strong> في حال نشوء أي خلاف أو نزاع حول تفسير أو تنفيذ بنود هذا العقد، يسعى الطرفان لحله ودياً خلال ثلاثين (30) يوماً، وفي حال تعذر ذلك يكون الاختصاص القضائي منعقداً للمحاكم المختصة نظاماً في المملكة العربية السعودية.</p>'
        },
        {
            "snippet_name": "جدول دفعات السداد المالية",
            "category": "بنود التوريد والدفع",
            "description": "جدول مقسم لدفعات السداد المالي حسب الإنجاز",
            "snippet_content": '<table style="width: 100%; border-collapse: collapse;"><thead><tr style="background-color: #f1f5f9;"><th style="width: 15%; text-align: center;">الدفعة</th><th style="width: 20%; text-align: center;">النسبة</th><th style="width: 25%; text-align: center;">المبلغ</th><th style="width: 40%; text-align: center;">شرط الاستحقاق / الإنجاز</th></tr></thead><tbody><tr><td style="text-align: center;">الأولى</td><td style="text-align: center;">25%</td><td>..................</td><td>عند توقيع العقد كدفعة مقدمة</td></tr><tr><td style="text-align: center;">الثانية</td><td style="text-align: center;">50%</td><td>..................</td><td>عند إنجاز 60% من الأعمال / التوريد</td></tr><tr><td style="text-align: center;">الأخيرة</td><td style="text-align: center;">25%</td><td>..................</td><td>عند التسليم النهائي والاعتماد الرسمي</td></tr></tbody></table>'
        },
        {
            "snippet_name": "الضمان وخدمات ما بعد البيع",
            "category": "الضمان والصيانة",
            "description": "مدة الضمان وتغطية العيوب المصنعية واستبدال القطع",
            "snippet_content": '<div style="border-right: 3px solid #d69e2e; padding-right: 12px; margin: 15px 0; font-size: 12pt; line-height: 1.8;"><strong>الضمان وخدمات ما بعد البيع:</strong><p>تضمن المنشأة خلو المواد والمنتجات الموردة من أي عيوب مصنعية لمدة (12) شهراً تبدأ من تاريخ التسليم النهائي. يشمل الضمان استبدال أو إصلاح الأجزاء المعيبة مجاناً دون تحميل العميل أي تكاليف إضافية، باستثناء الأعطال الناتجة عن سوء الاستخدام.</p></div>'
        },
        {
            "snippet_name": "جدول حصر الكميات والمواصفات والأسعار",
            "category": "جداول ونماذج بيانات",
            "description": "جدول رسمي لحصر المواد والكميات والأسعار الإجمالية",
            "snippet_content": '<table style="width: 100%; border-collapse: collapse;"><thead><tr style="background-color: #f1f5f9;"><th style="width: 8%; text-align: center;">م</th><th style="width: 42%;">الوصف والمواصفات</th><th style="width: 12%; text-align: center;">الكمية</th><th style="width: 12%; text-align: center;">الوحدة</th><th style="width: 13%; text-align: center;">سعر الوحدة</th><th style="width: 13%; text-align: center;">الإجمالي</th></tr></thead><tbody><tr><td style="text-align: center;">1</td><td></td><td style="text-align: center;"></td><td style="text-align: center;"></td><td style="text-align: center;"></td><td style="text-align: center;"></td></tr><tr><td style="text-align: center;">2</td><td></td><td style="text-align: center;"></td><td style="text-align: center;"></td><td style="text-align: center;"></td><td style="text-align: center;"></td></tr><tr><td style="text-align: center;">3</td><td></td><td style="text-align: center;"></td><td style="text-align: center;"></td><td style="text-align: center;"></td><td style="text-align: center;"></td></tr><tr style="background-color: #f8fafc; font-weight: bold;"><td colspan="5" style="text-align: left; padding-left: 15px;">المجموع الكلي:</td><td style="text-align: center;">0.00</td></tr></tbody></table>'
        }
    ]

    for s in snippets:
        if not frappe.db.exists("Sanad Document Snippet", s["snippet_name"]):
            doc = frappe.get_doc({
                "doctype": "Sanad Document Snippet",
                "snippet_name": s["snippet_name"],
                "category": s["category"],
                "description": s["description"],
                "snippet_content": s["snippet_content"],
                "is_active": 1
            })
            doc.insert(ignore_permissions=True)

    frappe.db.commit()
