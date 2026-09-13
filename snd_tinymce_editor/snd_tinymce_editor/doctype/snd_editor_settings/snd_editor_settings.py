# Copyright (c) 2024, Sanad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.utils import clear_cache

class SNDEditorSettings(Document):
	def on_update(self):
		clear_cache()
		frappe.clear_cache()
