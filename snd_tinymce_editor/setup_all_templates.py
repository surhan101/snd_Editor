import frappe

def setup_clean_templates():
    templates = [
        # ═════════════════════════════════════════════════════════════════════
        # 1. النماذج العامة (🌐 متاحة لجميع الإدارات والدوائر)
        # ═════════════════════════════════════════════════════════════════════
        {
            "template_name": "مذكرة عرض داخلية للمطالعة وإبداء الرأي",
            "category": "مذكرة داخلية",
            "is_public": 1,
            "department": None,
            "description": "مذكرة عرض داخلية مختصرة ومباشرة لعرض الموضوع والتوصيات للمطالعة دون ترويسة أو تذييلة.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 18%; background-color: #f8fafc;"><strong>من الإدارة:</strong></td>
        <td style="width: 32%;">............................................</td>
        <td style="width: 18%; background-color: #f8fafc;"><strong>إلى الإدارة:</strong></td>
        <td style="width: 32%;">............................................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>رقم القيد / المرجع:</strong></td>
        <td>{{ doc.name or '....................' }}</td>
        <td style="background-color: #f8fafc;"><strong>التاريخ:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الموضوع:</strong></td>
        <td colspan="3"><strong style="color: #0f4c81;">بشأن ....................................................................................</strong></td>
    </tr>
</table>

<p style="line-height: 1.8; margin-top: 15px;">
<strong>السلام عليكم ورحمة الله وبركاته ،،، وبعد:</strong>
</p>
<p style="line-height: 1.8; text-align: justify;">
نعرض على سعادتكم الموضوع الموضح أعلاه، حيث تفيد الوقائع والمعطيات بما يلي:
</p>
<ul style="line-height: 1.8;">
    <li>........................................................................................................................</li>
    <li>........................................................................................................................</li>
</ul>

<div class="snd-box-info">
    <strong>💡 الرأي والتوصية الإدارية:</strong><br>
    بناءً على ما سبق، نوصي بالموافقة على اتخاذ الإجراءات التالية: ................................................................
</div>

<p style="line-height: 1.8; margin-top: 20px;">
وتفضلوا بقبول فائق الاحترام والتقدير ،،،
</p>

<table style="width: 100%; margin-top: 25px; border: 1px solid #e2e8f0;">
    <tr style="background-color: #f1f5f9;">
        <th style="width: 50%; text-align: center;">إعداد المذكرة</th>
        <th style="width: 50%; text-align: center;">توجيه / قرار صاحب الصلاحية</th>
    </tr>
    <tr>
        <td style="padding: 12px; vertical-align: top;">
            <strong>الاسم والصفة:</strong> {{ frappe.session.user_fullname or frappe.session.user }}<br>
            <strong>التوقيع:</strong> ....................<br>
            <strong>التاريخ:</strong> {{ frappe.utils.today() }}
        </td>
        <td style="padding: 12px; vertical-align: top;">
            <strong>التوجيه:</strong> [ ] يُعتمد [ ] يُحال إلى ............. [ ] يُعاد للدراسة<br>
            <strong>الملاحظات:</strong> ........................................................<br>
            <strong>التوقيع:</strong> ....................
        </td>
    </tr>
</table>
"""
        },
        {
            "template_name": "طلب موافقة واعتماد إجراء إداري",
            "category": "طلب إداري/مالي",
            "is_public": 1,
            "department": None,
            "description": "طلب رسمي داخلي للموافقة المسبقة واعتماد الصلاحيات والقرارات.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>الجهة الطالبة:</strong></td>
        <td style="width: 30%;">..............................</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>تاريخ الطلب:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>نوع الإجراء المطلوب:</strong></td>
        <td colspan="3">[ ] مالي [ ] إداري [ ] فني وتقني [ ] تعاقدي استثنائي</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>موضوع الطلب:</strong></td>
        <td colspan="3"><strong style="color: #0f4c81;">الموافقة على ........................................................................</strong></td>
    </tr>
</table>

<h4 style="color: #0f4c81; margin: 15px 0 8px 0;">مبررات وأسباب الطلب:</h4>
<div style="border: 1px dashed #cbd5e1; padding: 12px; background-color: #fdfdfd; line-height: 1.8;">
1. ............................................................................................................................<br>
2. ............................................................................................................................
</div>

<h4 style="color: #0f4c81; margin: 15px 0 8px 0;">الأثر والنتائج المتوقعة:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f1f5f9;">
        <th style="width: 33%;">الأثر التشغيلي</th>
        <th style="width: 33%;">الأثر المالي المترتب</th>
        <th style="width: 34%;">المدة الزمنية المطلوبة للتنفيذ</th>
    </tr>
    <tr>
        <td>..............................</td>
        <td style="text-align: center;">.................... ريال</td>
        <td style="text-align: center;">...... أيام عمل</td>
    </tr>
</table>

<div class="snd-box-gold" style="margin-top: 15px;">
    <strong>📌 قرار جهة الاختصاص:</strong><br>
    [ ] موافقة تامة والبدء بالإجراء فوراً &nbsp;&nbsp;&nbsp;&nbsp; [ ] موافقة مشروطة بـ ........................ &nbsp;&nbsp;&nbsp;&nbsp; [ ] اعتذار لعدم توفر الاعتماد
</div>
"""
        },
        {
            "template_name": "محضر اجتماع وتوصيات دوري",
            "category": "تقرير إداري",
            "is_public": 1,
            "department": None,
            "description": "توثيق رسمي لوقائع الاجتماعات الدورية والقرارات وجدول متابعة المهام.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>عنوان الاجتماع:</strong></td>
        <td style="width: 30%;"><strong>............................................</strong></td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم المحضر:</strong></td>
        <td style="width: 30%;">{{ doc.name or '...... / 2026م' }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>تاريخ وتوقيت الانعقاد:</strong></td>
        <td>{{ frappe.utils.today() }} - الساعة .....</td>
        <td style="background-color: #f8fafc;"><strong>مكان الاجتماع:</strong></td>
        <td>قاعة الاجتماعات الرئيسية / افتراضياً</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>رئيس الاجتماع:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f8fafc;"><strong>مقرر الاجتماع:</strong></td>
        <td>{{ frappe.session.user_fullname or frappe.session.user }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الحاضرون:</strong></td>
        <td colspan="3">1. .................... &nbsp;|&nbsp; 2. .................... &nbsp;|&nbsp; 3. .................... &nbsp;|&nbsp; 4. ....................</td>
    </tr>
</table>

<h4 style="color: #0f4c81; margin: 15px 0 8px 0;">أولاً: جدول أعمال الاجتماع:</h4>
<ol style="line-height: 1.8;">
    <li>استعراض القرارات ومتابعة تنفيذ مخرجات الاجتماع السابق.</li>
    <li>مناقشة موضوع ........................................................................</li>
    <li>ما يُستجد من أعمال وطروحات.</li>
</ol>

<h4 style="color: #0f4c81; margin: 15px 0 8px 0;">ثانياً: جدول القرارات والمهام والتكليفات:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #0f4c81; color: #fff;">
        <th style="width: 8%;">م</th>
        <th style="width: 42%;">القرار / التكليف المتفق عليه</th>
        <th style="width: 25%;">المسؤول عن التنفيذ</th>
        <th style="width: 25%;">المهلة وتاريخ الإنجاز</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td>........................................................................</td>
        <td>..............................</td>
        <td style="text-align: center;">.... / .... / 2026م</td>
    </tr>
    <tr>
        <td style="text-align: center;">2</td>
        <td>........................................................................</td>
        <td>..............................</td>
        <td style="text-align: center;">.... / .... / 2026م</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "تقرير إنجاز ومتابعة مهام دوري",
            "category": "تقرير إداري",
            "is_public": 1,
            "department": None,
            "description": "تقرير مهني بحصر الأعمال المنجزة والمهام قيد التنفيذ ونسب الإنجاز.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>اسم الموظف / الإدارة:</strong></td>
        <td style="width: 30%;">{{ frappe.session.user_fullname or frappe.session.user }}</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>فترة التقرير:</strong></td>
        <td style="width: 30%;">[ ] أسبوعي [ ] شهري [ ] ربع سنوي</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>تاريخ إعداد التقرير:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
        <td style="background-color: #f8fafc;"><strong>المسمى الوظيفي:</strong></td>
        <td>..............................</td>
    </tr>
</table>

<h4 style="color: #0f4c81; margin: 15px 0 8px 0;">1. المهام والأعمال المكتملة بنجاح:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f0fdf4;">
        <th style="width: 10%;">م</th>
        <th style="width: 50%;">البيان وتفاصيل المهمة</th>
        <th style="width: 20%;">تاريخ الإنجاز</th>
        <th style="width: 20%;">المخرجات المتحققة</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td>............................................................</td>
        <td style="text-align: center;">{{ frappe.utils.today() }}</td>
        <td style="text-align: center; color: green;">مكتمل بنسبة 100%</td>
    </tr>
</table>

<h4 style="color: #0f4c81; margin: 15px 0 8px 0;">2. المهام قيد التنفيذ والمستمرة:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #fefce8;">
        <th style="width: 10%;">م</th>
        <th style="width: 45%;">المهمة والهدف منها</th>
        <th style="width: 20%;">نسبة الإنجاز الحالية</th>
        <th style="width: 25%;">التاريخ المتوقع للاكتمال</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td>............................................................</td>
        <td style="text-align: center; font-weight: bold;">...... %</td>
        <td style="text-align: center;">.... / .... / 2026م</td>
    </tr>
</table>

<h4 style="color: #0f4c81; margin: 15px 0 8px 0;">3. المعوقات والصعوبات ومقترحات الحل:</h4>
<div class="snd-box-warning">
    <strong>المعوقات:</strong> ........................................................................................................<br>
    <strong>المقترحات لدعم الإنجاز:</strong> ....................................................................................
</div>
"""
        },
        {
            "template_name": "إشعار وتبليغ رسمي داخلي",
            "category": "إشعار رسمي",
            "is_public": 1,
            "department": None,
            "description": "إشعار وتبليغ رسمي موجه لموظف أو قسم بإجراء محدد دون ترويسة.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم الإشعار:</strong></td>
        <td style="width: 30%;">{{ doc.name or '...... / 2026' }}</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>تاريخ الإشعار:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>إلى الأخ / الزميل:</strong></td>
        <td colspan="3"><strong>................................................................................</strong></td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>المسمى والإدارة:</strong></td>
        <td colspan="3">................................................................................</td>
    </tr>
</table>

<p style="line-height: 1.8;">
<strong>السلام عليكم ورحمة الله وبركاته ،،، وبعد:</strong>
</p>
<div class="snd-box-danger">
    <strong style="font-size: 13pt;">الموضوع: إشعار رسمي بخصوص ................................................................</strong>
</div>

<p style="line-height: 1.8; text-align: justify;">
نحيطكم علماً بأنه تقرر الآتي: .........................................................................................................................................
..........................................................................................................................................................................
</p>
<p style="line-height: 1.8;">
وعليه؛ يرجى الإحاطة والالتزام بموجبه والعمل بما تضمنه فوراً دون تأخير.
</p>

<table style="width: 100%; margin-top: 30px; border: none;">
    <tr>
        <td style="border: none; width: 50%;"><strong>المسؤول / الإدارة المصدرة للإشعار:</strong> ....................</td>
        <td style="border: none; width: 50%; text-align: left;"><strong>إقرار الاستلام والتوقيع:</strong> ....................</td>
    </tr>
</table>
"""
        },

        # ═════════════════════════════════════════════════════════════════════
        # 2. إدارة الموارد البشرية والشؤون الإدارية (🏢 HR-ADM)
        # ═════════════════════════════════════════════════════════════════════
        {
            "template_name": "طلب إجازة رسمية (اعتيادية / مرضية / اضطرارية)",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة الموارد البشرية والشؤون الإدارية",
            "description": "طلب إجازة متكامل يوضح الرصيد المستحق، اسم البديل، وتوصيات الاعتماد.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>اسم الموظف:</strong></td>
        <td style="width: 30%;">{{ frappe.session.user_fullname or frappe.session.user }}</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>الرقم الوظيفي:</strong></td>
        <td style="width: 30%;">..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الإدارة / القسم:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f8fafc;"><strong>المسمى الوظيفي:</strong></td>
        <td>..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>نوع الإجازة المطلوبة:</strong></td>
        <td colspan="3">[ ] اعتيادية سنوية &nbsp;&nbsp; [ ] مرضية (مرفق تقرير طبي) &nbsp;&nbsp; [ ] اضطرارية &nbsp;&nbsp; [ ] بدون راتب</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>مدة الإجازة:</strong></td>
        <td>(......) أيام عمل</td>
        <td style="background-color: #f8fafc;"><strong>الفترة:</strong></td>
        <td>من: .... / .... / 2026م &nbsp; إلى: .... / .... / 2026م</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الموظف البديل المكلف:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f8fafc;"><strong>توقيع الموظف البديل:</strong></td>
        <td>..............................</td>
    </tr>
</table>

<h4 style="color: #0f4c81; margin: 12px 0 6px 0;">بيان إدارة الموارد البشرية (مراجعة الأرصدة):</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #f1f5f9; text-align: center;">
        <th>رصيد الإجازات المستحق</th>
        <th>الإجازة المطلوبة الحالية</th>
        <th>الرصيد المتبقي بعد الإجازة</th>
        <th>رأي مسؤول شؤون الموظفين</th>
    </tr>
    <tr style="text-align: center;">
        <td>...... يوم</td>
        <td>...... يوم</td>
        <td>...... يوم</td>
        <td style="color: green; font-weight: bold;">مستوفٍ للشروط وموافق عليه</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f8fafc;">
        <td style="width: 50%; padding: 10px;"><strong>موافقة الرئيس المباشر:</strong><br>[ ] موافق &nbsp; [ ] غير موافق<br>التوقيع: ....................</td>
        <td style="width: 50%; padding: 10px;"><strong>اعتماد مدير الموارد البشرية:</strong><br>[ ] معتمد ومقيد في السجلات<br>التوقيع: ....................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "أمر تكليف بمهمة عمل رسمية وانتداب",
            "category": "قرار إداري",
            "is_public": 0,
            "department": "إدارة الموارد البشرية والشؤون الإدارية",
            "description": "أمر تكليف رسمي وانتداب داخلي أو خارجي مع بيان بدل الانتداب وتغطية النفقات.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم أمر التكليف:</strong></td>
        <td style="width: 30%;">{{ doc.name or '...... / 2026م' }}</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>تاريخ الصدور:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الموظف المكلف:</strong></td>
        <td><strong>............................................</strong></td>
        <td style="background-color: #f8fafc;"><strong>الرقم الوظيفي:</strong></td>
        <td>..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الإدارة / الدائرة:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f8fafc;"><strong>المسمى الوظيفي:</strong></td>
        <td>..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>جهة وموقع المهمة:</strong></td>
        <td colspan="3"><strong>................................................................................</strong></td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>المدة المقررة للتكليف:</strong></td>
        <td>(......) يوماً</td>
        <td style="background-color: #f8fafc;"><strong>الفترة:</strong></td>
        <td>ابتداءً من: .... / .... / 2026م</td>
    </tr>
</table>

<h4 style="color: #0f4c81; margin: 12px 0 6px 0;">أهداف ومحاور المهمة المكلف بها:</h4>
<div style="border: 1px dashed #94a3b8; padding: 12px; background-color: #fafafa; line-height: 1.8;">
1. ............................................................................................................................<br>
2. ............................................................................................................................
</div>

<h4 style="color: #0f4c81; margin: 12px 0 6px 0;">المخصصات والبدلات المالية المقررة:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #f1f5f9; text-align: center;">
        <th>بدل الانتداب اليومي</th>
        <th>وسيلة النقل / تذاكر السفر</th>
        <th>مصاريف الإقامة والانتقال</th>
        <th>الخصم على بند</th>
    </tr>
    <tr style="text-align: center;">
        <td>...... ريال / يوم</td>
        <td>سيارة المؤسسة / تذكرة سفر</td>
        <td>مغطاة بموجب الفواتير</td>
        <td>موازنة المهمات الرسمية</td>
    </tr>
</table>

<div class="snd-box-info">
    يلتزم الموظف المكلف برفع تقرير إنجاز فني تفصيلي لمدير الإدارة خلال (48 ساعة) من تاريخ انتهاء المهمة.
</div>
"""
        },
        {
            "template_name": "إشعار استفسار ومساءلة إدارية عن غياب أو تقصير",
            "category": "مذكرة داخلية",
            "is_public": 0,
            "department": "إدارة الموارد البشرية والشؤون الإدارية",
            "description": "خطاب استفسار ومساءلة نظامية لطلب إيضاح الموظف بشأن مخالفة أو غياب.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>إلى الأخ الزميل:</strong></td>
        <td style="width: 30%;">............................................</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>الرقم الوظيفي:</strong></td>
        <td style="width: 30%;">..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الوظيفة والإدارة:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f8fafc;"><strong>تاريخ المساءلة:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
    </tr>
</table>

<div class="snd-box-warning">
    <strong>الموضوع: استفسار ومساءلة إدارية بشأن (الغياب / التقصير في أداء الواجب الوظيفي)</strong>
</div>

<p style="line-height: 1.8; text-align: justify;">
بالرجوع إلى سجلات الحضور والانصراف والتقارير الرقابية المرفوعة إلينا، تبيّن تسجيل المخالفة التالية بحقكم:<br>
<span style="color: #b91c1c;">(.......................................................................................................................................................)</span>
</p>
<p style="line-height: 1.8;">
لذا؛ نأمل منكم إبداء أسباب ومبررات ما ذُكر كتابةً وتدوين ردكم أدناه، خلال مدة أقصاها (24 ساعة) من تاريخ استلامكم هذا الإشعار، تمهيداً لاتخاذ القرار النظامي المناسب.
</p>

<h4 style="color: #0f4c81; margin: 15px 0 6px 0;">رد وإيضاح الموظف المحال للمساءلة:</h4>
<div style="border: 1px dashed #94a3b8; padding: 15px; min-height: 100px; background-color: #fafafa; line-height: 1.8;">
أفيد سعادتكم بأن سبب ما ورد أعلاه يعود إلى: ..........................................................................................................................................<br>
..........................................................................................................................................<br>
<strong>توقيع الموظف:</strong> .................... &nbsp;&nbsp;&nbsp;&nbsp; <strong>التاريخ:</strong> .... / .... / 2026م
</div>
"""
        },
        {
            "template_name": "إقرار مباشرة عمل واستئناف دوام بعد إجازة",
            "category": "إشعار رسمي",
            "is_public": 0,
            "department": "إدارة الموارد البشرية والشؤون الإدارية",
            "description": "توثيق تاريخ ووقت استئناف الموظف لمهامه الوظيفية بعد انقضاء الإجازة أو الانتداب.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>اسم الموظف:</strong></td>
        <td style="width: 30%;">{{ frappe.session.user_fullname or frappe.session.user }}</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>الرقم الوظيفي:</strong></td>
        <td style="width: 30%;">..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الإدارة / القسم:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f8fafc;"><strong>المسمى الوظيفي:</strong></td>
        <td>..............................</td>
    </tr>
</table>

<h4 style="color: #0f4c81; margin: 12px 0 6px 0;">بيانات الانقطاع والإجازة السابقة:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 25%; background-color: #f8fafc;"><strong>نوع الانقطاع:</strong></td>
        <td style="width: 25%;">[ ] إجازة اعتيادية [ ] إجازة مرضية [ ] مهمة رسمية</td>
        <td style="width: 25%; background-color: #f8fafc;"><strong>رقم القرار/الطلب:</strong></td>
        <td style="width: 25%;">....................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>تاريخ انتهاء الإجازة:</strong></td>
        <td>.... / .... / 2026م</td>
        <td style="background-color: #f8fafc;"><strong>تاريخ المباشرة الفعلية:</strong></td>
        <td><strong style="color: green;">{{ frappe.utils.today() }}</strong></td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>موقف الانضباط:</strong></td>
        <td colspan="3">[ ] مباشرة في الموعد المحدد &nbsp;&nbsp;&nbsp;&nbsp; [ ] تأخر عن الموعد بمقدار (......) يوم بعذر / دون عذر</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1; margin-top: 15px;">
    <tr style="background-color: #f8fafc;">
        <td style="width: 50%; padding: 10px;"><strong>إقرار وتوقيع الموظف:</strong><br><br>أقر بأنني باشرت عملي الفعلي بتاريخ اليوم.<br>التوقيع: ....................</td>
        <td style="width: 50%; padding: 10px;"><strong>تأييد الرئيس المباشر:</strong><br><br>أؤكد مباشرة المذكور لعمله واستلامه لمهامه.<br>التوقيع: ....................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "طلب سلفة مالية على الراتب الشهري",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة الموارد البشرية والشؤون الإدارية",
            "description": "طلب سلفة على الراتب وتحديد جدول الأقساط الشهرية المستقطعة.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>اسم الموظف:</strong></td>
        <td style="width: 30%;">{{ frappe.session.user_fullname or frappe.session.user }}</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>الرقم الوظيفي:</strong></td>
        <td style="width: 30%;">..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الراتب الأساسي:</strong></td>
        <td>.................... ريال</td>
        <td style="background-color: #f8fafc;"><strong>صافي الراتب الشهري:</strong></td>
        <td>.................... ريال</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>مبلغ السلفة المطلوب:</strong></td>
        <td><strong style="color: #0f4c81; font-size: 13pt;">.................... ريال</strong></td>
        <td style="background-color: #f8fafc;"><strong>طريقة السداد:</strong></td>
        <td>على (......) أقساط شهرية متتالية</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>قيمة القسط الشهري:</strong></td>
        <td>.................... ريال شهرياً</td>
        <td style="background-color: #f8fafc;"><strong>بداية الخصم:</strong></td>
        <td>راتب شهر: .................... 2026م</td>
    </tr>
</table>

<div class="snd-box-gray">
    <strong>أسباب ومبررات طلب السلفة:</strong><br>
    ..........................................................................................................................................................................
</div>

<h4 style="color: #0f4c81; margin: 15px 0 6px 0;">موقف السلف والالتزامات السابقة (قسم الرواتب):</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #f1f5f9; text-align: center;">
        <th>هل توجد سلفة سابقة قائمة؟</th>
        <th>المتبقي من السلفة السابقة</th>
        <th>نسبة الاستقطاع الكلية من الراتب</th>
        <th>قرار قسم الاستحقاقات</th>
    </tr>
    <tr style="text-align: center;">
        <td>[ ] لا توجد &nbsp; [ ] نعم</td>
        <td>...... ريال</td>
        <td>...... % (الحد الأقصى 25%)</td>
        <td style="color: green; font-weight: bold;">مسموح نظاماً</td>
    </tr>
</table>
"""
        },

        # ═════════════════════════════════════════════════════════════════════
        # 3. إدارة الشؤون المالية والمحاسبة (🏢 FIN-ACC)
        # ═════════════════════════════════════════════════════════════════════
        {
            "template_name": "طلب نقل مخصصات واعتمادات بين بنود الميزانية",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة الشؤون المالية والمحاسبة",
            "description": "طلب مناقلة اعتمادات مالية وتعديل مخصصات البنود وفق اللائحة المالية.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #ecfdf5;"><strong>رقم المناقلة:</strong></td>
        <td style="width: 30%;">{{ doc.name or 'TR-BUD-....' }}</td>
        <td style="width: 20%; background-color: #ecfdf5;"><strong>التاريخ:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #ecfdf5;"><strong>السنة المالية:</strong></td>
        <td>2026م</td>
        <td style="background-color: #ecfdf5;"><strong>مركز التكلفة المعني:</strong></td>
        <td>..............................</td>
    </tr>
</table>

<h4 style="color: #047857; margin: 15px 0 8px 0;">جدول المناقلة المالية بين البنود:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #d1fae5; text-align: center;">
        <th style="width: 30%;">البند المنقول منه (تخفيض)</th>
        <th style="width: 20%;">المبلغ المنقول (ريال)</th>
        <th style="width: 30%;">البند المنقول إليه (تعزيز)</th>
        <th style="width: 20%;">الرصيد المتبقي بالبند الأول</th>
    </tr>
    <tr>
        <td>بند: ..............................</td>
        <td style="text-align: center; font-weight: bold; color: #dc2626;">- ....................</td>
        <td>بند: ..............................</td>
        <td style="text-align: center;">.................... ريال</td>
    </tr>
</table>

<div class="snd-box-info">
    <strong>مبررات المناقلة المالية:</strong><br>
    نظراً للحاجة الملحة لتغطية التزامات بند .................................................... واستنفاد مخصصاته، مع توفر وفر مالي في بند .................................................... دون الإخلال بالمشاريع المعتمدة.
</div>

<table style="width: 100%; margin-top: 25px; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f8fafc; text-align: center;">
        <th style="width: 33%;">مدير إدارة الميزانية والتخطيط</th>
        <th style="width: 33%;">المراجع المالي الداخلي</th>
        <th style="width: 34%;">اعتماد مدير الشؤون المالية</th>
    </tr>
    <tr style="text-align: center; height: 60px;">
        <td>....................</td>
        <td>....................</td>
        <td>....................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "محضر مطابقة حسابات وتسوية بنكية شهرية",
            "category": "تقرير إداري",
            "is_public": 0,
            "department": "إدارة الشؤون المالية والمحاسبة",
            "description": "محضر تسوية الفروقات بين الرصيد الدفتري وكشف الحساب البنكي.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>اسم البنك والحساب:</strong></td>
        <td style="width: 30%;">..............................</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم الحساب البنكي (IBAN):</strong></td>
        <td style="width: 30%;">............................................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>فترة التسوية الشهرية:</strong></td>
        <td>عن شهر: .................... 2026م</td>
        <td style="background-color: #f8fafc;"><strong>تاريخ إعداد التسوية:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #047857; color: #fff;">
        <th style="width: 70%;">البيـــــــــــــــــــــــــــــــــان</th>
        <th style="width: 30%; text-align: center;">المبلغ (ريال)</th>
    </tr>
    <tr>
        <td><strong>الرصيد بموجب كشف الحساب البنكي المرفق في نهاية الشهر:</strong></td>
        <td style="text-align: center; font-weight: bold;">....................</td>
    </tr>
    <tr style="background-color: #f8fafc;">
        <td colspan="2"><strong>يُضاف إليه (إيداعات بالطريق لم تقيد في كشف البنك):</strong></td>
    </tr>
    <tr>
        <td style="padding-right: 25px;">- إيداع نقدي بتاريخ .... / .... / 2026م (سند رقم .....)</td>
        <td style="text-align: center;">....................</td>
    </tr>
    <tr style="background-color: #f8fafc;">
        <td colspan="2"><strong>يُخصم منه (شيكات صادرة للمستفيدين لم تقدم للصرف):</strong></td>
    </tr>
    <tr>
        <td style="padding-right: 25px;">- شيك رقم (......) لأمر: ..............................</td>
        <td style="text-align: center; color: red;">( .................... )</td>
    </tr>
    <tr style="background-color: #ecfdf5; font-size: 13pt; font-weight: bold;">
        <td>الرصيد الدفتري المعدل المطابق لحساب الأستاذ العام:</td>
        <td style="text-align: center; color: #047857;">....................</td>
    </tr>
</table>

<div class="snd-box-success">
    <strong>نتيجة التدقيق:</strong> تم التحقق من القيود ولا توجد فروقات معلقة غير مبررة.
</div>
"""
        },
        {
            "template_name": "استمارة مطالبة مالية وصرف مستخلص أعمال منجزة",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة الشؤون المالية والمحاسبة",
            "description": "استمارة صرف مستخلص دوري أو نهائي لمقاول أو مورد مقابل أعمال منجزة.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>اسم المقاول / المورد:</strong></td>
        <td style="width: 30%;"><strong>............................................</strong></td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم المستخلص:</strong></td>
        <td style="width: 30%;">مستخلص رقم ( ... ) [ ] جاري [ ] ختامي</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>اسم المشروع / العقد:</strong></td>
        <td>............................................</td>
        <td style="background-color: #f8fafc;"><strong>رقم العقد وتاريخه:</strong></td>
        <td>عقد رقم: ............ بتاريخ: .... / ....</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #f1f5f9; text-align: center;">
        <th>قيمة الأعمال المنجزة تراكمياً</th>
        <th>يُخصم: مستخلصات منصرفة سابقاً</th>
        <th>يُخصم: نسبة ضمان حسن التنفيذ (10%)</th>
        <th>صافي المبلغ المستحق صرفه حالياً</th>
    </tr>
    <tr style="text-align: center; font-size: 12pt;">
        <td>.................... ريال</td>
        <td style="color: red;">( .................... )</td>
        <td style="color: red;">( .................... )</td>
        <td><strong style="color: #047857; font-size: 14pt;">.................... ريال</strong></td>
    </tr>
</table>

<div class="snd-box-info">
    <strong>المبلغ المستحق كتابةً:</strong> فقط .................................................................................... ريال يمني لا غير.
</div>
"""
        },

        # ═════════════════════════════════════════════════════════════════════
        # 4. إدارة المشتريات والمخازن والعقود (🏢 PROC-WH)
        # ═════════════════════════════════════════════════════════════════════
        {
            "template_name": "طلب شراء واحتياج مواد ومعدات (Purchase Requisition)",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة المشتريات والمخازن والعقود",
            "description": "طلب احتياج وشراء مواد وأجهزة ومستلزمات تشغيلية ومكتبية.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #fffbeb;"><strong>الإدارة الطالبة:</strong></td>
        <td style="width: 30%;">..............................</td>
        <td style="width: 20%; background-color: #fffbeb;"><strong>رقم طلب الاحتياج:</strong></td>
        <td style="width: 30%;">{{ doc.name or 'REQ-....' }}</td>
    </tr>
    <tr>
        <td style="background-color: #fffbeb;"><strong>تاريخ الطلب:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
        <td style="background-color: #fffbeb;"><strong>درجة الأهمية:</strong></td>
        <td>[ ] عاجل وطارئ &nbsp;&nbsp; [ ] اعتيادي</td>
    </tr>
</table>

<h4 style="color: #b45309; margin: 12px 0 6px 0;">جدول الأصناف والمواصفات الفنية المطلوبة:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #fef3c7; text-align: center;">
        <th style="width: 6%;">م</th>
        <th style="width: 34%;">اسم الصنف والمواصفات الفنية بدقة</th>
        <th style="width: 15%;">الوحدة</th>
        <th style="width: 15%;">الكمية المطلوبة</th>
        <th style="width: 30%;">الغرض ومكان الاستخدام</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td>............................................................</td>
        <td style="text-align: center;">عدد / حبة</td>
        <td style="text-align: center;">......</td>
        <td>............................................................</td>
    </tr>
    <tr>
        <td style="text-align: center;">2</td>
        <td>............................................................</td>
        <td style="text-align: center;">عدد / كرتون</td>
        <td style="text-align: center;">......</td>
        <td>............................................................</td>
    </tr>
</table>

<div class="snd-box-gray">
    <strong>إفادة إدارة المخازن بعدم التوفر:</strong><br>
    نفيدكم بأنه تم فحص أرصدة المخازن وتبين عدم توفر الأصناف المذكورة أعلاه في المخزون، وتوصي بالشراء.<br>
    <strong>أمين المخزن:</strong> .................... &nbsp;&nbsp;&nbsp;&nbsp; <strong>التوقيع:</strong> ....................
</div>
"""
        },
        {
            "template_name": "إذن صرف وخروج مواد وأصناف من المخزن",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة المشتريات والمخازن والعقود",
            "description": "إذن صرف مواد مسجلة وموثقة بالمخزن لصالح إدارة أو موظف محدد.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم إذن الصرف:</strong></td>
        <td style="width: 30%;">{{ doc.name or 'OUT-WH-....' }}</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>تاريخ الصرف:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>يُصرف للأخ / الإدارة:</strong></td>
        <td colspan="3"><strong>................................................................................</strong></td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>اسم المخزن:</strong></td>
        <td>المخزن الرئيسي</td>
        <td style="background-color: #f8fafc;"><strong>رقم طلب الاحتياج المعتمد:</strong></td>
        <td>..............................</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #f1f5f9; text-align: center;">
        <th style="width: 8%;">م</th>
        <th style="width: 22%;">رقم الصنف (Item Code)</th>
        <th style="width: 40%;">اسم الصنف والبيان</th>
        <th style="width: 15%;">الوحدة</th>
        <th style="width: 15%;">الكمية المصروفة</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td style="text-align: center;">ITM-001</td>
        <td>............................................................</td>
        <td style="text-align: center;">عدد</td>
        <td style="text-align: center; font-weight: bold;">......</td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f8fafc; text-align: center;">
        <th style="width: 33%;">أمين المخزن (المسلّم)</th>
        <th style="width: 33%;">مدير إدارة المخازن (المعتمد)</th>
        <th style="width: 34%;">المستلم الفعلي (الموظف)</th>
    </tr>
    <tr style="text-align: center; height: 50px;">
        <td>....................</td>
        <td>....................</td>
        <td>....................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "محضر فتح مظاريف وعطاءات توريد",
            "category": "محضر فحص واستلام",
            "is_public": 0,
            "department": "إدارة المشتريات والمخازن والعقود",
            "description": "توثيق فتح مظاريف المناقصات والعطاءات والأسعار والضمانات البنكية.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم المناقصة / الممارسة:</strong></td>
        <td style="width: 30%;">{{ doc.name or 'TND-2026-....' }}</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>تاريخ وساعة الفتح:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }} - الساعة 11:00 ص</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>موضوع المناقصة:</strong></td>
        <td colspan="3"><strong style="color: #0f4c81;">توريد وتجهيز ........................................................................</strong></td>
    </tr>
</table>

<p style="line-height: 1.8;">
اجتمعت لجنة فتح المظاريف المشكلة بموجب القرار الإداري رقم (....)، بحضور مندوبي الشركات المتقدمة بعطاءاتهم، وتم فض المظاريف ورصد البيانات كالتالي:
</p>

<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #fef3c7; text-align: center;">
        <th style="width: 6%;">م</th>
        <th style="width: 30%;">اسم الشركة / المورد المتقدم</th>
        <th style="width: 20%;">قيمة العطاء المالي</th>
        <th style="width: 24%;">الضمان البنكي الابتدائي</th>
        <th style="width: 20%;">موقف العطاء الفني</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td>شركة ........................................</td>
        <td style="text-align: center;">............ $ / ريال</td>
        <td>صالح حتى: ..../..../2026م</td>
        <td style="text-align: center; color: green;">مستوفٍ ومقبول</td>
    </tr>
    <tr>
        <td style="text-align: center;">2</td>
        <td>شركة ........................................</td>
        <td style="text-align: center;">............ $ / ريال</td>
        <td>صالح حتى: ..../..../2026م</td>
        <td style="text-align: center; color: green;">مستوفٍ ومقبول</td>
    </tr>
</table>

<div class="snd-box-info">
    <strong>قرار اللجنة:</strong> إحالة العطاءات المقبولة إلى لجنة التحليل الفني والمالي المشتركة لاستكمال التقييم وإعداد جدول المقارنة.
</div>
"""
        },

        # ═════════════════════════════════════════════════════════════════════
        # 5. إدارة الشؤون القانونية والمناقصات (🏢 LEG-TND)
        # ═════════════════════════════════════════════════════════════════════
        {
            "template_name": "إنذار تعاقدي وإشعار إخلال بشروط التوريد/التنفيذ",
            "category": "إشعار رسمي",
            "is_public": 0,
            "department": "إدارة الشؤون القانونية والمناقصات",
            "description": "إنذار قانوني شديد اللهجة للمقاولين والموردين المخالفين لالتزاماتهم التعاقدية.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #fef2f2;"><strong>إلى السادة / شركة:</strong></td>
        <td style="width: 40%;"><strong>............................................................</strong></td>
        <td style="width: 15%; background-color: #fef2f2;"><strong>التاريخ:</strong></td>
        <td style="width: 25%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #fef2f2;"><strong>رقم العقد وتاريخه:</strong></td>
        <td>عقد رقم: ............ بتاريخ: .... / ....</td>
        <td style="background-color: #fef2f2;"><strong>درجة الخطورة:</strong></td>
        <td><span class="snd-badge-red">إنذار قانوني نهائي</span></td>
    </tr>
</table>

<div class="snd-box-danger">
    <strong style="font-size: 13pt;">الموضوع: إشعار وإنذار نهائي بالإخلال بالالتزامات التعاقدية</strong>
</div>

<p style="line-height: 1.8; text-align: justify;">
بالإشارة إلى العقد المبرم معكم المشار إليه أعلاه لتنفيذ/توريد (........................................)، وحيث إنكم قد أخللتم بالتزاماتكم المحددة في البند (....) من العقد، والمتمثلة في:
</p>
<ul style="line-height: 1.8;">
    <li>التأخر غير المبرر في تسليم الأعمال/الأصناف عن الموعد المحدد المنتهي بتاريخ .... / .... / 2026م.</li>
    <li>توريد مكونات غير مطابقة للمواصفات القياسية المتفق عليها في كراسة الشروط.</li>
</ul>

<div class="snd-box-gold">
    <strong>⚠️ التوجيه والمهلة القانونية:</strong><br>
    ننذركم بضرورة تصحيح هذه المخالفات واستكمال التوريد والالتزام التام خلال مهلة أقصاها <strong>(7) سبعة أيام</strong> من تاريخ استلامكم هذا الإنذار، وفي حال انقضاء المهلة دون معالجة، سيتم اتخاذ الإجراءات القانونية الصارمة، بما فيها مصادرة الضمان البنكي، وتطبيق غرامات التأخير، وتنفيذ العقد على حسابكم طبقاً لأحكام القانون.
</div>
"""
        },
        {
            "template_name": "صيغة ملحق تمديد عقد وتعديل فترة التنفيذ",
            "category": "عقد واتفاقية",
            "is_public": 0,
            "department": "إدارة الشؤون القانونية والمناقصات",
            "description": "صيغة قانونية محكمة لملحق تمديد فترة عقد أو تعديل نطاق العمل دون نزاع.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 25%; background-color: #f8fafc;"><strong>ملحق عقد رقم:</strong></td>
        <td style="width: 25%;">01 للعقد رقم: ............</td>
        <td style="width: 25%; background-color: #f8fafc;"><strong>تاريخ تحرير الملحق:</strong></td>
        <td style="width: 25%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الطرف الأول:</strong></td>
        <td>المؤسسة / الإدارة العامة</td>
        <td style="background-color: #f8fafc;"><strong>الطرف الثاني:</strong></td>
        <td>شركة / مقاول: ..............................</td>
    </tr>
</table>

<h4 style="color: #1e3a8a; margin: 12px 0 6px 0;">التمهيد والاتفاق:</h4>
<p style="line-height: 1.8; text-align: justify;">
حيث إنه بتاريخ ..../..../2026م تم إبرام العقد الأصلي رقم (....)، ونظراً لظروف القوة القاهرة / طلب أعمال إضافية معتمدة، اتفق الطرفان بكامل الأهلية المعتبرة على ما يلي:
</p>
<ol style="line-height: 1.8;">
    <li><strong>البند الأول:</strong> تمديد فترة التنفيذ المحددة في العقد الأصلي لمدة (......) يوماً إضافية، بحيث يصبح تاريخ الانتهاء النهائي هو: .... / .... / 2026م.</li>
    <li><strong>البند الثاني:</strong> يلتزم الطرف الثاني بتمديد صلاحية الضمان البنكي لحسن التنفيذ لتغطي كامل فترة التمديد الجديدة.</li>
    <li><strong>البند الثالث:</strong> تظل كافة بنود وشروط العقد الأصلي سارية ونافذة فيما لم يرد بشأنه نص خاص في هذا الملحق.</li>
</ol>

<table style="width: 100%; margin-top: 30px; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f1f5f9; text-align: center;">
        <th style="width: 50%;">الطرف الأول (المؤسسة)</th>
        <th style="width: 50%;">الطرف الثاني (المقاول/المورد)</th>
    </tr>
    <tr style="text-align: center; height: 60px;">
        <td>التوقيع والختم: ....................</td>
        <td>التوقيع والختم: ....................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "محضر تحقيق إداري رسمي وسماع أقوال",
            "category": "تقرير إداري",
            "is_public": 0,
            "department": "إدارة الشؤون القانونية والمناقصات",
            "description": "توثيق إجراءات التحقيق الإداري وسماع أقوال الموظفين في الوقائع المحالة.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم التحقيق:</strong></td>
        <td style="width: 30%;">INV-2026-....</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>تاريخ وساعة الجلسة:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }} - الساعة ......</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>المحقق القانوني:</strong></td>
        <td>المستشار / ..............................</td>
        <td style="background-color: #f8fafc;"><strong>كاتب التحقيق:</strong></td>
        <td>..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>اسم المحقق معه:</strong></td>
        <td><strong>............................................</strong></td>
        <td style="background-color: #f8fafc;"><strong>الوظيفة والإدارة:</strong></td>
        <td>..............................</td>
    </tr>
