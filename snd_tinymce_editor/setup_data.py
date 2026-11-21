import frappe

def create_role():
    if not frappe.db.exists("Role", "Sanad Template Manager"):
        doc = frappe.get_doc({
            "doctype": "Role",
            "role_name": "Sanad Template Manager",
            "desk_access": 1
        })
        doc.insert(ignore_permissions=True)
        print("Created role: Sanad Template Manager")

def create_departments():
    departments = [
        {
            "name": "إدارة الموارد البشرية والشؤون الإدارية",
            "code": "HR-ADM",
            "description": "إدارة شؤون الموظفين، التعيينات، الترقيات، الإجازات، والقرارات الإدارية."
        },
        {
            "name": "إدارة الشؤون المالية والمحاسبة",
            "code": "FIN-ACC",
            "description": "إدارة الحسابات، الميزانيات، أوامر الصرف، العهد، والتسويات المالية."
        },
        {
            "name": "إدارة المشتريات والمخازن والعقود",
            "code": "PROC-WH",
            "description": "إدارة طلبات الشراء، لجان الفحص والاستلام، الجرد المخزني، وأوامر التوريد."
        },
        {
            "name": "إدارة الشؤون القانونية والمناقصات",
            "code": "LEG-TND",
            "description": "صياغة العقود، المذكرات القانونية، المناقصات، والتحقيقات الإدارية."
        },
        {
            "name": "إدارة تقنية المعلومات والتحول الرقمي",
            "code": "IT-DIG",
            "description": "الدعم الفني، إدارة الأجهزة والشبكات، أمن المعلومات، والتحول الرقمي."
        },
        {
            "name": "إدارة الرقابة الداخلية والتفتيش",
            "code": "AUD-COMP",
            "description": "التدقيق المالي والإداري، مراجعة الإجراءات، وضمان الامتثال والنزاهة."
        },
        {
            "name": "إدارة المراسلات والسكرتارية العامة",
            "code": "SEC-GEN",
            "description": "إدارة البريد الوارد والصادر، التعاميم الرسمية، وتوثيق المحاضر والاجتماعات."
        }
    ]

    for d in departments:
        if not frappe.db.exists("Sanad Department", d["name"]):
            doc = frappe.get_doc({
                "doctype": "Sanad Department",
                "department_name": d["name"],
                "code": d["code"],
                "description": d["description"],
                "is_active": 1
            })
            doc.insert(ignore_permissions=True)
            print(f"Created department: {d['name']}")

