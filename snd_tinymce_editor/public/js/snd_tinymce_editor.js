

frappe.ui.form.ControlTextEditor = class ControlTextEditor extends frappe.ui.form.ControlTextEditor {
  make_wrapper() {
      super.make_wrapper();
  }
  make_input() {
    this.has_input = true;
    this.is_tinymce_editor = this.is_tiny_editor();
    if (this.is_tinymce_editor) {
      this.make_tiny_editor();
    } else {
      this.make_quill_editor();
    }
  }

  save_doc_if_dirty() {
      if (this.frm && this.frm.is_dirty()) {
        this.frm.save();
        // this.activeEditor.setDirty(false);
      }
  }

  make_doc_dirty() {
    if (this.frm && !this.frm.is_dirty() && !this.frm.doc.__islocal) {
        this.frm.dirty();
    }
  }

  is_tiny_editor(){
    let doctype = this.doctype;
    let fieldname = this.df.fieldname;
    if (!frappe.boot.tinymce_editor_config) return false;
    this.toolbar = frappe.boot.tinymce_editor_config.toolbar;
    this.plugins = frappe.boot.tinymce_editor_config.plugins;
    this.menubar = frappe.boot.tinymce_editor_config.menubar;
    if (
      ["1", 1].includes(
        frappe.boot.tinymce_editor_config.apply_on_all_default_editors
      )
    )
      return true;
    if (
      frappe.boot.tinymce_editor_config.fields.find(
        (item) =>
          item.editor_doctype == doctype &&
          item.editor_name == fieldname &&
          !item.disabled
      )
    ) return true;

    return false;
  }

  make_tiny_editor() {
    const self = this;
    this.quill_container = $('<div>').appendTo(this.input_area);
    window.tinyMCE.EditorManager.baseURL = "/assets/snd_tinymce_editor/tinymce";
    window.tinyMCE.init({
        target: this.input_area,
        license_key: 'gpl',
        toolbar: self.toolbar || false,
        font_size_formats: '10px 11px 12px 14px 15px 16px 18px 24px 36px',
        plugins: self.plugins || '',
        menubar: self.menubar || false,
        suffix: ".min",
        powerpaste_googledocs_import: "prompt",
        // entity_encoding: 'raw',
        convert_urls: true,
        toolbar_sticky: false,
        promotion: false,
        link_default_target: "_blank",
        highlight_on_focus: false,
        // min_height: 400,
        // height : 400,
        // max_height: 600,
        branding: false,
        language: $('html').attr('lang') || "en" ,
        elementpath: false,
        readonly: !!self.df.read_only || this.frm.doc.docstatus == 1,
        skin: $('html').attr('data-theme-mode') == "dark" ? 'oxide-dark' : 'oxide',
        content_css:  $('html').attr('data-theme-mode') == "dark" ? 'dark' : 'default',
        // language_url: '/path/to/language/pack/fi.js',
        body_class : "snd-tiny-editor",
        resize: true,
        toolbar_mode: 'floating',
        // forced_root_block : 'div',
        newline_behavior: 'block',
        image_description: false,
        // editable_root: false,
        end_container_on_empty_block: true,
        setup: function(editor) {
            self.editor_id = editor.id
            editor.on('Change', function(e) {
              self.frm
                .$wrapper.find('button[data-label="Save"]')
                .on("click", function () {
                  self.parse_validate_and_set_in_model(e.level.content);
                });
            });
            editor.on('Dirty', function (e) {
              self.make_doc_dirty();
              tinymce.activeEditor.isNotDirty = true;
            });
            editor.on('init', function (e) {
              if(self.value){
                editor.setContent(self.value);
              }
            });
            editor.addShortcut('ctrl+s', 'Save Changes', function() {
              let content = tinymce.get(editor.id).getContent();
              self.parse_validate_and_set_in_model(content);
              self.save_doc_if_dirty();
            });
        }
    });
    this.activeEditor = tinymce.activeEditor
  }
  
  set_formatted_input_quill(value){
    if (!this.quill) return;
    if (value === this.get_input_value()) return;
    if (!value) {
      // clear contents for falsy values like '', undefined or null
      this.quill.setText("");
      return;
    }

    // set html without triggering a focus
    const delta = this.quill.clipboard.convert({ html: value, text: "" });
    this.quill.setContents(delta);
  }

  set_formatted_input_tiny(value){
    if (!this.activeEditor) return;
    if (value ===  this.activeEditor.getContent()) return;
    if(!value){
      this.activeEditor.setContent("")
      return;
    }
    this.activeEditor.setContent(value)
  }

  set_formatted_input(value) {
    if (this.is_tinymce_editor) {
      this.set_formatted_input_tiny(value);
    } else {
      this.set_formatted_input_quill(value);
    }
	}
 
}