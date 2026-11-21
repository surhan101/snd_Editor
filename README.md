# SND TinyMCE Rich Text Editor V2.2 📝✨

> **محرر نصوص متقدم واحترافي لبيئة Frappe / ERPNext مبني على TinyMCE 7 بتصميم صفحة A4 المستمرة، استيراد ملفات Word (.docx)، نظام نماذج الإدارات والدوائر، وتقارير تتبع الاستخدام.**
> 
> *Enterprise-grade TinyMCE 7 Rich Text Editor integration for Frappe / ERPNext featuring a continuous A4 page layout, one-click MS Word (.docx) import, department-based template governance, audit usage reports, floating quickbars, and ultra-high performance for large documents.*

---

## 🌟 أبرز المميزات الجديدة في الإصدار 2.2 (What's New in V2.2)

### 📥 1. استيراد ملفات مايكروسوفت وورد (One-Click Word .docx Import)
- زر مباشر في شريط الأدوات والقوائم: **📥 استيراد Word (.docx)**.
- تحويل المستندات فورياً إلى HTML نظيف ومتوافق مع المحرر باستخدام محرك `mammoth.browser` المضمن محلياً دون الحاجة لأي خوادم خارجية.
- استيراد الفقرات، العناوين، القوائم، وتنسيقات الجداول بكفاءة عالية.

### 🏢 2. حوكمة النماذج بحسب الإدارات والدوائر (Department-Based Template Governance)
- **عزل الصلاحيات:** كل إدارة أو دائرة لا تشاهد إلا النماذج المخصصة لها، مع قسم مخصص للنماذج العامة المتاحة للجميع (`is_public`).
- **مصفوفة الإدارات المشتركة:** إمكانية إتاحة نموذج محدد لعدة إدارات في آن واحد عبر جدول `allowed_departments`.
- **أمان الصلاحيات:** التحكم بالنماذج محصور بمسؤولي النظام أو حاملي دور **`Sanad Template Manager`**.

### 📊 3. تقارير تفصيلية لتتبع استخدام النماذج (Audit & Usage Tracking Report)
- تسجيل آلي فوري في جدول `Sanad Template Usage Log` عند قيام أي مستخدم بإدراج نموذج، شاملاً (اسم النموذج، المستخدم، الإدارة، المستند المستهدف، التاريخ والوقت).
- تقرير تحليلي متكامل **`Sanad Template Usage Summary`** يتضمن:
  - بطاقات إحصائية (إجمالي الاستخدام، عدد النماذج النشطة، أكثر النماذج طلباً، والإدارة الأكثر تفاعلاً).
  - رسم بياني شريطي مقارن (Bar Chart) يعكس كثافة استخدام النماذج عبر الإدارات.
  - فلاتر متقدمة بحسب الفترة الزمنية، الإدارة، والنموذج.

### 📋 4. أشرطة الأدوات الذكية السريعة (Contextual Quickbars)
- **شريط عائم عند تحديد النصوص (Quick Selection Toolbar):** يظهر فور تظليل أي كلمة أو فقرة لتقديم خيارات التنسيق السريع (عريض، مائل، تلوين، محاذاة) دون الحاجة للصعود لشريط الأدوات الرئيسي.
- **شريط أدوات الجداول الفوري (Quick Table Toolbar):** يظهر تلقائياً بمجرد النقر داخل أي خلية أو جدول لتقديم عمليات الجداول الحيوية (إدراج وحذف الصفوف والأعمدة، دمج الخلايا، وتعديل الخصائص).

### ⚡ 5. معالجة الجداول وتنظيف النسخ واللصق من Word و PDF
- القضاء التام على خطأ الكونسول `table_column_resizing` باعتماد الوضع المعياري `resizetable` مع الحفاظ على الأبعاد النسبية المرنة.
- فلاتر تنقية تلقائية (`paste_preprocess` و `paste_postprocess`) لتجريد نصوص Word و PDF من مخلفات MSO والوسوم الزائدة.
- ضبط الجداول تلقائياً بأسلوب `table-layout: fixed; width: 100%` لضمان عدم خروج الأعمدة عن هوامش صفحة A4 المطبوعة.
- فرض اتجاه النصوص العربية `dir="rtl"` تلقائياً على كل فقرة أو عنصر يحتوي حروفاً عربية.

### 🚀 6. استقرار فائق وتحمل المستندات الضخمة (Up to 500k Words)
- استبدال التزامن اللحظي بآلية **Debounced Two-Way Sync** ذكية بفترة (650ms) وتجاهل ضغطات مفاتيح التنقل، مما يمنع تجمد المتصفح نهائياً.
- ضبط مستويات التراجع (`custom_undo_redo_levels: 25`) لحماية ذاكرة التخزين للمتصفح وضمان سلاسة الكتابة في العقود والتقارير الطويلة.

