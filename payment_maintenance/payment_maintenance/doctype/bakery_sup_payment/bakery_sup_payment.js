// Copyright (c) 2021, Srijena_Nithish and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bakery Sup Payment', {
	// refresh: function(frm) {

	// }
	paid_amount : function(frm){
		if(frm.doc.total_amount >0){
			frm.doc.remaining_to_pay = frm.doc.total_amount - frm.doc.paid_amount;
			frm.refresh_fields();
		}

	}
});