</table>

<p style="line-height: 1.8;">
فتح المحضر بمعرفتنا نحن المحقق الموضح أعلاه، بمقر الإدارة القانونية، وذلك للتحقيق في موضوع الشكوى/المخالفة المقيدة برقم (.....)، وبسؤال المحقق معه أجاب بالآتي:
</p>

<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #f8fafc;">
        <td style="width: 15%; font-weight: bold; color: #1e3a8a;">س (1):</td>
        <td style="width: 85%;">ما قولك فيما هو منسوب إليك بشأن ................................................................؟</td>
    </tr>
    <tr>
        <td style="font-weight: bold; color: green;">ج (1):</td>
        <td>..........................................................................................................................................................</td>
    </tr>
    <tr style="background-color: #f8fafc;">
        <td style="font-weight: bold; color: #1e3a8a;">س (2):</td>
        <td>هل لديك شهود أو مستندات مؤيدة لما تفضلت به؟</td>
    </tr>
    <tr>
        <td style="font-weight: bold; color: green;">ج (2):</td>
        <td>..........................................................................................................................................................</td>
    </tr>
</table>

<div class="snd-box-gray">
    أقفل المحضر في ساعته وتاريخه بعد أن تليت عليه أقواله فأيدها وصادق عليها بتوقيعه.<br>
    <strong>توقيع المحقق معه:</strong> .................... &nbsp;&nbsp;&nbsp;&nbsp; <strong>المحقق القانوني:</strong> ....................
