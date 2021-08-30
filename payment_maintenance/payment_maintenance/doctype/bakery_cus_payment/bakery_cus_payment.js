// Copyright (c) 2021, Srijena_Nithish and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bakery Cus Payment', {
	// refresh: function(frm) {

	// }
	amount_paid : function(frm){
		if(frm.doc.total_amount >0){
			frm.doc.balance_amount = frm.doc.total_amount - frm.doc.amount_paid;
			frm.refresh_fields();
		}

	}
});
