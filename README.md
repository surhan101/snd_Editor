# SND TinyMCE Rich Text Editor V2.0 📝✨

> **محرر نصوص متقدم واحترافي لبيئة Frappe / ERPNext مبني على TinyMCE 7 بتصميم صفحة A4 المستمرة ونظام قوالب ومقتطفات ذكي.**
> 
> *Modern, robust TinyMCE 7 Rich Text Editor integration for Frappe / ERPNext featuring a continuous A4 page layout, Arabic & MS Word typography, advanced table cell controls, and a dynamic template & snippet system.*

---

## 🌟 أبرز المميزات (Key Features)

### 📄 1. تنسيق صفحة A4 الحقيقية (Continuous A4 Layout)
- عرض الصفحة بقياس A4 قياسي (`210mm`) مع هوامش وظلال واقعية تحاكي برامج معالجة الكلمات المكتبية (مثل Microsoft Word).
- مواءمة تلقائية للطباعة (`@media print`) لعرض المحتوى بدون ظلال أو هوامش إضافية أثناء الطباعة والتصدير إلى PDF.

### 🔤 2. حزمة الخطوط العربية والإنجليزية الاحترافية (MS Word & Google Fonts)
- دعم كامل لأشهر الخطوط العربية القياسية:
  - **Cairo, Almarai, Tajawal, Amiri, Alexandria, Noto Kufi Arabic, Noto Naskh Arabic, IBM Plex Sans Arabic, Readex Pro, Changa, Aref Ruqaa, Reem Kufi, Lateef, Mada, Traditional Arabic, Simplified Arabic**.
- دعم خطوط الويب والأنظمة القياسية: **Arial, Calibri, Segoe UI, Tahoma, Times New Roman, Courier New**.
- أحجام خطوط قياسية متطابقة مع Word (`8pt` إلى `72pt`).

### 📊 3. أدوات الجداول ومواءمة الخلايا المتقدمة (Table Cell Alignment)
- زر مخصص لمواءمة الخلايا (**مواءمة الخلية**) يتيح التحكم في 9 مواضع للمحاذاة الأفقية والرأسية (أعلى/وسط/أسفل - يمين/وسط/يسار).
- شريط أدوات سياقي يظهر تلقائياً داخل الجداول لتعديل الصفوف، الأعمدة، الخلفيات، وخصائص الخلايا بسهولة.

### 📑 4. نظام القوالب والمقتطفات الجاهزة (Templates & Snippets System)
- **قوالب المستندات (`Sanad Document Template`):** إنشاء وتخصيص قوالب جاهزة للعقود، المراسلات، والتقارير مع إمكانية استعراضها وإدراجها بنقرة زر.
- **المقتطفات والديباجات (`Sanad Document Snippet`):** مكتبة نصوص مصنفة (مقدمات وافتتاحيات، خواتم واعتمادات، شروط وأحكام التعاقد، بنود التوريد والدفع، الضمان والصيانة، جداول حصر الكميات).
- **تصنيفات المقتطفات (`Sanad Snippet Category`):** تنظيم المقتطفات حسب الأقسام والمجالات.

### 🎨 5. مظهر أنيق ودعم الوضع الليلي (Dark / Light Mode)
- شريط أدوات منظم في صفين بدون تشوه عند تغيير أبعاد الشاشة (`toolbar_mode: 'sliding'`).
- توافق كامل مع الوضع الليلي (Dark Mode) في Frappe Desk.

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

### 🔄 تحديث نسخة سابقة (Updating Existing Installation)
```bash
cd ~/frappe-bench/apps/snd_tinymce_editor
git remote add github https://github.com/surhan101/snd_Editor.git 2>/dev/null || git remote set-url github https://github.com/surhan101/snd_Editor.git
git fetch github
git reset --hard github/main

cd ~/frappe-bench
bench --site <sitename> migrate
bench build --app snd_tinymce_editor
bench --site <sitename> clear-cache
bench restart
```

---

## ⚙️ الإعدادات والاستخدام (Configuration)

انتقل إلى شاشة **`SND Editor Settings`** في Frappe Desk:

1. **Apply On All Default Editors:**
   - فعّل هذا الخيار لتطبيق محرر سند TinyMCE على جميع حقول `Text Editor` في النظام تلقائياً.
2. **Apply On Specifics Editors:**
   - جدول فرعي لتحديد حقول محددة فقط في دوكتايبات معينة إذا رغبت في عدم تفعيله على كامل النظام.
3. **أدوات سند (Sanad Tools):**
   - أزرار مباشرة داخل شريط المحرر: **نماذج وقوالب** و **مقتطفات** للوصول السريع للنصوص والديباجات.

---

## 📂 هيكل الـ DocTypes المضمنة

| DocType | الوصف |
| :--- | :--- |
| **`SND Editor Settings`** | إعدادات المحرر العامة وتحديد الحقول المطبقة |
| **`Sanad Document Template`** | قوالب المستندات والعقود الجاهزة |
| **`Sanad Document Snippet`** | الديباجات والمقتطفات النصية وبنود العقود |
| **`Sanad Snippet Category`** | تصنيفات المقتطفات والنصوص |

---

## 📄 الترخيص (License)
MIT License - مفتوح المصدر ومتاح للاستخدام والتطوير.