</div>
"""
        },

        # ═════════════════════════════════════════════════════════════════════
        # 6. إدارة تقنية المعلومات والتحول الرقمي (🏢 IT-DIG)
        # ═════════════════════════════════════════════════════════════════════
        {
            "template_name": "طلب صلاحيات وفتح حسابات مستخدمين على الأنظمة",
            "category": "طلب إداري/مالي",
            "is_public": 0,
            "department": "إدارة تقنية المعلومات والتحول الرقمي",
            "description": "طلب منح أو تعديل صلاحيات دخول على السيرفرات والبريد وقواعد بيانات ERPNext.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f0f9ff;"><strong>اسم الموظف:</strong></td>
        <td style="width: 30%;">{{ frappe.session.user_fullname or frappe.session.user }}</td>
        <td style="width: 20%; background-color: #f0f9ff;"><strong>الرقم الوظيفي:</strong></td>
        <td style="width: 30%;">..............................</td>
    </tr>
    <tr>
        <td style="background-color: #f0f9ff;"><strong>الإدارة / القسم:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f0f9ff;"><strong>البريد الإلكتروني:</strong></td>
        <td>{{ frappe.session.user }}</td>
    </tr>
    <tr>
        <td style="background-color: #f0f9ff;"><strong>نوع الطلب:</strong></td>
        <td colspan="3">[ ] مستخدم جديد &nbsp;&nbsp; [ ] ترقية صلاحيات حالية &nbsp;&nbsp; [ ] إلغاء وتجميد حساب</td>
    </tr>
</table>

<h4 style="color: #0284c7; margin: 12px 0 6px 0;">الأنظمة والصلاحيات والمجموعات المطلوبة:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #e0f2fe; text-align: center;">
        <th style="width: 30%;">اسم النظام / التطبيق</th>
        <th style="width: 35%;">الأدوار المطلوبة (Roles)</th>
        <th style="width: 35%;">مستوى الوصول (قراءة / كتابة / اعتماد)</th>
    </tr>
    <tr>
        <td>نظام الفواتير والمخازن (ERPNext)</td>
        <td>Accounts User / Stock User</td>
        <td>[ ] إدخال وتعديل [ ] استعراض وتقارير</td>
    </tr>
    <tr>
        <td>منظومة المراسلات والبريد الرسمي</td>
        <td>Mail User / Doc Approval</td>
        <td>[ ] كامل الصلاحيات</td>
    </tr>
</table>

<div class="snd-box-info">
    <strong>تعهد أمن وسرية المعلومات:</strong> يتعهد الموظف بالحفاظ التام على سرية كلمة المرور وعدم مشاركتها مع أي طرف آخر واستخدام النظام للأغراض الرسمية فقط.
</div>
"""
        },
        {
            "template_name": "تقرير فحص عطل ومعاينة صيانة أجهزة وشبكات",
            "category": "تقرير إداري",
            "is_public": 0,
            "department": "إدارة تقنية المعلومات والتحول الرقمي",
            "description": "تقرير فحص فني للأجهزة المتعطلة وبيان جدوى الإصلاح أو الاستبدال.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f0f9ff;"><strong>رقم بطاقة الصيانة:</strong></td>
        <td style="width: 30%;">TKT-IT-....</td>
        <td style="width: 20%; background-color: #f0f9ff;"><strong>تاريخ الفحص:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f0f9ff;"><strong>نوع الجهاز / الطراز:</strong></td>
        <td>..............................</td>
        <td style="background-color: #f0f9ff;"><strong>الرقم التسلسلي (S/N):</strong></td>
        <td>............................................</td>
    </tr>
    <tr>
        <td style="background-color: #f0f9ff;"><strong>الموقع / الإدارة المستخدمة:</strong></td>
        <td colspan="3">................................................................................</td>
    </tr>
</table>

<h4 style="color: #0284c7; margin: 12px 0 6px 0;">التشخيص الفني للعطل ونتائج الفحص:</h4>
<div style="border: 1px dashed #94a3b8; padding: 12px; background-color: #fafafa; line-height: 1.8;">
<strong>وصف العطل المرصود:</strong> ............................................................................................................................<br>
<strong>القطع المتضررة:</strong> [ ] لوحة أم (Motherboard) &nbsp; [ ] قرص تخزين (SSD) &nbsp; [ ] مزود طاقة &nbsp; [ ] أخرى
</div>

<h4 style="color: #0284c7; margin: 15px 0 6px 0;">التوصية الفنية وقرار الصيانة:</h4>
<div class="snd-box-warning">
    [ ] قابل للإصلاح محلياً بتكلفة تقديرية: ( ............ ريال ) لشراء قطع غيار.<br>
    [ ] مغطى بالضمان وساري المفعول ويُحال للوكيل المعتمد.<br>
    [ ] غير مجدٍ اقتصادياً ويُوصى بشطبه واستبداله بجهاز جديد.
</div>
"""
        },
        {
            "template_name": "بلاغ أمني لحادثة أو اختراق سيبراني (Incident Report)",
            "category": "إشعار رسمي",
            "is_public": 0,
            "department": "إدارة تقنية المعلومات والتحول الرقمي",
            "description": "توثيق فوري وعاجل لحوادث أمن المعلومات والبرمجيات الخبيثة وتدابير الاحتواء.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #fef2f2;"><strong>رقم الحادثة الأمنية:</strong></td>
        <td style="width: 30%;">SEC-INC-....</td>
        <td style="width: 20%; background-color: #fef2f2;"><strong>وقت الرصد الدقيق:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.now_datetime() }}</td>
    </tr>
    <tr>
        <td style="background-color: #fef2f2;"><strong>مستوى التهديد:</strong></td>
        <td><span class="snd-badge-red">CRITICAL - حرج جداً</span></td>
        <td style="background-color: #fef2f2;"><strong>الأنظمة المتأثرة:</strong></td>
        <td>............................................</td>
    </tr>
</table>

<div class="snd-box-danger">
    <strong style="font-size: 13pt;">وصف الحادثة السيبرانية والمؤشرات المرصودة:</strong><br>
    ..........................................................................................................................................................................
</div>

<h4 style="color: #dc2626; margin: 12px 0 6px 0;">إجراءات الاحتواء العاجلة المتخذة فوراً:</h4>
<ul style="line-height: 1.8;">
    <li>عزل السيرفرات والأجهزة المصابة عن الشبكة الداخلية (Network Isolation).</li>
    <li>إعادة تعيين كلمات مرور الحسابات الحساسة وتعطيل مفاتيح API المعنية.</li>
    <li>أخذ لقطات فورية للذاكرة وفحص ملفات السجلات (Forensic Log Analysis).</li>
</ul>
"""
        },

        # ═════════════════════════════════════════════════════════════════════
        # 7. إدارة الرقابة الداخلية والتفتيش (🏢 AUD-COMP)
        # ═════════════════════════════════════════════════════════════════════
        {
            "template_name": "محضر ضبط وإثبات واقعة مخالفة مالية أو إدارية",
            "category": "تقرير إداري",
            "is_public": 0,
            "department": "إدارة الرقابة الداخلية والتفتيش",
            "description": "محضر رسمي قانوني لضبط المخالفات والتجاوزات وحفظ الأدلة الثبوتية.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #faf5ff;"><strong>رقم محضر الضبط:</strong></td>
        <td style="width: 30%;">AUD-REC-....</td>
        <td style="width: 20%; background-color: #faf5ff;"><strong>تاريخ وساعة الواقعة:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }} - الساعة ......</td>
    </tr>
    <tr>
        <td style="background-color: #faf5ff;"><strong>مقر التفتيش / الإدارة:</strong></td>
        <td colspan="3">................................................................................</td>
    </tr>
    <tr>
        <td style="background-color: #faf5ff;"><strong>أعضاء لجنة التفتيش:</strong></td>
        <td colspan="3">1. ........................................ &nbsp;&nbsp;|&nbsp;&nbsp; 2. ........................................</td>
    </tr>
