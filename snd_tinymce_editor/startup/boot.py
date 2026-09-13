import frappe

def boot_session(bootinfo):
  if not frappe.session.get("user") in ("Guest", None):
    try:
      tinymce_editor_config = {}
      
      values = frappe.db.get_values(
        "SND Editor Settings",
        "SND Editor Settings",
        ["toolbar", "plugins", "menubar", "apply_on_all_default_editors"],
        as_dict=1,
      )
      if values and len(values) > 0:
        val = values[0]
        sanad_editor_items = frappe.get_all(
          "Sanad Editor items",
          fields=["editor_doctype", "editor_name", "disabled"],
        ) if frappe.db.exists("DocType", "Sanad Editor items") else []

        tinymce_editor_config["toolbar"] = getattr(val, "toolbar", None)
        tinymce_editor_config["plugins"] = getattr(val, "plugins", None)
        tinymce_editor_config["menubar"] = getattr(val, "menubar", None)
        tinymce_editor_config["apply_on_all_default_editors"] = getattr(val, "apply_on_all_default_editors", None)
        tinymce_editor_config["fields"] = sanad_editor_items

        bootinfo.update({
          "tinymce_editor_config": tinymce_editor_config
        })
    except Exception:
      pass
      
  return bootinfo