// Copyright (c) 2024, Sanad and contributors
// For license information, please see license.txt

frappe.ui.form.on('SND Editor Settings', {
	refresh: function(frm) {
		frm.set_value('toolbar_options', 'undo redo | bold italic underline strikethrough | fontfamily fontsize blocks | alignleft aligncenter alignright alignjustify | ltr rtl | outdent indent |  numlist bullist checklist |  forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview print | insertfile image media pageembed template link anchor codesample | showcomments addcomment | footnotes | mergetags');
		frm.set_value('plugins_options', 'preview importcss searchreplace autolink  directionality code visualblocks visualchars fullscreen image link media codesample table charmap pagebreak nonbreaking anchor insertdatetime advlist lists wordcount help charmap quickbars emoticons accordion');
		frm.set_value('menubar_options', 'file edit view insert format tools table help');
		frm.refresh_field('menubar_options');
	}
});