</table>

<h4 style="color: #7c3aed; margin: 12px 0 6px 0;">تفاصيل ووقائع المخالفة المضبوطة:</h4>
<p style="line-height: 1.8; text-align: justify;">
بناءً على الصلاحيات المخولة لإدارة الرقابة والتفتيش، وأثناء النزول الميداني الفجائي تبين بالدليل القاطع وجود التجاوزات التالية:
</p>
<div class="snd-box-danger">
    1. ....................................................................................................................................<br>
    2. ....................................................................................................................................
</div>

<h4 style="color: #7c3aed; margin: 12px 0 6px 0;">الأدلة والمستندات التحفظية:</h4>
<p style="line-height: 1.8;">
تم التحفظ على المستندات والأوليات المؤيدة لهذه المخالفة والمتمثلة في: ....................................................................
</p>

<table style="width: 100%; margin-top: 25px; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f3e8ff; text-align: center;">
        <th style="width: 50%;">عضو الرقابة والتفتيش</th>
        <th style="width: 50%;">توقيع الحاضر أثناء الضبط</th>
    </tr>
    <tr style="text-align: center; height: 50px;">
        <td>....................</td>
        <td>....................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "إشعار استيفاء ملاحظات وتوصيات تقرير الرقابة",
            "category": "إشعار رسمي",
            "is_public": 0,
            "department": "إدارة الرقابة الداخلية والتفتيش",
            "description": "إشعار إغلاق الملاحظات الرقابية بعد تصحيحها من الإدارة المعنية.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 25%; background-color: #faf5ff;"><strong>الإدارة المعنية بالتصحيح:</strong></td>
        <td style="width: 25%;">..............................</td>
        <td style="width: 25%; background-color: #faf5ff;"><strong>رقم تقرير الرقابة السابق:</strong></td>
        <td style="width: 25%;">AUD-REP-....</td>
    </tr>
    <tr>
        <td style="background-color: #faf5ff;"><strong>تاريخ الاستيفاء والإغلاق:</strong></td>
        <td>{{ frappe.utils.today() }}</td>
        <td style="background-color: #faf5ff;"><strong>حالة الاستيفاء:</strong></td>
        <td><span class="snd-badge-green">مستوفى ومغلق بنجاح</span></td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #f3e8ff; text-align: center;">
        <th style="width: 40%;">الملاحظة الرقابية السابقة</th>
        <th style="width: 40%;">الإجراء التصحيحي المتخذ فعلياً</th>
        <th style="width: 20%;">قرار لجنة التدقيق</th>
    </tr>
    <tr>
        <td>............................................................</td>
        <td>تم تقديم المستندات وإجراء التسوية المحاسبية</td>
        <td style="text-align: center; color: green; font-weight: bold;">معتمد ومغلق ✅</td>
    </tr>
