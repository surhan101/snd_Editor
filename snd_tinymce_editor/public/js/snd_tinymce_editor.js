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

    /* ─── تهيئة TinyMCE كصفحة واحدة مستمرة بعرض A4 بتنسيق احترافي ─── */
    _snd_make_tiny_editor() {
        const self = this;

        this.quill_container = $('<div>').appendTo(this.input_area);

        window.tinyMCE.EditorManager.baseURL = "/assets/snd_tinymce_editor/tinymce";

        const is_dark = $('html').attr('data-theme-mode') === 'dark';
        const lang = $('html').attr('lang') || 'en';
        const is_editable = this._snd_is_editable();

        // التحقق من صلاحية الأدمن لعرض زر المتغيرات الذكية
        const is_admin = Boolean(
            frappe.session && (
                frappe.session.user === 'Administrator' ||
                (frappe.user_roles && (
                    frappe.user_roles.includes('System Manager') ||
                    frappe.user_roles.includes('Administrator')
                ))
            )
        );

        // أنماط CSS لصفحة A4 مع تضمين خطوط Google Fonts الاحترافية
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
                font-size: 13pt;
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
            body.snd-tiny-editor table {
                width: 100% !important;
                max-width: 100% !important;
                table-layout: fixed !important;
                border-collapse: collapse !important;
                margin: 14px 0 !important;
                box-sizing: border-box !important;
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
                background-color: #f1f5f9 !important;
                font-weight: bold !important;
                color: #1e293b !important;
                text-align: center !important;
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
            ? 'sanad_templates_btn sanad_snippets_btn smart_vars_btn'
            : 'sanad_templates_btn sanad_snippets_btn';

        tinymce.init({
            target: this.input_area,
            license_key: 'gpl',
            suffix: '.min',
            language: lang,
            skin: is_dark ? 'oxide-dark' : 'oxide',
            content_css: is_dark ? 'dark' : 'default',
            content_style: a4_content_css,
            height: 880,
            min_height: 500,

            table_sizing_mode: 'relative',
            table_column_resizing: 'rescale',
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

            toolbar: [
                'undo redo | fontfamily fontsize blocks | bold italic underline strikethrough | forecolor backcolor | alignleft aligncenter alignright alignjustify | ltr rtl',
                `${sanad_tools_row} | table snd_cell_align_btn | numlist bullist | outdent indent | hr charmap emoticons | link image | removeformat | searchreplace visualblocks fullscreen code`
            ],
            toolbar_mode: 'sliding',
            plugins: (
                'searchreplace autolink directionality code ' +
                'visualblocks fullscreen image link table charmap ' +
                'advlist lists wordcount quickbars accordion preview emoticons'
            ),
            menubar: 'file edit view insert format tools table sanad_menu',
            menu: {
                sanad_menu: {
                    title: 'أدوات المحرر',
                    items: is_admin
                        ? 'sanad_templates_menu sanad_snippets_menu smart_vars_menu | sanad_add_category_menu sanad_add_snippet_menu'
                        : 'sanad_templates_menu sanad_snippets_menu | sanad_add_category_menu sanad_add_snippet_menu'
                }
            },

            font_family_formats: [
                'Arial=Arial, Helvetica, sans-serif',
                'Calibri=Calibri, Candara, Segoe, Segoe UI, Optima, Arial, sans-serif',
                'Segoe UI=Segoe UI, Tahoma, Geneva, Verdana, sans-serif',
                'Tahoma=Tahoma, Arial, sans-serif',
                'Times New Roman=Times New Roman, Times, serif',
                'Cairo=Cairo, sans-serif',
                'Almarai=Almarai, sans-serif',
                'Tajawal=Tajawal, sans-serif',
                'Amiri=Amiri, serif',
                'Alexandria=Alexandria, sans-serif',
                'Noto Kufi Arabic=Noto Kufi Arabic, sans-serif',
                'Noto Naskh Arabic=Noto Naskh Arabic, serif',
                'IBM Plex Sans Arabic=IBM Plex Sans Arabic, sans-serif',
                'Changa=Changa, sans-serif',
                'Readex Pro=Readex Pro, sans-serif',
                'Aref Ruqaa=Aref Ruqaa, serif',
                'Marhey=Marhey, sans-serif',
                'Reem Kufi=Reem Kufi, sans-serif',
                'Lateef=Lateef, serif',
                'Mada=Mada, sans-serif',
                'Traditional Arabic=Traditional Arabic, serif',
                'Simplified Arabic=Simplified Arabic, sans-serif',
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

            setup: function(editor) {
                self._snd_editor = editor;
                self._snd_editor_id = editor.id;

                editor.on('init', function() {
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

                editor.on('Dirty', function() {
                    self._snd_make_dirty();
                    if (tinymce.activeEditor) {
                        tinymce.activeEditor.isNotDirty = true;
                    }
                });

                // مزامنة المحتوى تلقائياً وبأمان عند إدخال المستخدم
                const debounced_sync = frappe.utils.debounce(() => {
                    self._snd_sync_editor_to_doc(editor);
                }, 250);

                editor.on('input change keyup paste undo redo', function() {
                    debounced_sync();
                });

                editor.on('blur', function() {
                    self._snd_sync_editor_to_doc(editor);
                });

                editor.addShortcut('ctrl+s', 'Save', function(e) {
                    if (e && e.preventDefault) e.preventDefault();
                    self._snd_sync_editor_to_doc(editor);
                    if (self.frm) {
                        self.frm.save();
                    }
                });

                /* ── تسجيل أزرار النماذج والمقتطفات ومواءمة الخلايا ── */
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

    /* ─── تسجيل أزرار الشريط وقوائم سند ─── */
    _snd_register_buttons(editor, is_admin) {
        const self = this;
        const current_doctype = self.doctype || (self.frm && self.frm.doctype) || null;

        /* ── زر مواءمة وضبط النص داخل الخلايا ── */
        editor.ui.registry.addMenuButton('snd_cell_align_btn', {
            text: 'مواءمة الخلية',
            tooltip: 'مواءمة وضبط النص داخل خلايا الجدول',
            fetch: function(cb) {
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
            fetch: function(cb) {
                frappe.call({
                    method: 'snd_tinymce_editor.snd_tinymce_editor.api.templates.get_quick_snippets',
                    args: { target_doctype: current_doctype },
                    callback: function(r) {
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
                                getSubmenuItems: function() {
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

    /* ─── نافذة اختيار النموذج ─── */
    _snd_open_templates_dialog(editor, current_doctype) {
        const self = this;
        frappe.call({
            method: 'snd_tinymce_editor.snd_tinymce_editor.api.templates.get_templates',
            args: { target_doctype: current_doctype },
            callback: function(r) {
                const templates = r.message || [];

                if (!templates.length) {
                    frappe.msgprint(__('لا توجد نماذج مضافة. يمكنك إضافتها من قائمة «Sanad Document Template»'));
                    return;
                }

                const list_html = templates.map((t, i) => `
                    <div class="snd-tpl-card${i === 0 ? ' active' : ''}" data-idx="${i}"
                        style="padding:10px 12px;border:1px solid var(--border-color);border-radius:6px;
                               margin-bottom:8px;cursor:pointer;transition:all .15s;">
                        <strong style="font-size:14px;">${t.template_name}</strong>
                        <span class="indicator-pill blue" style="margin-right:8px;font-size:11px;">${t.category || ''}</span>
                        ${t.description ? `<div style="font-size:12px;color:var(--text-muted);margin-top:4px;">${t.description}</div>` : ''}
                    </div>
                `).join('');

                const d = new frappe.ui.Dialog({
                    title: __('📄 مكتبة نماذج المعاملات الرسمية'),
                    size: 'extra-large',
                    fields: [{
                        fieldtype: 'HTML',
                        fieldname: 'tpl_html',
                        options: `
                        <div style="display:flex;gap:14px;min-height:400px;">
                            <div style="flex:1;overflow-y:auto;max-height:430px;" id="snd-tpl-list">
                                ${list_html}
                            </div>
                            <div style="flex:2;border:1px solid var(--border-color);border-radius:6px;
                                        padding:14px;overflow-y:auto;max-height:430px;
                                        background:var(--control-bg);" id="snd-tpl-preview">
                                ${templates[0] ? templates[0].template_content : ''}
                            </div>
                        </div>
                        <style>
                            .snd-tpl-card:hover { border-color: var(--primary) !important; background: var(--bg-light-gray); }
                            .snd-tpl-card.active { border-color: var(--primary) !important; background: var(--bg-light-gray); }
                        </style>`
                    }],
                    primary_action_label: __('إدراج في المحرر'),
                    primary_action: function() {
                        const card = d.$wrapper.find('.snd-tpl-card.active');
                        const idx = parseInt(card.data('idx'));
                        if (!isNaN(idx) && templates[idx]) {
                            editor.setContent(templates[idx].template_content);
                            self._snd_sync_editor_to_doc(editor);
                            d.hide();
                            frappe.show_alert({ message: __('تم إدراج النموذج ✅'), indicator: 'green' });
                        }
                    }
                });

                d.show();

                d.$wrapper.on('click', '.snd-tpl-card', function() {
                    d.$wrapper.find('.snd-tpl-card').removeClass('active');
                    $(this).addClass('active');
                    const idx = parseInt($(this).data('idx'));
                    if (!isNaN(idx) && templates[idx]) {
                        d.$wrapper.find('#snd-tpl-preview').html(templates[idx].template_content);
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
            return this.value || (this.frm && this.frm.doc && this.frm.doc[this.df.fieldname]) || '';
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
$(document).on('before_workflow_action submit', function() {
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

console.log('✅ SND TinyMCE Editor loaded (Secure Two-Way Sync + Workflow Send Protection)');
