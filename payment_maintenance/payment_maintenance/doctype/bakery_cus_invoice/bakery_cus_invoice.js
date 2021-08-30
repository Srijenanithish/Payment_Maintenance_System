// Copyright (c) 2021, Srijena_Nithish and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bakery Cus Invoice', {
	// refresh: function(frm) {

	// }
	//var Bagels = 30;
	qty: function(frm){
		if(frm.doc.qty && frm.doc.qty >0){
			var Bagels = 20;
			var Snacks = 40;
			var Muffins = 60;
			var Rolls = 35;
			var Biscuits = 10;
			if(frm.doc.items == 'Bagels'){
				frm.doc.total_amount = frm.doc.qty * Bagels;
				frm.refresh_fields();
			}
			else if(frm.doc.items == 'Snacks'){
				frm.doc.total_amount = frm.doc.qty * Snacks;
				frm.refresh_fields();
			}
			else if(frm.doc.items == 'Rolls'){
				frm.doc.total_amount = frm.doc.qty * Rolls;
				frm.refresh_fields();
			}
			else if(frm.doc.items == 'Muffins'){
				frm.doc.total_amount = frm.doc.qty * Muffins;
				frm.refresh_fields();
			}
			else if(frm.doc.items == 'Biscuits'){
				frm.doc.total_amount = frm.doc.qty * Biscuits;
				frm.refresh_fields();
			}
			else{
				frm.doc.total_amount = frm.doc.qty * 30;
				frm.refresh_fields();
			}
		}
	},
	amount_paid : function(frm){
		if(frm.doc.total_amount >0){
			frm.doc.balance_amount_to_pay = frm.doc.total_amount - frm.doc.amount_paid;
			frm.refresh_fields();
		}

	}
	//selling_price: function(frm){
	//	if(frm.doc.qty && frm.doc.qty >0){
	//		frm.doc.total_amount = frm.doc.qty * frm.doc.selling_price;
	//		frm.refresh_fields();
	//	}

	//}
});
