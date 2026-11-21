frappe.provide('frappe.ui.form');

frappe.ui.form.ControlTextEditor = class ControlTextEditor extends frappe.ui.form.ControlTextEditor {
    make_input() {
        this.has_input = true;
        this.is_tinymce_editor = this._snd_is_tiny_editor();
        if (this.is_tinymce_editor) {
            this._snd_make_tiny_editor();
        } else {
            this.make_quill_editor();
        }
    }

    /* ─── هل يجب تفعيل TinyMCE؟ ─── */
    _snd_is_tiny_editor() {
        const doctype = this.doctype;
        const fieldname = this.df && this.df.fieldname;
        const cfg = frappe.boot && frappe.boot.tinymce_editor_config;
        if (!cfg) return false;

        if (["1", 1, true].includes(cfg.apply_on_all_default_editors)) {
            return true;
        }

        const fields = cfg.fields || [];
        return !!fields.find(
            (item) =>
                item.editor_doctype == doctype &&
                item.editor_name == fieldname &&
                !item.disabled
        );
    }

    /* ─── التحقق من إمكانية التعديل ─── */
    _snd_is_editable() {
        if (this.df && (this.df.read_only || this.df.disabled)) return false;
        if (!this.frm || !this.frm.doc) return true;

        const doc = this.frm.doc;

        if (this.frm.perm && this.frm.perm[0] && !this.frm.perm[0].write) {
            return false;
        }

        if (doc.docstatus === 1 || doc.docstatus === 2) {
            return false;
        }

        return true;
    }

    /* ─── تهيئة TinyMCE كصفحة A4 احترافية مع دعم الجداول واللصق الفائق ─── */
    _snd_make_tiny_editor() {
        const self = this;

        this.quill_container = $('<div>').appendTo(this.input_area);

        window.tinyMCE.EditorManager.baseURL = "/assets/snd_tinymce_editor/tinymce";

        const is_dark = $('html').attr('data-theme-mode') === 'dark';
        const lang = $('html').attr('lang') || 'ar';
        const is_editable = this._snd_is_editable();

        const is_admin = Boolean(
            frappe.session && (
                frappe.session.user === 'Administrator' ||
                (frappe.user_roles && (
                    frappe.user_roles.includes('System Manager') ||
                    frappe.user_roles.includes('Administrator')
                ))
            )
        );

        /* أنماط CSS لصفحة A4 القياسية مع حماية الهوامش والجداول */
        const a4_content_css = `
            @import url('https://fonts.googleapis.com/css2?family=Alexandria:wght@400;600;700&family=Almarai:wght@400;700;800&family=Amiri:ital,wght@0,400;0,700;1,400&family=Aref+Ruqaa:wght@400;700&family=Cairo:wght@400;600;700;800&family=Changa:wght@400;600;700&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Lateef:wght@400;700&family=Mada:wght@400;700&family=Marhey:wght@400;700&family=Noto+Kufi+Arabic:wght@400;600;700&family=Noto+Naskh+Arabic:wght@400;700&family=Readex+Pro:wght@400;600;700&family=Reem+Kufi:wght@400;700&family=Tajawal:wght@400;500;700&display=swap');

            html {
                background-color: #e2e8f0;
                padding: 24px 0;
                margin: 0;
            }
            body.snd-tiny-editor {
                width: 210mm !important;
                max-width: 210mm !important;
                min-height: 297mm !important;
                margin: 0 auto 35px auto !important;
                padding: 20mm !important;
                background-color: #ffffff !important;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12), 0 1px 4px rgba(0, 0, 0, 0.08) !important;
                box-sizing: border-box !important;
                overflow-wrap: break-word !important;
                word-break: break-word !important;
                overflow-x: hidden !important;
                font-family: 'Cairo', 'Almarai', 'Segoe UI', Tahoma, Arial, sans-serif !important;
                font-size: 12pt;
                line-height: 1.8;
                color: #2d3748;
                direction: rtl;
                text-align: right;
                position: relative;
            }
            body.snd-tiny-editor img {
                max-width: 100% !important;
                height: auto !important;
            }
            /* جداول ذكية لا تخرق حدود صفحة A4 أبداً */
            body.snd-tiny-editor table {
                width: 100% !important;
                max-width: 100% !important;
                table-layout: fixed !important;
                border-collapse: collapse !important;
                margin: 14px 0 !important;
                box-sizing: border-box !important;
                page-break-inside: auto;
            }
            body.snd-tiny-editor tr {
                page-break-inside: avoid;
                page-break-after: auto;
            }
            body.snd-tiny-editor th, body.snd-tiny-editor td {
                max-width: 100% !important;
                box-sizing: border-box !important;
                word-wrap: break-word !important;
                word-break: break-word !important;
                overflow-wrap: break-word !important;
                white-space: normal !important;
                border: 1px solid #cbd5e1 !important;
                padding: 8px 12px !important;
                vertical-align: middle;
            }
            body.snd-tiny-editor th {
                background-color: #0f4c81 !important;
                color: #ffffff !important;
                font-weight: bold !important;
                text-align: center !important;
            }

            /* صناديق الملاحظات والتنبيهات الملونة (Callouts) */
            .snd-box-info {
                background-color: #f0f9ff !important;
                border: 1px solid #bae6fd !important;
                border-right: 5px solid #0284c7 !important;
                border-radius: 6px !important;
                padding: 12px 16px !important;
                margin: 14px 0 !important;
                color: #0369a1 !important;
            }
            .snd-box-warning {
                background-color: #fffbeb !important;
                border: 1px solid #fde68a !important;
                border-right: 5px solid #d97706 !important;
                border-radius: 6px !important;
                padding: 12px 16px !important;
                margin: 14px 0 !important;
                color: #92400e !important;
            }
            .snd-box-danger {
                background-color: #fef2f2 !important;
                border: 1px solid #fecaca !important;
                border-right: 5px solid #dc2626 !important;
                border-radius: 6px !important;
                padding: 12px 16px !important;
                margin: 14px 0 !important;
                color: #991b1b !important;
            }
            .snd-box-success {
                background-color: #f0fdf4 !important;
                border: 1px solid #bbf7d0 !important;
                border-right: 5px solid #16a34a !important;
                border-radius: 6px !important;
                padding: 12px 16px !important;
                margin: 14px 0 !important;
                color: #166534 !important;
            }
            .snd-box-gold {
                background-color: #fffdf0 !important;
                border: 1px solid #fef08a !important;
                border-right: 5px solid #ca8a04 !important;
                border-radius: 6px !important;
                padding: 12px 16px !important;
                margin: 14px 0 !important;
                color: #854d0e !important;
            }
            .snd-box-gray {
                background-color: #f8fafc !important;
                border: 1px solid #e2e8f0 !important;
                border-right: 5px solid #64748b !important;
                border-radius: 6px !important;
                padding: 12px 16px !important;
                margin: 14px 0 !important;
                color: #334155 !important;
            }

            /* شارات وحالات المعاملة */
            .snd-badge-red {
                display: inline-block !important;
                background-color: #ef4444 !important;
                color: #ffffff !important;
                border-radius: 4px !important;
                padding: 2px 8px !important;
                font-size: 10pt !important;
                font-weight: bold !important;
            }
            .snd-badge-green {
                display: inline-block !important;
                background-color: #10b981 !important;
                color: #ffffff !important;
                border-radius: 4px !important;
                padding: 2px 8px !important;
                font-size: 10pt !important;
                font-weight: bold !important;
            }
            .snd-badge-blue {
                display: inline-block !important;
                background-color: #2563eb !important;
                color: #ffffff !important;
                border-radius: 4px !important;
                padding: 2px 8px !important;
                font-size: 10pt !important;
                font-weight: bold !important;
            }
            .snd-badge-orange {
                display: inline-block !important;
                background-color: #f97316 !important;
                color: #ffffff !important;
                border-radius: 4px !important;
                padding: 2px 8px !important;
                font-size: 10pt !important;
                font-weight: bold !important;
            }
            .snd-badge-purple {
                display: inline-block !important;
                background-color: #8b5cf6 !important;
                color: #ffffff !important;
                border-radius: 4px !important;
                padding: 2px 8px !important;
                font-size: 10pt !important;
                font-weight: bold !important;
            }

            /* أنماط الجداول الإضافية */
            .snd-table-striped tbody tr:nth-child(even) {
                background-color: #f8fafc !important;
            }
            .snd-table-compact th, .snd-table-compact td {
                padding: 5px 8px !important;
                font-size: 10.5pt !important;
            }
            blockquote.snd-quote {
                margin: 16px 0 !important;
                padding: 10px 18px !important;
                border-right: 4px solid #0f4c81 !important;
                background-color: #f8fafc !important;
                color: #334155 !important;
                font-style: italic !important;
            }
            code.snd-code-inline {
                font-family: 'Courier New', Courier, monospace !important;
                background-color: #f1f5f9 !important;
                color: #0f172a !important;
                padding: 2px 6px !important;
                border-radius: 4px !important;
                border: 1px solid #cbd5e1 !important;
            }

            body.snd-tiny-editor[contenteditable="false"],
            body.snd-tiny-editor.tox-edit-area__iframe--readonly {
                background-color: #fafbfc !important;
                cursor: default !important;
                user-select: text !important;
            }

            @media print {
                html {
                    background: transparent !important;
                    padding: 0 !important;
                }
                body.snd-tiny-editor {
                    width: 100% !important;
                    max-width: 100% !important;
                    margin: 0 !important;
                    padding: 0 !important;
                    box-shadow: none !important;
                }
            }
        `;

        const sanad_tools_row = is_admin
            ? 'sanad_templates_btn sanad_snippets_btn smart_vars_btn snd_import_word_btn'
            : 'sanad_templates_btn sanad_snippets_btn snd_import_word_btn';

        tinymce.init({
            target: this.input_area,
            license_key: 'gpl',
            suffix: '.min',
            language: lang,
            skin: is_dark ? 'oxide-dark' : 'oxide',
            content_css: is_dark ? 'dark' : 'default',
            content_style: a4_content_css,
            height: 900,
            min_height: 500,

            /* 1. إصلاح خيار الجداول وتوسيعه ليقبل أي حالة بحرية ودقة واحترافية */
            table_sizing_mode: 'relative',
            table_column_resizing: 'resizetable',
            table_default_attributes: { border: '1' },
            table_default_styles: {
                'width': '100%',
                'border-collapse': 'collapse',
                'table-layout': 'fixed'
            },
            table_toolbar: 'snd_cell_align_btn tablecellvalign | tablecellprops tablecellbackgroundcolor | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol | tablemergecells tablesplitcells | tablerowprops tableprops',
            table_advtab: true,
            table_cell_advtab: true,
            table_row_advtab: true,
            table_grid: true,
            table_style_by_css: true,

            /* 2. أشرطة الأدوات التفاعلية والسياقية (Quickbars) */
            quickbars_selection_toolbar: 'bold italic underline strikethrough | forecolor backcolor | fontfamily fontsize styles | lineheight | alignleft aligncenter alignright alignjustify | removeformat',
            quickbars_table_toolbar: 'snd_cell_align_btn tablecellvalign | tablecellprops tablecellbackgroundcolor | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol | tablemergecells tablesplitcells',
            quickbars_insert_toolbar: false,

            /* شريط أدوات شامل لكافة إمكانيات التنسيق المتقدمة */
            toolbar: [
                'undo redo | fontfamily fontsize blocks styles | lineheight | bold italic underline strikethrough | forecolor backcolor | alignleft aligncenter alignright alignjustify | ltr rtl',
                `${sanad_tools_row} | table snd_cell_align_btn | numlist bullist | outdent indent | subscript superscript | blockquote hr pagebreak insertdatetime | charmap emoticons | link image accordion | removeformat | searchreplace visualblocks fullscreen code`
            ],
            toolbar_mode: 'sliding',
            plugins: (
                'searchreplace autolink directionality code ' +
                'visualblocks fullscreen image link table charmap ' +
                'advlist lists wordcount quickbars accordion preview emoticons ' +
                'insertdatetime pagebreak nonbreaking'
            ),

            /* 3. قائمة التنسيقات المخصصة (Style Formats) */
            style_formats: [
                {
                    title: '📦 صناديق الملاحظات والتنبيهات',
                    items: [
                        { title: 'ℹ️ صندوق ملاحظة إدارية (أزرق)', block: 'div', classes: 'snd-box-info', wrapper: true },
                        { title: '⚠️ صندوق تنبيه وتحذير (برتقالي)', block: 'div', classes: 'snd-box-warning', wrapper: true },
                        { title: '⛔ صندوق قرار أو حظر (أحمر)', block: 'div', classes: 'snd-box-danger', wrapper: true },
                        { title: '✅ صندوق اعتماد وموافقة (أخضر)', block: 'div', classes: 'snd-box-success', wrapper: true },
                        { title: '📌 صندوق شروط والتزامات (مذهب)', block: 'div', classes: 'snd-box-gold', wrapper: true },
                        { title: '📄 بطاقة توثيق إدارية (رمادي)', block: 'div', classes: 'snd-box-gray', wrapper: true }
                    ]
                },
                {
                    title: '🏷️ شارات وحالات المعاملة',
                    items: [
                        { title: '🔴 سري للغاية وعاجل', inline: 'span', classes: 'snd-badge-red' },
                        { title: '🟢 معتمد ونهائي', inline: 'span', classes: 'snd-badge-green' },
                        { title: '🔵 قيد المتابعة والإجراء', inline: 'span', classes: 'snd-badge-blue' },
                        { title: '🟠 هام جداً ومؤجل', inline: 'span', classes: 'snd-badge-orange' },
                        { title: '🟣 للعرض والمصادقة', inline: 'span', classes: 'snd-badge-purple' }
                    ]
                },
                {
                    title: '📊 أنماط الجداول الجاهزة',
                    items: [
                        { title: 'جدول محاسبي مخطط (Zebra)', selector: 'table', classes: 'snd-table-striped' },
                        { title: 'جدول مدمج ومضغوط (Compact)', selector: 'table', classes: 'snd-table-compact' }
                    ]
                },
                {
                    title: '✍️ تنسيقات نصوص واقتباسات',
                    items: [
                        { title: 'اقتباس رسمي فاخر', block: 'blockquote', classes: 'snd-quote' },
                        { title: 'رقم قيد / كود تقني', inline: 'code', classes: 'snd-code-inline' },
                        { title: 'نص إبراز أصفر', inline: 'mark', styles: { 'background-color': '#fef08a', 'padding': '2px 4px', 'border-radius': '2px' } }
                    ]
                }
            ],

            line_height_formats: '1 1.15 1.25 1.5 1.75 2 2.5 3',
            insertdatetime_formats: ['%Y-%m-%d', '%H:%M:%S', '%Y-%m-%d %H:%M:%S', '%d/%m/%Y'],
            menubar: 'file edit view insert format tools table sanad_menu',
            menu: {
                sanad_menu: {
                    title: 'أدوات المحرر',
                    items: is_admin
                        ? 'sanad_templates_menu sanad_snippets_menu smart_vars_menu | snd_import_word_menu | sanad_add_category_menu sanad_add_snippet_menu'
                        : 'sanad_templates_menu sanad_snippets_menu | snd_import_word_menu | sanad_add_category_menu sanad_add_snippet_menu'
                }
            },

            font_family_formats: [
                'Cairo=Cairo, sans-serif',
                'Almarai=Almarai, sans-serif',
                'Tajawal=Tajawal, sans-serif',
                'Amiri=Amiri, serif',
                'Alexandria=Alexandria, sans-serif',
                'Noto Kufi Arabic=Noto Kufi Arabic, sans-serif',
                'Noto Naskh Arabic=Noto Naskh Arabic, serif',
                'IBM Plex Sans Arabic=IBM Plex Sans Arabic, sans-serif',
                'Traditional Arabic=Traditional Arabic, serif',
                'Simplified Arabic=Simplified Arabic, sans-serif',
                'Arial=Arial, Helvetica, sans-serif',
                'Calibri=Calibri, Candara, Segoe, Segoe UI, Optima, Arial, sans-serif',
                'Segoe UI=Segoe UI, Tahoma, Geneva, Verdana, sans-serif',
                'Tahoma=Tahoma, Arial, sans-serif',
                'Times New Roman=Times New Roman, Times, serif',
                'Courier New=Courier New, Courier, monospace'
            ].join('; '),

            font_size_formats: '8pt 9pt 10pt 11pt 12pt 14pt 16pt 18pt 20pt 22pt 24pt 26pt 28pt 36pt 48pt 72pt',
            promotion: false,
            branding: false,
            elementpath: false,
            resize: true,
            newline_behavior: 'block',
            end_container_on_empty_block: true,
            link_default_target: '_blank',
            highlight_on_focus: false,
            body_class: 'snd-tiny-editor',
            readonly: !is_editable,

            /* 3. كفاءة الأداء الفائق (500,000 كلمة دون تجميد المتصفح) */
            custom_undo_redo_levels: 25, // تحديد تاريخ التراجع لمنع انهيار الذاكرة العشوائية في النصوص الضخمة

            /* 4. تنظيف ومعالجة النسخ واللصق من Word و PDF بدقة عالية */
            paste_preprocess: function (plugin, args) {
                let html = args.content;
                if (!html) return;
                // إزالة تعليقات أوفيس التالفة والوسوم الزائدة
                html = html.replace(/<!--[\s\S]*?-->/g, '');
                html = html.replace(/<\/?\w+:[^>]*>/gi, '');
                html = html.replace(/mso-[^;:"]+:[^;"]+;?/gi, '');
                args.content = html;
            },
            paste_postprocess: function (plugin, args) {
                if (!args.node) return;

                // حماية وتعديل كافة الجداول الملصوقة لتناسب هوامش صفحة A4 تماماً
                const tables = args.node.querySelectorAll('table');
                tables.forEach(tbl => {
                    tbl.style.width = '100%';
                    tbl.style.maxWidth = '100%';
                    tbl.style.tableLayout = 'fixed';
                    tbl.style.borderCollapse = 'collapse';
                    tbl.removeAttribute('width');

                    tbl.querySelectorAll('td, th').forEach(cell => {
                        cell.style.maxWidth = '100%';
                        cell.style.wordBreak = 'break-word';
                        cell.style.overflowWrap = 'break-word';
                        cell.style.whiteSpace = 'normal';
                        cell.removeAttribute('width');
                    });
                });

                // ضبط اتجاه RTL التلقائي للفقرات والعناوين والجداول المحتوية على نصوص عربية
                const blocks = args.node.querySelectorAll('p, div, h1, h2, h3, h4, table, ul, ol');
                const arabicRegex = /[\u0600-\u06FF\u0750-\u077F]/;
                blocks.forEach(el => {
                    if (arabicRegex.test(el.textContent)) {
                        el.setAttribute('dir', 'rtl');
                        if (!el.style.textAlign || el.style.textAlign === 'left') {
                            el.style.textAlign = 'right';
                        }
                    }
                });
            },

            setup: function (editor) {
                self._snd_editor = editor;
                self._snd_editor_id = editor.id;

                editor.on('init', function () {
                    self._is_setting_value = true;
                    try {
                        const initVal = self.value || (self.frm && self.frm.doc && self.frm.doc[self.df.fieldname]) || '';
                        if (initVal) {
                            editor.setContent(initVal);
                        }
                    } finally {
                        self._is_setting_value = false;
                    }

                    if (!self._snd_is_editable() && editor.mode) {
                        editor.mode.set('readonly');
                    }
                });

                editor.on('Dirty', function () {
                    self._snd_make_dirty();
                    if (tinymce.activeEditor) {
                        tinymce.activeEditor.isNotDirty = true;
                    }
                });

                // مزامنة ذكية بنظام Debounce (650ms) لإعطاء أقصى سلاسة أثناء الكتابة في المستندات الضخمة
                const debounced_sync = frappe.utils.debounce(() => {
                    self._snd_sync_editor_to_doc(editor);
                }, 650);

                editor.on('input change paste undo redo', function () {
                    debounced_sync();
                });

                editor.on('keyup', function (e) {
                    // تجاهل مفاتيح التوجيه والأسهم لعدم استنزاف المعالج
                    if (e && [16, 17, 18, 37, 38, 39, 40].includes(e.keyCode)) return;
                    debounced_sync();
                });

                editor.on('blur', function () {
                    self._snd_sync_editor_to_doc(editor);
                });

                editor.addShortcut('ctrl+s', 'Save', function (e) {
                    if (e && e.preventDefault) e.preventDefault();
                    self._snd_sync_editor_to_doc(editor);
                    if (self.frm) {
                        self.frm.save();
                    }
                });

                /* ── تسجيل أزرار النماذج والمقتطفات ومواءمة الخلايا واستيراد Word ── */
                self._snd_register_buttons(editor, is_admin);
            }
        });

        this.activeEditor = tinymce.activeEditor;
    }

    /* ─── مزامنة آمنة من المحرر إلى المستند ─── */
    _snd_sync_editor_to_doc(editor) {
        if (this._is_setting_value) return;
        const ed = editor || this._snd_editor || (this._snd_editor_id && tinymce.get(this._snd_editor_id));
        if (!ed || !ed.initialized) return;

        const content = ed.getContent();
        this.value = content;
        if (this.frm && this.frm.doc && this.df && this.df.fieldname) {
            this.frm.doc[this.df.fieldname] = content;
            this._snd_make_dirty();
        }
    }

    /* ─── تحديث حالة التجميد/التحرير عند تحديث النموذج ─── */
    refresh() {
        super.refresh();
        if (this.is_tinymce_editor && this._snd_editor && this._snd_editor.initialized) {
            const is_editable = this._snd_is_editable();
            if (this._snd_editor.mode) {
                this._snd_editor.mode.set(is_editable ? 'design' : 'readonly');
            }
        }
    }

    /* ─── تحميل مكتبة Mammoth لاستيراد ملفات Word محلياً وسحابياً ─── */
    _snd_load_mammoth() {
        return new Promise((resolve, reject) => {
            if (window.mammoth) {
                resolve(window.mammoth);
                return;
            }
            const script = document.createElement('script');
            script.src = "/assets/snd_tinymce_editor/js/mammoth.browser.min.js";
            script.onload = () => {
                if (window.mammoth) resolve(window.mammoth);
                else reject(new Error("Mammoth loaded but window.mammoth is undefined"));
            };
            script.onerror = () => {
                // محاولة التحميل من CDN كاحتياط
                const cdnScript = document.createElement('script');
                cdnScript.src = "https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.6.0/mammoth.browser.min.js";
                cdnScript.onload = () => {
                    if (window.mammoth) resolve(window.mammoth);
                    else reject(new Error("CDN Mammoth failed"));
                };
                cdnScript.onerror = () => reject(new Error("Failed to load Mammoth"));
                document.head.appendChild(cdnScript);
            };
            document.head.appendChild(script);
        });
    }

    /* ─── تسجيل أزرار الشريط وقوائم سند ─── */
    _snd_register_buttons(editor, is_admin) {
        const self = this;
        const current_doctype = self.doctype || (self.frm && self.frm.doctype) || null;

        /* ── زر استيراد ملف وورد (.docx) ── */
        const import_word_action = () => {
            const fileInput = document.createElement('input');
            fileInput.type = 'file';
            fileInput.accept = '.docx';
            fileInput.style.display = 'none';
            document.body.appendChild(fileInput);

            fileInput.onchange = function (e) {
                const file = e.target.files && e.target.files[0];
                if (!file) {
                    fileInput.remove();
                    return;
                }

                frappe.show_alert({ message: __('جاري قراءة واستيراد ملف Word... ⏳'), indicator: 'blue' });

                self._snd_load_mammoth().then(mammoth => {
                    const reader = new FileReader();
                    reader.onload = function (loadEvent) {
                        const arrayBuffer = loadEvent.target.result;
                        mammoth.convertToHtml({ arrayBuffer: arrayBuffer })
                            .then(function (result) {
                                let html = result.value;
                                const container = document.createElement('div');
                                container.innerHTML = html;

                                // ضبط الجداول المستوردة لتتوافق مع معايير A4
                                container.querySelectorAll('table').forEach(tbl => {
                                    tbl.style.width = '100%';
                                    tbl.style.maxWidth = '100%';
                                    tbl.style.tableLayout = 'fixed';
                                    tbl.style.borderCollapse = 'collapse';
                                    tbl.setAttribute('border', '1');
                                    tbl.querySelectorAll('td, th').forEach(cell => {
                                        cell.style.wordBreak = 'break-word';
                                        cell.style.overflowWrap = 'break-word';
                                    });
                                });

                                // ضبط اتجاه النصوص العربية إلى RTL
                                const arabicRegex = /[\u0600-\u06FF\u0750-\u077F]/;
                                container.querySelectorAll('p, table, h1, h2, h3, h4, ul, ol').forEach(el => {
                                    if (arabicRegex.test(el.textContent)) {
                                        el.setAttribute('dir', 'rtl');
                                        el.style.textAlign = 'right';
                                    }
                                });

                                editor.insertContent(container.innerHTML);
                                self._snd_sync_editor_to_doc(editor);
                                frappe.show_alert({ message: __('تم استيراد مستند Word بنجاح ✅'), indicator: 'green' });
                                fileInput.remove();
                            })
                            .catch(function (err) {
                                frappe.msgprint(__('تعذر تحويل ملف Word: ') + (err && err.message ? err.message : err));
                                fileInput.remove();
                            });
                    };
                    reader.readAsArrayBuffer(file);
                }).catch(() => {
                    frappe.msgprint(__('تعذر تحميل مكتبة استيراد Word.'));
                    fileInput.remove();
                });
            };

            fileInput.click();
        };

        editor.ui.registry.addButton('snd_import_word_btn', {
            text: '📥 استيراد Word',
            tooltip: 'استيراد مستند وورد (.docx) وتحويله مباشرة داخل المحرر',
            onAction: import_word_action
        });

        editor.ui.registry.addMenuItem('snd_import_word_menu', {
            text: '📥 استيراد من ملف Word (.docx)...',
            onAction: import_word_action
        });

        /* ── زر مواءمة وضبط النص داخل الخلايا ── */
        editor.ui.registry.addMenuButton('snd_cell_align_btn', {
            text: 'مواءمة الخلية',
            tooltip: 'مواءمة وضبط النص داخل خلايا الجدول',
            fetch: function (cb) {
                cb([
                    {
                        type: 'menuitem',
                        text: '🎯 توسيط كامل (وسط رأسياً + وسط أفقياً)',
                        onAction: () => {
                            self._snd_apply_cell_align(editor, { 'vertical-align': 'middle', 'text-align': 'center' });
                        }
                    },
                    {
                        type: 'menuitem',
                        text: '↔️ ضبط ومواءمة النص (Justify + وسط رأسياً)',
                        onAction: () => {
                            self._snd_apply_cell_align(editor, { 'vertical-align': 'middle', 'text-align': 'justify' });
                        }
                    },
                    {
                        type: 'menuitem',
                        text: '➡️ محاذاة لليمين + وسط رأسياً',
                        onAction: () => {
                            self._snd_apply_cell_align(editor, { 'vertical-align': 'middle', 'text-align': 'right' });
                        }
                    },
                    {
                        type: 'menuitem',
                        text: '⬅️ محاذاة لليسار + وسط رأسياً',
                        onAction: () => {
                            self._snd_apply_cell_align(editor, { 'vertical-align': 'middle', 'text-align': 'left' });
                        }
                    },
                    { type: 'separator' },
                    {
                        type: 'menuitem',
                        text: '⬆️ محاذاة لأعلى الخلية (Top)',
                        onAction: () => {
                            self._snd_apply_cell_align(editor, { 'vertical-align': 'top' });
                        }
                    },
                    {
                        type: 'menuitem',
                        text: '⏺️ محاذاة لوسط الخلية (Middle)',
                        onAction: () => {
                            self._snd_apply_cell_align(editor, { 'vertical-align': 'middle' });
                        }
                    },
                    {
                        type: 'menuitem',
                        text: '⬇️ محاذاة لأسفل الخلية (Bottom)',
                        onAction: () => {
                            self._snd_apply_cell_align(editor, { 'vertical-align': 'bottom' });
                        }
                    },
                    { type: 'separator' },
                    {
                        type: 'menuitem',
                        text: '📐 توزيع أعمدة الجدول بالتساوي (Auto Fit)',
                        onAction: () => {
                            self._snd_distribute_table_cols(editor);
                        }
                    }
                ]);
            }
        });

        /* ── زر النماذج ── */
        editor.ui.registry.addButton('sanad_templates_btn', {
            text: '📄 نماذج',
            tooltip: 'مكتبة نماذج المعاملات الرسمية والعقود',
            onAction: () => self._snd_open_templates_dialog(editor, current_doctype)
        });
        editor.ui.registry.addMenuItem('sanad_templates_menu', {
            text: '📄 مكتبة النماذج...',
            onAction: () => self._snd_open_templates_dialog(editor, current_doctype)
        });

        /* ── زر المقتطفات (مقسّمة بالتصنيفات ومربوطة بالدوكتايب) ── */
        editor.ui.registry.addMenuButton('sanad_snippets_btn', {
            text: '✍️ مقتطفات',
            tooltip: 'ديباجات وصيغ جاهزة (مقدمات، خواتم، شروط، جداول)',
            fetch: function (cb) {
                frappe.call({
                    method: 'snd_tinymce_editor.snd_tinymce_editor.api.templates.get_quick_snippets',
                    args: { target_doctype: current_doctype },
                    callback: function (r) {
                        const snippets = r.message || [];
                        const menuItems = [];

                        const categories = {};
                        snippets.forEach(s => {
                            const cat = s.category || 'أخرى';
                            if (!categories[cat]) categories[cat] = [];
                            categories[cat].push(s);
                        });

                        Object.keys(categories).forEach(cat => {
                            menuItems.push({
                                type: 'nestedmenuitem',
                                text: cat,
                                getSubmenuItems: function () {
                                    return categories[cat].map(s => ({
                                        type: 'menuitem',
                                        text: s.title,
                                        onAction: () => {
                                            editor.insertContent(s.content);
                                            self._snd_sync_editor_to_doc(editor);
                                            frappe.show_alert({ message: __('تم إدراج المقتطف ✅'), indicator: 'green' });
                                        }
                                    }));
                                }
                            });
                        });

                        if (!menuItems.length) {
                            menuItems.push({
                                type: 'menuitem',
                                text: __('لا توجد مقتطفات مضافة'),
                                enabled: false
                            });
                        }

                        menuItems.push({ type: 'separator' });
                        menuItems.push({
                            type: 'menuitem',
                            text: '➕ إضافة مقتطف جديد...',
                            onAction: () => {
                                frappe.new_doc('Sanad Document Snippet');
                            }
                        });

                        cb(menuItems);
                    }
                });
            }
        });
        editor.ui.registry.addMenuItem('sanad_snippets_menu', {
            text: '✍️ المقتطفات والديباجات',
            onAction: () => editor.execCommand('mceMenuButton', false, 'sanad_snippets_btn')
        });

        /* ── {x} المتغيرات الذكية (مقتصرة على الأدمن فقط) ── */
        if (is_admin) {
            editor.ui.registry.addMenuButton('smart_vars_btn', {
                text: '{x} متغير',
                tooltip: 'إدراج حقل ديناميكي من المستند الحالي (خاص بالمسؤولين)',
                fetch: function (cb) {
                    if (!current_doctype) {
                        cb([{ type: 'menuitem', text: 'افتح مستنداً أولاً', enabled: false }]);
                        return;
                    }
                    frappe.call({
                        method: 'snd_tinymce_editor.snd_tinymce_editor.api.templates.get_doctype_fields',
                        args: { target_doctype: current_doctype },
                        callback: function (r) {
                            cb((r.message || []).map(f => ({
                                type: 'menuitem',
                                text: f.label,
                                onAction: () => editor.insertContent(f.value)
                            })));
                        }
                    });
                }
            });
            editor.ui.registry.addMenuItem('smart_vars_menu', {
                text: '{x} متغيرات ذكية',
                onAction: () => editor.execCommand('mceMenuButton', false, 'smart_vars_btn')
            });
        }

        /* ── عناصر إضافية في قائمة أدوات سند ── */
        editor.ui.registry.addMenuItem('sanad_add_category_menu', {
            text: '🏷️ إدارة تصنيفات المقتطفات',
            onAction: () => frappe.set_route('List', 'Sanad Snippet Category')
        });
        editor.ui.registry.addMenuItem('sanad_add_snippet_menu', {
            text: '➕ إضافة ديباجة أو مقتطف جديد',
            onAction: () => frappe.new_doc('Sanad Document Snippet')
        });
    }

    /* ─── تطبيق المحاذاة على خلايا الجدول ─── */
    _snd_apply_cell_align(editor, styles) {
        const node = editor.selection.getNode();
        let targetCell = node ? (node.tagName === 'TD' || node.tagName === 'TH' ? node : node.closest('td, th')) : null;

        if (!targetCell) {
            frappe.show_alert({ message: __('يرجى وضع المؤشر داخل إحدى خلايا الجدول أولاً'), indicator: 'orange' });
            return;
        }

        const selectedCells = editor.dom.select('td[data-mce-selected], th[data-mce-selected]');
        const cellsToApply = (selectedCells && selectedCells.length > 0) ? selectedCells : [targetCell];

        editor.undoManager.transact(() => {
            cellsToApply.forEach(cell => {
                Object.keys(styles).forEach(prop => {
                    cell.style[prop] = styles[prop];
                });
                if (styles['text-align']) {
                    const children = cell.querySelectorAll('p, div, span, h1, h2, h3, h4, h5, h6');
                    children.forEach(child => {
                        child.style['text-align'] = styles['text-align'];
                    });
                }
            });
        });

        frappe.show_alert({ message: __('تمت مواءمة الخلية بنجاح ✅'), indicator: 'green' });
        editor.nodeChanged();
        this._snd_sync_editor_to_doc(editor);
    }

    /* ─── مواءمة وتوزيع أعمدة الجدول بالتساوي ─── */
    _snd_distribute_table_cols(editor) {
        const node = editor.selection.getNode();
        const table = node ? node.closest('table') : null;
        if (!table) {
            frappe.show_alert({ message: __('يرجى وضع المؤشر داخل الجدول أولاً'), indicator: 'orange' });
            return;
        }

        const rows = table.rows;
        if (!rows || !rows.length) return;

        let maxCols = 0;
        for (let r of rows) {
            if (r.cells.length > maxCols) maxCols = r.cells.length;
        }
        if (!maxCols) return;

        const colWidth = (100 / maxCols).toFixed(2) + '%';
        editor.undoManager.transact(() => {
            for (let r of rows) {
                for (let c of r.cells) {
                    c.style.width = colWidth;
                }
            }
            const colgroup = table.querySelector('colgroup');
            if (colgroup) {
                colgroup.innerHTML = '';
                for (let i = 0; i < maxCols; i++) {
                    const col = editor.getDoc().createElement('col');
                    col.style.width = colWidth;
                    colgroup.appendChild(col);
                }
            }
        });
        frappe.show_alert({ message: __('تمت مواءمة وتوزيع أعمدة الجدول بالتساوي ✅'), indicator: 'green' });
        editor.nodeChanged();
        this._snd_sync_editor_to_doc(editor);
    }

    /* ─── نافذة اختيار النموذج مع التصفية بحسب الإدارة والصلاحيات ─── */
    _snd_open_templates_dialog(editor, current_doctype) {
        const self = this;

        frappe.call({
            method: 'snd_tinymce_editor.snd_tinymce_editor.api.templates.get_user_template_permissions',
            callback: function (perm_res) {
                const userPerm = perm_res.message || {};
                const is_admin = userPerm.is_admin_or_manager;
                const user_depts = userPerm.user_departments || [];
                const all_depts = userPerm.all_departments || [];

                frappe.call({
                    method: 'snd_tinymce_editor.snd_tinymce_editor.api.templates.get_templates',
                    args: { target_doctype: current_doctype },
                    callback: function (r) {
                        const templates = r.message || [];

                        if (!templates.length) {
                            frappe.msgprint(__('لا توجد نماذج مخصصة لإدارتك أو مصرح لك بالوصول إليها حالياً.'));
                            return;
                        }

                        // تجميع خيارات الإدارات المتاحة
                        let deptOptions = `<option value="">🌐 عرض الكل (النماذج العامة + نماذج الإدارة)</option>`;
                        deptOptions += `<option value="__public__">🌐 النماذج العامة فقط</option>`;
                        if (is_admin) {
                            all_depts.forEach(d => {
                                deptOptions += `<option value="${d.name}">🏢 ${d.department_name}</option>`;
                            });
                        } else if (user_depts.length) {
                            user_depts.forEach(d => {
                                deptOptions += `<option value="${d}">🏢 ${d}</option>`;
                            });
                        }

                        // شريط أدوات المسؤول
                        const adminToolbar = is_admin ? `
                            <div style="display:flex;gap:6px;align-items:center;">
                                <button class="btn btn-xs btn-primary" id="snd-btn-new-tpl" style="border-radius:4px;">
                                    ➕ إضافة نموذج جديد
                                </button>
                                <button class="btn btn-xs btn-default" id="snd-btn-manage-depts" style="border-radius:4px;">
                                    🏢 إدارة الإدارات والدوائر
                                </button>
                                <button class="btn btn-xs btn-info" id="snd-btn-usage-rep" style="border-radius:4px;">
                                    📊 تقرير الاستخدام
                                </button>
                            </div>
                        ` : '';

                        const renderList = function (listData) {
                            if (!listData.length) {
                                return `<div style="padding:25px;text-align:center;color:var(--text-muted);font-size:13px;">لا توجد نماذج مطابقة للبحث أو التصفية</div>`;
                            }
                            return listData.map((t, i) => {
                                const deptBadge = t.is_public
                                    ? `<span style="background:#10b981;color:#ffffff;padding:2px 6px;border-radius:4px;font-size:10px;font-weight:600;">🌐 عام للجميع</span>`
                                    : `<span style="background:#0f4c81;color:#ffffff;padding:2px 6px;border-radius:4px;font-size:10px;font-weight:600;">🏢 ${t.department || 'إدارة محددة'}</span>`;
                                const catBadge = `<span style="background:#f1f5f9;color:#334155;border:1px solid #cbd5e1;padding:2px 6px;border-radius:4px;font-size:10px;">${t.category || ''}</span>`;
                                const usageText = `<span style="color:#64748b;font-size:11px;">📊 استُخدم: <strong>${t.usage_count || 0}</strong> مرة</span>`;

                                return `
                                <div class="snd-tpl-card${i === 0 ? ' active' : ''}" data-name="${t.name}"
                                    style="padding:10px 12px;border:1px solid var(--border-color);border-radius:6px;
                                           margin-bottom:8px;cursor:pointer;transition:all .15s;background:var(--card-bg);">
                                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                                        <strong style="font-size:13px;color:var(--text-color);">${t.template_name}</strong>
                                        <div style="display:flex;gap:4px;">${deptBadge} ${catBadge}</div>
                                    </div>
                                    ${t.description ? `<div style="font-size:11px;color:var(--text-muted);margin-bottom:4px;line-height:1.4;">${t.description}</div>` : ''}
                                    <div style="display:flex;justify-content:flex-end;">${usageText}</div>
                                </div>`;
                            }).join('');
                        };

                        const d = new frappe.ui.Dialog({
                            title: __('📄 مكتبة النماذج الرسمية (حسب الإدارات والدوائر)'),
                            size: 'extra-large',
                            fields: [{
                                fieldtype: 'HTML',
                                fieldname: 'tpl_html',
                                options: `
                                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid var(--border-color);">
                                    <div style="display:flex;gap:10px;flex:1;max-width:65%;">
                                        <input type="text" id="snd-tpl-search" class="form-control input-sm" placeholder="🔍 بحث سريع في النماذج..." style="flex:1;">
                                        <select id="snd-tpl-dept-filter" class="form-control input-sm" style="flex:1.2;">
                                            ${deptOptions}
                                        </select>
                                    </div>
                                    ${adminToolbar}
                                </div>
                                <div style="display:flex;gap:14px;min-height:430px;">
                                    <div style="flex:1.1;overflow-y:auto;max-height:460px;padding-right:4px;" id="snd-tpl-list">
                                        ${renderList(templates)}
                                    </div>
                                    <div style="flex:1.9;border:1px solid var(--border-color);border-radius:6px;
                                                padding:16px;overflow-y:auto;max-height:460px;
                                                background:var(--control-bg);" id="snd-tpl-preview">
                                        ${templates[0] ? templates[0].template_content : ''}
                                    </div>
                                </div>
                                <style>
                                    .snd-tpl-card:hover { border-color: var(--primary) !important; background: var(--bg-light-gray); }
                                    .snd-tpl-card.active { border-color: #0f4c81 !important; background: #f0f7ff !important; border-width: 2px !important; }
                                </style>`
                            }],
                            primary_action_label: __('إدراج في المحرر ✅'),
                            primary_action: function () {
                                const card = d.$wrapper.find('.snd-tpl-card.active');
                                const tplName = card.data('name');
                                const selected = templates.find(t => t.name === tplName);

                                if (selected && selected.template_content) {
                                    editor.insertContent(selected.template_content);
                                    self._snd_sync_editor_to_doc(editor);

                                    // تسجيل حركة استخدام النموذج في السجل التفصيلي
                                    frappe.call({
                                        method: 'snd_tinymce_editor.snd_tinymce_editor.api.templates.log_template_usage',
                                        args: {
                                            template_name: selected.name,
                                            target_doctype: current_doctype || (self.doctype || null),
                                            target_docname: (self.frm && self.frm.doc && self.frm.doc.name) || null
                                        }
                                    });

                                    d.hide();
                                    frappe.show_alert({ message: __('تم إدراج النموذج وتسجيل استخدامه بنجاح ✅'), indicator: 'green' });
                                }
                            }
                        });

                        d.show();

                        let currentFiltered = [...templates];

                        const applyFilter = function () {
                            const q = (d.$wrapper.find('#snd-tpl-search').val() || '').trim().toLowerCase();
                            const dept = d.$wrapper.find('#snd-tpl-dept-filter').val();

                            currentFiltered = templates.filter(t => {
                                const matchesSearch = !q || (t.template_name && t.template_name.toLowerCase().includes(q)) || (t.description && t.description.toLowerCase().includes(q));
                                let matchesDept = true;
                                if (dept === '__public__') {
                                    matchesDept = Boolean(t.is_public);
                                } else if (dept) {
                                    matchesDept = (t.department === dept) || (t.allowed_depts && t.allowed_depts.includes(dept));
                                }
                                return matchesSearch && matchesDept;
                            });

                            d.$wrapper.find('#snd-tpl-list').html(renderList(currentFiltered));
                            if (currentFiltered.length) {
                                d.$wrapper.find('#snd-tpl-preview').html(currentFiltered[0].template_content);
                            } else {
                                d.$wrapper.find('#snd-tpl-preview').html('<div style="text-align:center;padding:50px;color:var(--text-muted);">لا يوجد نموذج محدد للمعاينة</div>');
                            }
                        };

                        d.$wrapper.on('input', '#snd-tpl-search', applyFilter);
                        d.$wrapper.on('change', '#snd-tpl-dept-filter', applyFilter);

                        d.$wrapper.on('click', '.snd-tpl-card', function () {
                            d.$wrapper.find('.snd-tpl-card').removeClass('active');
                            $(this).addClass('active');
                            const tplName = $(this).data('name');
                            const tpl = templates.find(t => t.name === tplName);
                            if (tpl) {
                                d.$wrapper.find('#snd-tpl-preview').html(tpl.template_content);
                            }
                        });

                        if (is_admin) {
                            d.$wrapper.on('click', '#snd-btn-new-tpl', function () {
                                d.hide();
                                frappe.new_doc('Sanad Document Template');
                            });
                            d.$wrapper.on('click', '#snd-btn-manage-depts', function () {
                                d.hide();
                                frappe.set_route('List', 'Sanad Department');
                            });
                            d.$wrapper.on('click', '#snd-btn-usage-rep', function () {
                                d.hide();
                                frappe.set_route('query-report', 'Sanad Template Usage Summary');
                            });
                        }
                    }
                });
            }
        });
    }

    /* ─── ضبط القيمة ─── */
    set_formatted_input(value) {
        if (this.is_tinymce_editor) {
            this._snd_set_tiny_value(value);
        } else {
            this._snd_set_quill_value(value);
        }
    }

    _snd_set_tiny_value(value) {
        const ed = this._snd_editor || (this._snd_editor_id && tinymce.get(this._snd_editor_id));
        if (!ed || !ed.initialized) return;
        if (value === ed.getContent()) return;

        this._is_setting_value = true;
        try {
            ed.setContent(value || '');
        } finally {
            this._is_setting_value = false;
        }
    }

    _snd_set_quill_value(value) {
        if (!this.quill) return;
        if (value === this.get_input_value()) return;
        if (!value) {
            this.quill.setText('');
            return;
        }
        const delta = this.quill.clipboard.convert({ html: value, text: '' });
        this.quill.setContents(delta);
    }

    /* ─── قراءة قيمة الإدخال ومزامنتها حياً ─── */
    get_input_value() {
        if (this.is_tinymce_editor) {
            const ed = this._snd_editor || (this._snd_editor_id && tinymce.get(this._snd_editor_id));
            if (ed && ed.initialized) {
                const val = ed.getContent();
                this.value = val;
                if (this.frm && this.frm.doc && this.df && this.df.fieldname) {
                    this.frm.doc[this.df.fieldname] = val;
                }
                return val;
            }
            return this.value || (this.frm && this.frm.doc && this.df && this.frm.doc[this.df.fieldname]) || '';
        }
        return super.get_input_value();
    }

    get_value() {
        if (this.is_tinymce_editor) {
            return this.get_input_value();
        }
        return super.get_value();
    }

    /* ─── مساعدات الحفظ وحالة التعديل ─── */
    _snd_make_dirty() {
        if (this.frm && !this.frm.is_dirty() && !this.frm.doc.__islocal) {
            this.frm.dirty();
        }
    }

    _snd_save_if_dirty() {
        if (this.frm && this.frm.is_dirty()) {
            this.frm.save();
        }
    }
};

/* ─── خطاف عام لضمان مزامنة كافة محررات TinyMCE النشطة قبل أي حفظ أو إرسال أو إجراء Workflow ─── */
$(document).on('before_workflow_action submit', function () {
    if (window.tinymce && window.cur_frm && cur_frm.fields) {
        cur_frm.fields.forEach(f => {
            if (f.is_tinymce_editor && f._snd_editor_id) {
                const ed = tinymce.get(f._snd_editor_id);
                if (ed && ed.initialized) {
                    const content = ed.getContent();
                    f.value = content;
                    if (cur_frm.doc && f.df && f.df.fieldname) {
                        cur_frm.doc[f.df.fieldname] = content;
                    }
                }
            }
        });
    }
});

console.log('✅ SND TinyMCE Editor v2.2 loaded (Word Clean Paste + Docx Import + Quickbars + 500K Perf + Resizable Tables)');
