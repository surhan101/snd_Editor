frappe.ui.form.on('Sanad Department', {
    refresh(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('عرض نماذج الإدارة'), function() {
                frappe.set_route('List', 'Sanad Document Template', { department: frm.doc.name });
            }, __('إجراءات'));
        }
    }
});