def create_templates():
    templates = [
        # ─── النماذج العامة (Public) ───
        {
            "template_name": "تعميم إداري عام ورسمي",
            "category": "قرار إداري",
            "is_public": 1,
            "department": None,
            "description": "تعميم رسمي موجه لكافة الإدارات والدوائر والموظفين بتعليمات أو ضوابط جديدة.",
            "template_content": """
<div style="text-align: center; border-bottom: 2px solid #0f4c81; padding-bottom: 15px; margin-bottom: 25px;">
    <h2 style="color: #0f4c81; margin: 0 0 5px 0; font-family: 'Cairo', Arial, sans-serif;">الجمهورية اليمنية</h2>
    <h3 style="margin: 0 0 5px 0;">الجهة الرسمية / الإدارة العامة</h3>
    <h4 style="color: #64748b; margin: 0;">تعميم إداري عام رقم ( ..... / 2026م )</h4>
</div>
<table style="width: 100%; margin-bottom: 20px; border: none;">
    <tr>
        <td style="border: none; width: 60%;"><strong>إلى:</strong> كافة الإدارات والدوائر والأقسام والموظفين</td>
        <td style="border: none; width: 40%; text-align: left;"><strong>التاريخ:</strong> {{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="border: none;" colspan="2"><strong>الموضوع:</strong> بشأن تنظيم وتطبيق إجراءات ........................................</td>
    </tr>
</table>
<p style="line-height: 1.8; text-align: justify;">
بناءً على مقتضيات المصلحة العامة، وحرصاً على انتظام سير العمل ورفع كفاءة الأداء المؤسسي، يُعتمد الالتزام بالتعليمات التالية اعتباراً من تاريخه:
</p>
<ol style="line-height: 1.8;">
    <li>الالتزام التام بالتعليمات والضوابط المنصوص عليها في اللائحة التنفيذية.</li>
    <li>يُحظر تجاوز الإجراءات النظامية المعتمدة دون الرجوع إلى أصحاب الصلاحية.</li>
    <li>تتحمل كل دائرة وإدارة مسؤولية متابعة تنفيذ بنود هذا التعميم وموافاتنا بأي مستجدات.</li>
</ol>
<p style="line-height: 1.8; margin-top: 30px;">
نأمل من الجميع الالتزام والتقيد التام بما ورد أعلاه تجنباً لأي مساءلة نظامية.
</p>
<div style="margin-top: 40px; text-align: left;">
    <p style="margin: 0;"><strong>المدير العام / المسؤول الأول</strong></p>
    <p style="margin: 5px 0 0 0; color: #64748b;">(التوقيع والختم الرسمي)</p>
</div>
"""
        },
        {
            "template_name": "مذكرة تفاهم وإحالة معاملة داخلية",
            "category": "مذكرة داخلية",
            "is_public": 1,
            "department": None,
            "description": "مذكرة رسمية داخلية لإحالة المعاملات والمستندات بين الإدارات للمطالعة أو إبداء الرأي.",
            "template_content": """
<div style="border-bottom: 2px solid #334155; padding-bottom: 10px; margin-bottom: 20px; text-align: center;">
    <h3 style="margin: 0; color: #1e293b;">مذكرة إحالة معاملة داخلية</h3>
</div>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 20px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>من الإدارة:</strong></td>
        <td style="width: 30%;">............................................</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>إلى الإدارة:</strong></td>
        <td style="width: 30%;">............................................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>رقم القيد الداخلي:</strong></td>
        <td>{{ doc.name or '........' }}</td>
        <td style="background-color: #f8fafc;"><strong>تاريخ الإحالة:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الموضوع:</strong></td>
        <td colspan="3">....................................................................................</td>
    </tr>
</table>
<h4 style="color: #0f4c81; margin-bottom: 8px;">الغرض من الإحالة:</h4>
<table style="width: 100%; border: none; margin-bottom: 20px;">
    <tr>
        <td style="border: none;"><input type="checkbox"> للدراسة وإبداء الرأي</td>
        <td style="border: none;"><input type="checkbox"> للاختصاص واستكمال الإجراءات</td>
        <td style="border: none;"><input type="checkbox"> للإحاطة والعلم والمطالعة</td>
        <td style="border: none;"><input type="checkbox"> عاجل وهام جداً</td>
    </tr>
</table>
<p style="line-height: 1.8;"><strong>الشرح والتوجيه الإداري:</strong></p>
<div style="border: 1px dashed #94a3b8; padding: 15px; min-height: 120px; background-color: #fafafa;">
نحيل إليكم المعاملة المرفقة، للتكرم بالتوجيه باتخاذ ما يلزم وفقاً للأنظمة واللوائح المعتمدة.
</div>
<table style="width: 100%; margin-top: 30px; border: none;">
    <tr>
        <td style="border: none; width: 50%;"><strong>اسم الموظف المحيل:</strong> {{ frappe.session.user_fullname or frappe.session.user }}</td>
        <td style="border: none; width: 50%; text-align: left;"><strong>توقيع المستلم وتاريخ الاستلام:</strong> ....................</td>
    </tr>
</table>
"""
        },

        # ─── نماذج إدارة الموارد البشرية والشؤون الإدارية ───
        {
            "template_name": "قرار إداري بترقية وتعيين موظف",
            "category": "قرار إداري",
            "is_public": 0,
            "department": "إدارة الموارد البشرية والشؤون الإدارية",
            "description": "قرار رسمي صادر عن إدارة الموارد البشرية بترقية موظف مع تحديد الدرجة والراتب.",
            "template_content": """
<div style="text-align: center; border-bottom: 2px solid #0f4c81; padding-bottom: 15px; margin-bottom: 25px;">
    <h3 style="color: #0f4c81; margin: 0;">إدارة الموارد البشرية والشؤون الإدارية</h3>
    <h4 style="margin: 5px 0;">قرار إداري رقم ( ..... / 2026م ) بشأن الترقية الوظيفية</h4>
</div>
<p style="line-height: 1.8;">
إن المدير العام / مدير إدارة الموارد البشرية،<br>
- بعد الاطلاع على قانون الخدمة المدنية ولائحة شؤون الموظفين المعتمدة،<br>
- وبناءً على تقرير تقييم الأداء السنوي وموافقة لجنة شؤون الموظفين،<br>
- ولمقتضيات مصلحة العمل،
</p>
<h4 style="text-align: center; color: #0f4c81; margin: 20px 0;">قـــــــــــــرر مـــــا يلـــــــي:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 20px;">
    <tr style="background-color: #f1f5f9;">
        <th style="width: 25%;">اسم الموظف</th>
        <th style="width: 25%;">المسمى السابق</th>
        <th style="width: 25%;">المسمى الجديد</th>
        <th style="width: 25%;">تاريخ سريان القرار</th>
    </tr>
    <tr>
        <td style="text-align: center;">..............................</td>
        <td style="text-align: center;">..............................</td>
        <td style="text-align: center;"><strong>..............................</strong></td>
        <td style="text-align: center;">{{ frappe.utils.today() }}</td>
    </tr>
</table>
<p style="line-height: 1.8;">
<strong>مادة (1):</strong> يُمنح المذكور كافة المزايا والبدلات المالية المقررة للمسمى الوظيفي الجديد.<br>
<strong>مادة (2):</strong> على الإدارات المعنية (الموارد البشرية والشؤون المالية) تنفيذ هذا القرار كلٌ فيما يخصه.<br>
<strong>مادة (3):</strong> يُعمل بهذا القرار من تاريخ صدوره ويُبلغ للمعني.
</p>
<table style="width: 100%; margin-top: 40px; border: none;">
    <tr>
        <td style="border: none; width: 50%;"><strong>مدير الموارد البشرية:</strong> ....................</td>
        <td style="border: none; width: 50%; text-align: left;"><strong>اعتماد المدير العام:</strong> ....................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "نموذج إخلاء طرف وتسليم عهدة وظيفية",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة الموارد البشرية والشؤون الإدارية",
            "description": "براءة ذمة وإخلاء طرف شامل لكافة الإدارات عند استقالة أو انتهاء خدمة الموظف.",
            "template_content": """
<div style="text-align: center; border-bottom: 2px solid #0f4c81; padding-bottom: 10px; margin-bottom: 20px;">
    <h3 style="color: #0f4c81; margin: 0;">نموذج إخلاء طرف ومخالصة عهدة موظف</h3>
</div>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 20px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>اسم الموظف:</strong></td>
        <td style="width: 30%;">..............................</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>الرقم الوظيفي:</strong></td>
        <td style="width: 30%;">..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الإدارة / القسم:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f8fafc;"><strong>تاريخ انتهاء العمل:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
    </tr>
</table>
<h4 style="color: #0f4c81;">إقرارات براءة الذمة من الإدارات المعنية:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 20px;">
    <tr style="background-color: #f1f5f9;">
        <th style="width: 25%;">الإدارة المختصة</th>
        <th style="width: 35%;">موقف العهدة والالتزامات</th>
        <th style="width: 20%;">اسم المسؤول</th>
        <th style="width: 20%;">التوقيع والختم</th>
    </tr>
    <tr>
        <td><strong>الإدارة التابع لها</strong></td>
        <td>تم تسليم كافة الملفات والمهام</td>
        <td>..............................</td>
        <td>..............................</td>
    </tr>
    <tr>
        <td><strong>تقنية المعلومات (IT)</strong></td>
        <td>تم تسليم اللابتوب والبريد والصلاحيات</td>
        <td>..............................</td>
        <td>..............................</td>
    </tr>
    <tr>
        <td><strong>إدارة المخازن والعهد</strong></td>
        <td>لا توجد عهد عينية مسجلة</td>
        <td>..............................</td>
        <td>..............................</td>
    </tr>
    <tr>
        <td><strong>الشؤون المالية</strong></td>
        <td>تمت تسوية كافة العهد والسلف المالية</td>
        <td>..............................</td>
        <td>..............................</td>
    </tr>
</table>
<p style="line-height: 1.8; font-weight: bold; text-align: center; margin-top: 25px;">
بناءً على التوقيعات أعلاه، تُعتبر ذمة الموظف بريئة تماماً من أي التزامات تجاه المؤسسة.
</p>
"""
        },

        # ─── نماذج إدارة الشؤون المالية والمحاسبة ───
        {
            "template_name": "طلب أمر صرف مالي ومستحقات",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة الشؤون المالية والمحاسبة",
            "description": "طلب رسمي لصرف مستحقات أو دفعات تعاقدية مع بيان البند والاعتماد المالي.",
            "template_content": """
<div style="text-align: center; border-bottom: 2px solid #047857; padding-bottom: 12px; margin-bottom: 20px;">
    <h3 style="color: #047857; margin: 0;">إدارة الشؤون المالية والمحاسبة</h3>
    <h4 style="margin: 5px 0;">طلب أمر صرف مالي رقم ( ..... / 2026م )</h4>
</div>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 20px;">
    <tr>
        <td style="width: 20%; background-color: #ecfdf5;"><strong>يُصرف لأمر المستفيد:</strong></td>
        <td colspan="3"><strong>....................................................................................</strong></td>
    </tr>
    <tr>
        <td style="background-color: #ecfdf5;"><strong>المبلغ بالأرقام:</strong></td>
        <td style="width: 30%; color: #047857; font-weight: bold; font-size: 14pt;">........................ ريال</td>
        <td style="background-color: #ecfdf5; width: 20%;"><strong>طريقة الدفع:</strong></td>
        <td style="width: 30%;">شيك ( ) / تحويل بنكي ( ) / نقداً ( )</td>
    </tr>
    <tr>
        <td style="background-color: #ecfdf5;"><strong>المبلغ كتابةً:</strong></td>
        <td colspan="3">فقط .................................................................................... لا غير.</td>
    </tr>
    <tr>
        <td style="background-color: #ecfdf5;"><strong>وذلك مقابل:</strong></td>
        <td colspan="3">................................................................................................................</td>
    </tr>
    <tr>
        <td style="background-color: #ecfdf5;"><strong>الخصم على البند:</strong></td>
        <td>..............................</td>
        <td style="background-color: #ecfdf5;"><strong>مركز التكلفة:</strong></td>
        <td>..............................</td>
    </tr>
</table>
<table style="width: 100%; margin-top: 35px; border: none;">
    <tr>
        <td style="border: none; text-align: center; width: 25%;"><strong>إعداد المحاسب:</strong><br><br>....................</td>
        <td style="border: none; text-align: center; width: 25%;"><strong>المراجعة والتدقيق:</strong><br><br>....................</td>
        <td style="border: none; text-align: center; width: 25%;"><strong>مدير الشؤون المالية:</strong><br><br>....................</td>
        <td style="border: none; text-align: center; width: 25%;"><strong>اعتماد الصرف (المدير العام):</strong><br><br>....................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "مذكرة تسوية عهدة مالية مؤقتة",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة الشؤون المالية والمحاسبة",
            "description": "كشف تفصيلي بتسوية العهد المالية المؤقتة وإرفاق فواتير المصروفات.",
            "template_content": """
<div style="text-align: center; border-bottom: 2px solid #047857; padding-bottom: 12px; margin-bottom: 20px;">
    <h3 style="color: #047857; margin: 0;">كشف تسوية عهدة مالية مؤقتة</h3>
</div>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 20px;">
    <tr>
        <td style="width: 25%; background-color: #f8fafc;"><strong>اسم صاحب العهدة:</strong></td>
        <td style="width: 25%;">..............................</td>
        <td style="width: 25%; background-color: #f8fafc;"><strong>مبلغ العهدة الأصلي:</strong></td>
        <td style="width: 25%;">.................... ريال</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>رقم سند صرف العهدة:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f8fafc;"><strong>تاريخ الاستلام:</strong></td>
        <td>..............................</td>
    </tr>
</table>
<h4 style="color: #047857;">بيان الفواتير والمصروفات الفعلية:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 20px;">
    <tr style="background-color: #f1f5f9;">
        <th style="width: 10%;">م</th>
        <th style="width: 20%;">رقم الفاتورة</th>
        <th style="width: 45%;">البيان وتفاصيل المصروف</th>
        <th style="width: 25%;">المبلغ (ريال)</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td style="text-align: center;">......</td>
        <td>............................................................</td>
        <td style="text-align: center;">......</td>
    </tr>
    <tr>
        <td style="text-align: center;">2</td>
        <td style="text-align: center;">......</td>
        <td>............................................................</td>
        <td style="text-align: center;">......</td>
    </tr>
    <tr style="background-color: #f8fafc; font-weight: bold;">
        <td colspan="3" style="text-align: right;">إجمالي المصروف الفعلي المؤيد بالمستندات:</td>
        <td style="text-align: center;">....................</td>
    </tr>
    <tr style="background-color: #ecfdf5; font-weight: bold;">
        <td colspan="3" style="text-align: right;">المبلغ المتبقي المورد للخزينة / المستحق للموظف:</td>
        <td style="text-align: center; color: #047857;">....................</td>
    </tr>
</table>
"""
        },

        # ─── نماذج إدارة المشتريات والمخازن والعقود ───
        {
            "template_name": "محضر فحص واستلام مشتريات وتجهيزات",
            "category": "محضر فحص واستلام",
            "is_public": 0,
            "department": "إدارة المشتريات والمخازن والعقود",
            "description": "محضر لجنة فحص وتدقيق مطابقة الأصناف الموردة ومقارنتها بالمواصفات الفنية.",
            "template_content": """
<div style="text-align: center; border-bottom: 2px solid #b45309; padding-bottom: 12px; margin-bottom: 20px;">
    <h3 style="color: #b45309; margin: 0;">إدارة المشتريات والمخازن - لجنة الفحص والاستلام</h3>
    <h4 style="margin: 5px 0;">محضر فحص واستلام فني رقم ( ..... / 2026م )</h4>
</div>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 15px;">
    <tr>
        <td style="width: 20%; background-color: #fffbeb;"><strong>اسم المورد:</strong></td>
        <td style="width: 30%;">..............................</td>
        <td style="width: 20%; background-color: #fffbeb;"><strong>رقم أمر الشراء/العقد:</strong></td>
        <td style="width: 30%;">{{ doc.name or '........' }}</td>
    </tr>
    <tr>
        <td style="background-color: #fffbeb;"><strong>رقم الفاتورة:</strong></td>
        <td>..............................</td>
        <td style="background-color: #fffbeb;"><strong>تاريخ الفحص:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
    </tr>
</table>
<p style="line-height: 1.8;">
اجتمعت لجنة الفحص والاستلام المشكلة بموجب القرار الإداري رقم (....)، وقامت بإجراء الفحص والمعاينة للأصناف الموردة، وكانت النتائج كالتالي:
</p>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 20px;">
    <tr style="background-color: #fef3c7;">
        <th style="width: 8%;">م</th>
        <th style="width: 32%;">اسم الصنف والمواصفات</th>
        <th style="width: 15%;">الكمية الموردة</th>
        <th style="width: 15%;">الكمية المقبولة</th>
        <th style="width: 15%;">الكمية المرفوضة</th>
        <th style="width: 15%;">القرار الفني</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td>أجهزة كمبيوتر مكتبي Core i7</td>
        <td style="text-align: center;">50</td>
        <td style="text-align: center;">50</td>
        <td style="text-align: center;">0</td>
        <td style="text-align: center; color: green; font-weight: bold;">مطابق ومقبول</td>
    </tr>
    <tr>
        <td style="text-align: center;">2</td>
        <td>طابعات ليزر شبكية ملونة</td>
        <td style="text-align: center;">5</td>
        <td style="text-align: center;">5</td>
        <td style="text-align: center;">0</td>
        <td style="text-align: center; color: green; font-weight: bold;">مطابق ومقبول</td>
    </tr>
</table>
<p style="line-height: 1.8;"><strong>توصيات وقرار اللجنة:</strong><br>
تقر اللجنة بقبول الأصناف المطابقة وإدخالها المخازن رسمياً، مع إشعار إدارة الحسابات باستكمال صرف مستحقات المورد.
</p>
<table style="width: 100%; margin-top: 35px; border: none;">
    <tr>
        <td style="border: none; text-align: center; width: 33%;"><strong>العضو الفني:</strong><br><br>....................</td>
        <td style="border: none; text-align: center; width: 33%;"><strong>أمين المخزن:</strong><br><br>....................</td>
        <td style="border: none; text-align: center; width: 33%;"><strong>رئيس لجنة الفحص:</strong><br><br>....................</td>
    </tr>
</table>
"""
        },

        # ─── نماذج إدارة الشؤون القانونية والمناقصات ───
        {
            "template_name": "مذكرة رأي ودراسة قانونية",
            "category": "مذكرة داخلية",
            "is_public": 0,
            "department": "إدارة الشؤون القانونية والمناقصات",
            "description": "مذكرة رسمية متكاملة لتقديم الاستشارة والرأي القانوني في النزاعات والعقود.",
            "template_content": """
<div style="text-align: center; border-bottom: 2px solid #1e3a8a; padding-bottom: 12px; margin-bottom: 25px;">
    <h3 style="color: #1e3a8a; margin: 0;">إدارة الشؤون القانونية والمناقصات</h3>
    <h4 style="margin: 5px 0;">مذكرة رأي قانوني رقم ( ..... / 2026م )</h4>
</div>
<table style="width: 100%; border: none; margin-bottom: 20px;">
    <tr>
        <td style="border: none; width: 60%;"><strong>إلى سعادة:</strong> المدير العام المحترم</td>
        <td style="border: none; width: 40%; text-align: left;"><strong>التاريخ:</strong> {{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="border: none;" colspan="2"><strong>الموضوع:</strong> الرأي القانوني بشأن موضوع ........................................</td>
    </tr>
</table>
<h4 style="color: #1e3a8a; margin-bottom: 6px;">أولاً: الوقائع والخلفية:</h4>
<p style="line-height: 1.8; text-align: justify;">
بالإشارة إلى إحالتكم الكريمة للموضوع المقيد برقم (.....) وتاريخ (.....)، وبمطالعة أوراق المعاملة والعقد المبرم يتبين أن:
..........................................................................................................................................................
</p>
<h4 style="color: #1e3a8a; margin-bottom: 6px;">ثانياً: التأصيل والتحليل القانوني:</h4>
<p style="line-height: 1.8; text-align: justify;">
حيث إن المادة (....) من القانون رقم (....) تنص على أنه: "........................................................"، وحيث إن الثابت بالأوراق أن الطرف الآخر قد أخل بالتزاماته التعاقدية المحددة في البند (....).
</p>
<h4 style="color: #1e3a8a; margin-bottom: 6px;">ثالثاً: الرأي القانوني والخلاصة:</h4>
<div style="border-right: 4px solid #1e3a8a; background-color: #f8fafc; padding: 12px; line-height: 1.8;">
نرى قانوناً: توجيه إنذار عدلي للمورد بمنحه مهلة أقصاها (7) أيام لتصحيح المخالفة، وفي حال عدم الالتزام يتم مصادرة الضمان البنكي وتطبيق غرامات التأخير التعاقدية.
</div>
<div style="margin-top: 40px; text-align: left;">
    <p style="margin: 0;"><strong>مدير الإدارة القانونية</strong></p>
    <p style="margin: 5px 0 0 0; color: #64748b;">المستشار القانوني: ....................</p>
</div>
"""
        },

        # ─── نماذج إدارة تقنية المعلومات والتحول الرقمي ───
        {
            "template_name": "محضر تسليم عهدة أجهزة إلكترونية (IT)",
            "category": "محضر فحص واستلام",
            "is_public": 0,
            "department": "إدارة تقنية المعلومات والتحول الرقمي",
            "description": "نموذج توثيق تسليم أجهزة كمبيوتر ولابتوبات للموظفين وتحديد السيريال والشروط.",
            "template_content": """
<div style="text-align: center; border-bottom: 2px solid #0284c7; padding-bottom: 12px; margin-bottom: 20px;">
    <h3 style="color: #0284c7; margin: 0;">إدارة تقنية المعلومات والتحول الرقمي</h3>
    <h4 style="margin: 5px 0;">محضر تسليم عهدة أجهزة تقنية رقم ( ..... / 2026م )</h4>
</div>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 15px;">
    <tr>
        <td style="width: 20%; background-color: #f0f9ff;"><strong>اسم المستلم:</strong></td>
        <td style="width: 30%;">..............................</td>
        <td style="width: 20%; background-color: #f0f9ff;"><strong>الإدارة / القسم:</strong></td>
        <td style="width: 30%;">..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f0f9ff;"><strong>الرقم الوظيفي:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f0f9ff;"><strong>تاريخ التسليم:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
    </tr>
</table>
<h4 style="color: #0284c7;">بيانات ومواصفات الأجهزة المسلمة:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 20px;">
    <tr style="background-color: #e0f2fe;">
        <th style="width: 25%;">نوع الجهاز</th>
        <th style="width: 25%;">الموديل والمصنع</th>
        <th style="width: 25%;">الرقم التسلسلي (S/N)</th>
        <th style="width: 25%;">الحالة الفنية</th>
    </tr>
    <tr>
        <td style="text-align: center;">كمبيوتر محمول (Laptop)</td>
        <td style="text-align: center;">Dell Latitude / HP Elite</td>
        <td style="text-align: center;">..............................</td>
        <td style="text-align: center; color: green;">جديد - ممتاز</td>
    </tr>
    <tr>
        <td style="text-align: center;">شاحن وحقيبة أصلية</td>
        <td style="text-align: center;">المصنع الأصلي</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center; color: green;">جديد - كامل</td>
    </tr>
</table>
<p style="line-height: 1.8; font-size: 10pt; color: #475569;">
<strong>إقرار المستلم:</strong> أقر أنا الموقع أدناه بأنني استلمت الأجهزة الموضحة أعلاه بحالة سليمة وجاهزة للعمل، وأتعهد بالمحافظة عليها واستخدامها لأغراض العمل الرسمي فقط وإعادتها فور طلب الإدارة أو انتهاء الخدمة.
</p>
<table style="width: 100%; margin-top: 35px; border: none;">
    <tr>
        <td style="border: none; width: 50%;"><strong>مهندس قسم الدعم الفني:</strong> ....................</td>
        <td style="border: none; width: 50%; text-align: left;"><strong>توقيع الموظف المستلم:</strong> ....................</td>
    </tr>
</table>
"""
        },

        # ─── نماذج إدارة الرقابة الداخلية والتفتيش ───
        {
            "template_name": "تقرير تدقيق ومراجعة رقابية داخلية",
            "category": "تقرير إداري",
            "is_public": 0,
            "department": "إدارة الرقابة الداخلية والتفتيش",
            "description": "تقرير تدقيق فني وإداري يوضح الملاحظات الرقابية، أسبابها، والتوصيات التصحيحية.",
            "template_content": """
<div style="text-align: center; border-bottom: 2px solid #7c3aed; padding-bottom: 12px; margin-bottom: 20px;">
    <h3 style="color: #7c3aed; margin: 0;">إدارة الرقابة الداخلية والتفتيش</h3>
    <h4 style="margin: 5px 0;">تقرير تدقيق ومراجعة رقابية دورية</h4>
</div>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 15px;">
    <tr>
        <td style="width: 25%; background-color: #faf5ff;"><strong>الإدارة محل التدقيق:</strong></td>
        <td style="width: 25%;">..............................</td>
        <td style="width: 25%; background-color: #faf5ff;"><strong>الفترة محل الفحص:</strong></td>
        <td style="width: 25%;">من .... إلى ....</td>
    </tr>
</table>
<h4 style="color: #7c3aed;">جدول حصر الملاحظات الرقابية والإجراءات التصحيحية:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 20px;">
    <tr style="background-color: #f3e8ff;">
        <th style="width: 8%;">م</th>
        <th style="width: 32%;">الملاحظة الرقابية المرصودة</th>
        <th style="width: 15%;">مستوى المخاطر</th>
        <th style="width: 45%;">التوصية والإجراء التصحيحي المطلوب</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td>عدم استكمال توقيعات محاضر الفحص قبل الصرف</td>
        <td style="text-align: center; color: red; font-weight: bold;">مرتفع</td>
        <td>إلزام الإدارة المالية بعدم اعتماد أي أمر صرف دون محضر فحص مكتمل الأركان.</td>
    </tr>
    <tr>
        <td style="text-align: center;">2</td>
        <td>تأخر ترحيل القيود المحاسبية الدورية</td>
        <td style="text-align: center; color: orange; font-weight: bold;">متوسط</td>
        <td>جدولة دورية أسبوعية للترحيل والمراجعة تفادياً لتراكم القيود.</td>
    </tr>
</table>
<table style="width: 100%; margin-top: 35px; border: none;">
    <tr>
        <td style="border: none; width: 50%;"><strong>فريق المراجعة والتفتيش:</strong> ....................</td>
        <td style="border: none; width: 50%; text-align: left;"><strong>مدير إدارة الرقابة الداخلية:</strong> ....................</td>
    </tr>
</table>
"""
        }
    ]

    for t in templates:
        if not frappe.db.exists("Sanad Document Template", t["template_name"]):
            doc = frappe.get_doc({
                "doctype": "Sanad Document Template",
                "template_name": t["template_name"],
                "category": t["category"],
                "is_public": t["is_public"],
                "department": t["department"],
                "description": t["description"],
                "template_content": t["template_content"].strip(),
                "is_active": 1,
                "usage_count": 0
            })
            doc.insert(ignore_permissions=True)
            print(f"Created template: {t['template_name']}")
        else:
            doc = frappe.get_doc("Sanad Document Template", t["template_name"])
            doc.is_public = t["is_public"]
            doc.department = t["department"]
            doc.save(ignore_permissions=True)

def setup_all():
    create_role()
    create_departments()
    create_templates()
    frappe.db.commit()
    print("Setup completed successfully!")