</table>
"""
        },

        # ═════════════════════════════════════════════════════════════════════
        # 8. إدارة المراسلات والسكرتارية العامة (🏢 SEC-GEN)
        # ═════════════════════════════════════════════════════════════════════
        {
            "template_name": "بيان وإرسالية تسليم بريد ومعاملات سرية باليد",
            "category": "إشعار رسمي",
            "is_public": 0,
            "department": "إدارة المراسلات والسكرتارية العامة",
            "description": "حافظة تسليم وتسلم المعاملات والظروف والبريد السري مناولة باليد.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم الحافظة:</strong></td>
        <td style="width: 30%;">POST-2026-....</td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>تاريخ الإرسال:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>اسم مندوب التوصيل:</strong></td>
        <td>............................................</td>
        <td style="background-color: #f8fafc;"><strong>درجة السرية:</strong></td>
        <td><span class="snd-badge-red">سري ومناولة باليد</span></td>
    </tr>
</table>

<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr style="background-color: #f1f5f9; text-align: center;">
        <th style="width: 6%;">م</th>
        <th style="width: 20%;">رقم الصادر / المعاملة</th>
        <th style="width: 34%;">الجهة المرسل إليها المعاملة</th>
        <th style="width: 20%;">اسم المستلم وصفته</th>
        <th style="width: 20%;">توقيع المستلم وتاريخه</th>
    </tr>
    <tr>
        <td style="text-align: center;">1</td>
        <td style="text-align: center;">{{ doc.name or '......' }}</td>
        <td>............................................................</td>
        <td>..............................</td>
        <td>التوقيع: ....................</td>
    </tr>
    <tr>
        <td style="text-align: center;">2</td>
        <td style="text-align: center;">......</td>
        <td>............................................................</td>
        <td>..............................</td>
        <td>التوقيع: ....................</td>
    </tr>
</table>
"""
        },
        {
            "template_name": "بطاقة مسار ومتابعة تدفق معاملة عاجلة",
            "category": "مذكرة داخلية",
            "is_public": 0,
            "department": "إدارة المراسلات والسكرتارية العامة",
            "description": "بطاقة تدفق وتتبع الإحالات والتوقيت بين مختلف الإدارات للمعاملات الهامة.",
            "template_content": """
<table style="width: 100%; border: 1px solid #cbd5e1; margin-bottom: 16px;">
    <tr>
        <td style="width: 20%; background-color: #f8fafc;"><strong>رقم المعاملة العام:</strong></td>
        <td style="width: 30%;"><strong style="color: #0f4c81;">{{ doc.name or '......' }}</strong></td>
        <td style="width: 20%; background-color: #f8fafc;"><strong>تاريخ ورود المعاملة:</strong></td>
        <td style="width: 30%;">{{ frappe.utils.today() }}</td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>الجهة / المصدر الوارد منه:</strong></td>
        <td>............................................</td>
        <td style="background-color: #f8fafc;"><strong>درجة الأسبقية:</strong></td>
        <td><span class="snd-badge-orange">عاجل وهام</span></td>
    </tr>
    <tr>
        <td style="background-color: #f8fafc;"><strong>موجز الموضوع:</strong></td>
        <td colspan="3">................................................................................................................</td>
    </tr>
</table>

<h4 style="color: #0f4c81; margin: 12px 0 6px 0;">سجل مسار وتدرج المعاملة بين الإدارات:</h4>
<table style="width: 100%; border: 1px solid #cbd5e1;">
    <tr style="background-color: #f1f5f9; text-align: center;">
        <th style="width: 25%;">الإدارة المحال إليها</th>
        <th style="width: 20%;">تاريخ ووقت الاستلام</th>
        <th style="width: 35%;">الإجراء المتخذ والتوجيه</th>
        <th style="width: 20%;">اسم وتوقيع المستلم</th>
    </tr>
    <tr>
        <td>إدارة الشؤون القانونية</td>
        <td style="text-align: center;">{{ frappe.utils.today() }}</td>
        <td>لدراسة الجوانب التعاقدية وإبداء الرأي</td>
        <td>....................</td>
    </tr>
    <tr>
        <td>إدارة الشؤون المالية</td>
        <td style="text-align: center;">.... / .... / 2026م</td>
        <td>لتدقيق الاعتماد المالي والمطابقة</td>
        <td>....................</td>
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
        else:
            doc = frappe.get_doc("Sanad Document Template", name)
            doc.is_public = t["is_public"]
            doc.department = t["department"]
            doc.category = t["category"]
            doc.description = t["description"]
            doc.template_content = content
            doc.save(ignore_permissions=True)
            print(f"Updated (body-only): {name}")

    frappe.db.commit()
    print("All body-only templates installed successfully!")

if __name__ == "__main__":
    setup_clean_templates()