### 🎨 7. تنسيقات بصرية متقدمة (Advanced Visual Styling)
- **صناديق التنبيه (Callout Boxes):** معلومات، تحذير، نجاح، وتنبيه هام بتصميم عربي حديث.
- **الشارات والوسوم (Status Badges):** شارات ملونة للحالات (معتمد، قيد المراجعة، ملغى، مسودة).
- خيارات تباعد الأسطر المباشرة (Line Heights من 1 إلى 3)، الأكورديون القابل للطي، وفواصل الصفحات للطباعة.

### 📚 8. حزمة 50 نموذجاً رسمياً شاملاً (50 Comprehensive Templates)
- توفير 50 نموذجاً إدارياً وقانونياً وفنياً جاهزاً تغطي كافة الإدارات (الموارد البشرية، الشؤون القانونية، المالية، المشتريات والمخازن، الرقابة والتفتيش، تقنية المعلومات، السكرتارية).
- جميع النماذج خالية تماماً من الترويسات والتذييلات الثابتة للتوافق المثالي مع الأوراق الرسمية المطبوعة مسبقاً (Letterhead).

---

## 🚀 التثبيت والترقية (Installation & Update)

### 📥 تثبيت جديد على البنش (New Installation)
```bash
cd ~/frappe-bench
bench get-app https://github.com/surhan101/snd_Editor.git snd_tinymce_editor
bench --site <sitename> install-app snd_tinymce_editor
bench --site <sitename> migrate
bench build --app snd_tinymce_editor
bench --site <sitename> clear-cache
bench restart
```

### 🔄 تحديث نسخة سابقة إلى V2.2 (Updating to V2.2)
```bash
cd ~/frappe-bench/apps/snd_tinymce_editor
git pull upstream main

cd ~/frappe-bench
bench --site <sitename> migrate
bench build --app snd_tinymce_editor
bench --site <sitename> clear-cache
bench restart
```

---

## ⚙️ الإعدادات وحوكمة النماذج (Configuration & Governance)

1. **إعدادات المحرر (`SND Editor Settings`):**
   - **Apply On All Default Editors:** تفعيل محرر TinyMCE المتطور لجميع حقول `Text Editor` على كامل النظام.
   - **Apply On Specifics Editors:** تخصيص تفعيل المحرر على حقول ودوكتايبات محددة.

2. **إدارة الإدارات والدوائر (`Sanad Department`):**
   - تعريف الإدارات وربط المستخدمين بها عبر جدول المستخدمين الداخلي لتحديد النماذج التي يحق لهم الوصول إليها.

3. **صلاحيات النماذج (`Sanad Document Template`):**
   - تحديد ما إذا كان النموذج عاماً (`is_public`) متاحاً للجميع أو مخصصاً لإدارة محددة، مع خيار منحه لإدارات إضافية.
   - يُشترط دور **`Sanad Template Manager`** أو مسؤول النظام لإضافة وتعديل النماذج.

4. **التقرير التحليلي لاستخدام النماذج (`Sanad Template Usage Summary`):**
   - تقرير قياسي من نوع Script Report يتيح قياس تفاعل الموظفين مع القوالب والإدارات الأكثر إنتاجية.

---

## 📂 هيكل الـ DocTypes والتقارير المضمنة (DocTypes & Reports)

| النوع | الاسم البرمجي | الوصف |
| :--- | :--- | :--- |
| **DocType** | `SND Editor Settings` | الإعدادات العامة للمحرر وتحديد الحقول المطبقة |
| **DocType** | `Sanad Document Template` | قوالب المستندات والعقود المربوطة بالإدارات |
| **DocType** | `Sanad Department` | بطاقة الإدارة أو الدائرة وربط مستخدميها |
| **DocType** | `Sanad Department User` | جدول فرعي لربط المستخدمين بالإدارات |
| **DocType** | `Sanad Template Department` | جدول فرعي للإدارات المشتركة المصرح لها بالنموذج |
| **DocType** | `Sanad Template Usage Log` | سجل التتبع والتدقيق الآلي لاستخدام النماذج |
| **DocType** | `Sanad Document Snippet` | الديباجات والمقتطفات النصية السريعة |
| **DocType** | `Sanad Snippet Category` | تصنيفات المقتطفات والنصوص |
| **Report** | `Sanad Template Usage Summary` | تقرير تحليلي وإحصائي شامل لاستخدام النماذج مع رسم بياني |

---

## 📄 الترخيص (License)
MIT License - مفتوح المصدر ومتاح للاستخدام والتطوير.
