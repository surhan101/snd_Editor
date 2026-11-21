import frappe

def add_more_specialized_templates():
    templates = [
        # الرقابة الداخلية
        {
            "template_name": "قائمة تدقيق وفحص الامتثال للوائح المؤسسية",
            "category": "تقرير إداري",
            "is_public": 0,
            "department": "إدارة الرقابة الداخلية والتفتيش",
            "description": "قائمة تحقق متكاملة (Checklist) لفحص مدى التزام الإدارة بالسياسات واللوائح.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 25%; background-color: #faf5ff;"><strong>الإدارة الخاضعة للتدقيق:</strong></td>
        <td style="width: 25%;">..............................</td>
        <td style="width: 25%; background-color: #faf5ff;"><strong>تاريخ التدقيق:</strong></td>
        <td style="width: 25%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #faf5ff;"><strong>رئيس فريق الفحص:</strong></td>
        <td>..............................</td>
        <td style="background-color: #faf5ff;"><strong>نوع التدقيق:</strong></td>
        <td>[ ] دوري مجدول &nbsp; [ ] فجائي طارئ</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #7c3aed; color: #fff; text-align: center;">
        <th style="width: 8%;">م</th>
        <th style="width: 47%;">معيار ومجال الفحص والامتثال</th>
        <th style="width: 15%;">مستوى الامتثال</th>
        <th style="width: 30%;">الملاحظات والشواهد</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td>اكتمال الدورة المستندية والتوقيعات الإدارية المعتمدة</td>
        <td style="text-align: center;">[ ] ممتثل [ ] جزئي [ ] غير ممتثل</td>
        <td>............................................................</td>
    </tr>
    <tr>
        <td style="text-align: center;">2</td>
        <td>سلامة وصحة القيود والمستندات المالية والتعاقدية</td>
        <td style="text-align: center;">[ ] ممتثل [ ] جزئي [ ] غير ممتثل</td>
        <td>............................................................</td>
    </tr>
    <tr>
        <td style="text-align: center;">3</td>
        <td>حماية الأصول وسجلات المخازن والجرد الدوري</td>
        <td style="text-align: center;">[ ] ممتثل [ ] جزئي [ ] غير ممتثل</td>
        <td>............................................................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "تقرير متابعة تنفيذ توصيات اللجان الرقابية",
            "category": "تقرير إداري",
            "is_public": 0,
            "department": "إدارة الرقابة الداخلية والتفتيش",
            "description": "تقرير متابعة دوري لرصد تنفيذ الإدارات لتوصيات تقارير التفتيش والرقابة السابقة.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #faf5ff;"><strong>رقم تقرير المتابعة:</strong></td>
        <td style="width: 30%;">AUD-FOL-....</td>
        <td style="width: 20%; background-color: #faf5ff;"><strong>تاريخ التقرير:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #faf5ff;"><strong>الإدارة محل المتابعة:</strong></td>
        <td colspan="3">................................................................................</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f3e8ff; text-align: center;">
        <th style="width: 8%;">م</th>
        <th style="width: 35%;">التوصية الرقابية الواجبة النفاذ</th>
        <th style="width: 22%;">الإجراء المنفذ حتى تاريخه</th>
        <th style="width: 15%;">نسبة التنفيذ</th>
        <th style="width: 20%;">تقييم فريق الرقابة</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td>............................................................</td>
        <td>............................................................</td>
        <td style="text-align: center; font-weight: bold;">...... %</td>
        <td style="text-align: center; color: green;">مقبول ومطابق</td>
    </tr>
</table>
"""
        },
        # السكرتارية والمراسلات
        {
            "template_name": "كشف حصر المراسلات والتعاميم الصادرة والواردة",
            "category": "تقرير إداري",
            "is_public": 0,
            "department": "إدارة المراسلات والسكرتارية العامة",
            "description": "كشف توثيقي يومي لحركة البريد الوارد والصادر وتوزيعه على الإدارات المعنية.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 25%; background-color: #f8fafc;"><strong>كشف حركة البريد ليوم:</strong></td>
        <td style="width: 25%;">....................</td>
        <td style="width: 25%; background-color: #f8fafc;"><strong>تاريخ القيد:</strong></td>
        <td style="width: 25%;">{{ frappe.utils.today() }}</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #0f4c81; color: #fff; text-align: center;">
        <th style="width: 15%;">رقم القيد الداخلي</th>
        <th style="width: 25%;">الجهة المصدرة / الوارد منها</th>
        <th style="width: 35%;">موضوع المعاملة</th>
        <th style="width: 25%;">الإدارة المحال إليها والتوجيه</th>
    </tr>
    <tr>
        <td style="text-align: center;">IN-.... / 2026</td>
        <td>............................................</td>
        <td>............................................................</td>
        <td>............................................</td>
    </tr>
    <tr>
        <td style="text-align: center;">OUT-.... / 2026</td>
        <td>............................................</td>
        <td>............................................................</td>
        <td>............................................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "سجل توثيق واستعارة الملفات والوثائق من الأرشيف",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة المراسلات والسكرتارية العامة",
            "description": "سند رسمي لطلب واستعارة أصول أو نسخ الملفات من قسم الأرشيف وحفظ الوثائق.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>اسم المستعير:</strong></td>
        <td style="width: 30%;">{{ frappe.session.user_fullname or frappe.session.user }}</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>الإدارة / القسم:</strong></td>
        <td style="width: 30%;">..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>تاريخ الاستعارة:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
        <td style="background-color: #f8fafc;"><strong>تاريخ الإعادة المحدد:</strong></td>
        <td>.... / .... / 2026م</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>رقم وتصنيف الملف:</strong></td>
        <td>ARC-BOX-....</td>
        <td style="background-color: #f8fafc;"><strong>عنوان الملف المطلوب:</strong></td>
        <td>............................................</td>
    </tr>
</table>

<div class="snd-box-gold">
    <strong>إقرار وتعهد:</strong> يتعهد المستعير بالمحافظة التامة على سرية وسلامة وثائق الملف وعدم نزع أي ورقة أو تمزيقها أو تصويرها دون إذن رسمي وإعادتها فور انتهاء الغرض.
</div>
"""
        },
        # المشتريات والمخازن
        {
            "template_name": "محضر جرد دوري وحصر الأصناف الراكدة والتالفة",
            "category": "محضر فحص واستلام",
            "is_public": 0,
            "department": "إدارة المشتريات والمخازن والعقود",
            "description": "محضر جرد مخزني رسمي لحصر العجز أو الزيادة والأصناف بطيئة الحركة.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #fffbeb;"><strong>اسم المخزن:</strong></td>
        <td style="width: 30%;">..............................</td>
        <td style="width: 20%; background-color: #fffbeb;"><strong>تاريخ الجرد:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #fffbeb;"><strong>لجنة الجرد المكلفة:</strong></td>
        <td colspan="3">1. .................... &nbsp;|&nbsp; 2. .................... &nbsp;|&nbsp; 3. ....................</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #fef3c7; text-align: center;">
        <th style="width: 15%;">رمز الصنف</th>
        <th style="width: 30%;">اسم الصنف والوصف</th>
        <th style="width: 15%;">الرصيد الدفتري</th>
        <th style="width: 15%;">الرصيد الفعلي</th>
        <th style="width: 10%;">الفارق</th>
        <th style="width: 15%;">الحالة الفنية</th>
    </tr>
    <tr>
        <td style="text-align: center;">ITM-01</td>
        <td>............................................</td>
        <td style="text-align: center;">......</td>
        <td style="text-align: center;">......</td>
        <td style="text-align: center; color: green;">مطابق</td>
        <td style="text-align: center;">سليم وصالح</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "سند إرجاع مواد وأصناف إلى المخزن",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة المشتريات والمخازن والعقود",
            "description": "توثيق إعادة أصناف فائضة أو صالحة للاستخدام من الإدارات إلى المخزن.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم سند الإرجاع:</strong></td>
        <td style="width: 30%;">RET-WH-....</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>تاريخ الإرجاع:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الإدارة المرجعة:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f8fafc;"><strong>المخزن المستلم:</strong></td>
        <td>المخزن الرئيسي</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>سبب الإرجاع:</strong></td>
        <td colspan="3">[ ] فائض عن الحاجة &nbsp;&nbsp; [ ] انتهاء المشروع &nbsp;&nbsp; [ ] عدم مطابقة فنية</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f1f5f9; text-align: center;">
        <th style="width: 15%;">رمز الصنف</th>
        <th style="width: 45%;">اسم الصنف والبيان</th>
        <th style="width: 20%;">الكمية المرتجعة</th>
        <th style="width: 20%;">الحالة الفنية عند الاستلام</th>
    </tr>
    <tr>
        <td style="text-align: center;">ITM-01</td>
        <td>............................................................</td>
        <td style="text-align: center; font-weight: bold;">......</td>
        <td style="text-align: center; color: green;">ممتازة وجاهزة للصرف</td>
    </tr>
</table>
"""
        },
        # الشؤون القانونية
        {
            "template_name": "كراسة شروط ومواصفات مناقصة محدودة",
            "category": "عقد واتفاقية",
            "is_public": 0,
            "department": "إدارة الشؤون القانونية والمناقصات",
            "description": "الهيكل القانوني للشروط العامة والخاصة والضمانات لمناقصة توريد أو تنفيذ.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم المناقصة:</strong></td>
        <td style="width: 30%;">TND-SPEC-....</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>سنة الطرح:</strong></td>
        <td style="width: 30%;">2026م</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>موضوع المناقصة:</strong></td>
        <td colspan="3"><strong style="color: #0f4c81;">بشأن توريد وتنفيذ ................................................................</strong></td>
    </tr>
</table>

<h4 style="color: #0f4c81; margin: 12px 0 6px 0;">أولاً: الشروط والضوابط العامة:</h4>
<ol style="line-height: 1.8;">
    <li>يُشترط أن يقدم العطاء في مظروفين منفصلين ومغلقين بالشمع الأحمر (مظروف فني + مظروف مالي).</li>
    <li>يُرفق مع العطاء ضمان بنكي ابتدائي غير مشروط بنسبة (2.5%) من قيمة العطاء ساري لمدة (90 يوماً).</li>
    <li>يلتزم الفائز بالمناقصة بتقديم ضمان حسن التنفيذ بنسبة (10%) من إجمالي قيمة العقد عند التوقيع.</li>
</ol>

<h4 style="color: #0f4c81; margin: 12px 0 6px 0;">ثانياً: الغرامات وجزاءات التأخير:</h4>
<div class="snd-box-warning">
    تُطبق غرامة تأخير قدرها (1%) عن كل أسبوع تأخير وبحد أقصى (10%) من إجمالي قيمة العقد، مع حق المؤسسة في فسخ العقد ومصادرة الضمان عند بلوغ الحد الأقصى.
</div>
"""
        },
        {
            "template_name": "مذكرة تسوية ودية لنزاع تعاقدي",
            "category": "عقد واتفاقية",
            "is_public": 0,
            "department": "إدارة الشؤون القانونية والمناقصات",
            "description": "صيغة قانونية لتسوية ودية تنهي الخلافات والنزاعات التعاقدية دون التقاضي.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 25%; background-color: #f8fafc;"><strong>اتفاقية تسوية عقد رقم:</strong></td>
        <td style="width: 25%;">SET-LEG-....</td>
        <td style="width: 25%; background-color: #f8fafc;"><strong>تاريخ التحرير:</strong></td>
        <td style="width: 25%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الطرف الأول:</strong></td>
        <td>المؤسسة / الإدارة العامة</td>
        <td style="background-color: #f8fafc;"><strong>الطرف الثاني:</strong></td>
        <td>شركة / مقاول: ..............................</td>
    </tr>
</table>

<h4 style="color: #1e3a8a; margin: 12px 0 6px 0;">بنود التسوية والتنازل المتبادل:</h4>
<ol style="line-height: 1.8;">
    <li><strong>البند الأول:</strong> يُسقط الطرف الأول غرامات التأخير المتنازع عليها والبالغة (............ ريال) نظراً لثبوت ظروف القوة القاهرة المعتمدة.</li>
    <li><strong>البند الثاني:</strong> يلتزم الطرف الثاني بإنجاز وتسليم باقي الأعمال العالقة خلال مهلة محددة تنتهي في .... / .... / 2026م.</li>
    <li><strong>البند الثالث:</strong> يعتبر هذا الاتفاق تسوية نهائية وشاملة تبرئ ذمة الطرفين ويُسقط أي دعاوى قضائية سابقة بشأنه.</li>
</ol>
"""
        },
        # تقنية المعلومات
        {
            "template_name": "استمارة طلب شراء وتجديد تراخيص برمجية وأنظمة",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة تقنية المعلومات والتحول الرقمي",
            "description": "طلب شراء وتجديد رخص البرمجيات والسحابة ومكافحات الفيروسات والأنظمة.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f0f9ff;"><strong>رقم طلب الترخيص:</strong></td>
        <td style="width: 30%;">LIC-REQ-....</td>
        <td style="width: 20%; background-color: #f0f9ff;"><strong>تاريخ الطلب:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f0f9ff;"><strong>اسم البرنامج / النظام:</strong></td>
        <td colspan="3"><strong style="color: #0284c7;">................................................................................</strong></td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #e0f2fe; text-align: center;">
        <th style="width: 30%;">نوع الترخيص</th>
        <th style="width: 20%;">عدد المستخدمين (Seats)</th>
        <th style="width: 25%;">فترة التجديد المقترحة</th>
        <th style="width: 25%;">التكلفة التقديرية بالدولار</th>
    </tr>
    <tr>
        <td>[ ] سنوي مستمر [ ] ترخيص دائم</td>
        <td style="text-align: center;">...... مستخدم</td>
        <td style="text-align: center;">سنة واحدة (2026-2027م)</td>
        <td style="text-align: center; font-weight: bold;">$ ......</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "محضر إتلاف وشطب أجهزة إلكترونية قديمة أو تالفة",
            "category": "محضر فحص واستلام",
            "is_public": 0,
            "department": "إدارة تقنية المعلومات والتحول الرقمي",
            "description": "محضر لجنة فنية لشطب الأجهزة غير القابلة للإصلاح ومحو البيانات السرية بأمان.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم محضر الشطب:</strong></td>
        <td style="width: 30%;">DIS-IT-....</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>تاريخ المعاينة:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>أعضاء اللجنة الفنية:</strong></td>
        <td colspan="3">1. مهندس نظم &nbsp;|&nbsp; 2. مندوب المخازن &nbsp;|&nbsp; 3. ممثل الرقابة والتفتيش</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f1f5f9; text-align: center;">
        <th style="width: 15%;">نوع الجهاز</th>
        <th style="width: 25%;">الرقم التسلسلي (S/N)</th>
        <th style="width: 35%;">التشخيص الفني وسبب الشطب</th>
        <th style="width: 25%;">محو البيانات (Data Sanitization)</th>
    </tr>
    <tr>
        <td style="text-align: center;">سيرفر قديم / لابتوب</td>
        <td style="text-align: center;">SN-............</td>
        <td>احتراق المعالج واللوحة الأم وتجاوز العمر الافتراضي</td>
        <td style="text-align: center; color: green; font-weight: bold;">تم إتلاف القرص الصلب بأمان ✅</td>
    </tr>
</table>
"""
        }
    ]

    for t in templates:
        name = t["template_name"]
        content = t["template_content"].strip()
        if not frappe.db.exists("Sanad Document Template", name):
            doc = frappe.get_doc({
                "doctype": "Sanad Document Template",
                "template_name": name,
                "category": t["category"],
                "is_public": t["is_public"],
                "department": t["department"],
                "description": t["description"],
                "template_content": content,
                "is_active": 1,
                "usage_count": 0
            })
            doc.insert(ignore_permissions=True)
            print(f"Created: {name}")

    frappe.db.commit()
    print("Additional specialized templates installed successfully!")

if __name__ == "__main__":
    add_more_specialized_templates()

