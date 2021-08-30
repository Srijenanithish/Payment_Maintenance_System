// Copyright (c) 2021, Srijena_Nithish and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bakery Sup Invoice', {
	// refresh: function(frm) {

	// }
	qty: function(frm){
		if(frm.doc.selling_price && frm.doc.selling_price >0){
			frm.doc.total_amount = frm.doc.qty * frm.doc.selling_price;
			frm.refresh_fields();
		}
	},
	selling_price: function(frm){
		if(frm.doc.qty && frm.doc.qty >0){
			frm.doc.total_amount = frm.doc.qty * frm.doc.selling_price;
			frm.refresh_fields();
		}

	},
	amount_paid : function(frm){
		if(frm.doc.total_amount >0){
			frm.doc.balance_amount_to_pay = frm.doc.total_amount - frm.doc.amount_paid;
			frm.refresh_fields();
		}

	},
});
