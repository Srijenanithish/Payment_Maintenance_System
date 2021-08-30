# Copyright (c) 2021, Srijena_Nithish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BakerySupInvoice(Document):
	def validate(self):
		if self.qty >0:
			if frappe.db.exists("Bakery Warehouse",{'item': self.item}):
				existing_qty = frappe.db.get_value("Bakery Warehouse",{'item':self.item},"qty")
				updated_qty = self.qty
				if existing_qty:
					updated_qty += existing_qty
				frappe.db.set_value("Bakery Warehouse",{'item': self.item},"qty",updated_qty)
			else:
				stock_entry = frappe.new_doc("Bakery Warehouse")
				stock_entry.item = self.item
				stock_entry.qty = self.qty
				stock_entry.save()		

		if self.qty > 0:
			if frappe.db.exists("Bakery Sup Payment",{'supplier': self.supplier}):
				existing_amt = frappe.db.get_value("Bakery Sup Payment",{'supplier':self.supplier},"paid_amount")
				exist_balance_amt = frappe.db.get_value("Bakery Sup Payment",{'supplier':self.supplier},"remaining_to_pay")
				exist_total_amt = frappe.db.get_value("Bakery Sup Payment",{'supplier':self.supplier},"total_amount")
				updated_balance_amt = self.balance_amount_to_pay
				updated_amt = self.amount_paid
				updated_total_amt = self.total_amount
				if existing_amt and exist_balance_amt:
					existing_amt = updated_amt
					exist_balance_amt = updated_balance_amt
					exist_total_amt = updated_total_amt
				frappe.db.set_value("Bakery Sup Payment",{'supplier': self.supplier},"paid_amount",existing_amt)
				frappe.db.set_value("Bakery Sup Payment",{'supplier': self.supplier},"remaining_to_pay",exist_balance_amt)
				frappe.db.set_value("Bakery Sup Payment",{'supplier': self.supplier},"total_amount",exist_total_amt)

			else:
				stock_entry = frappe.new_doc("Bakery Sup Payment")
				stock_entry.supplier = self.supplier
				stock_entry.paid_amount = self.amount_paid
				stock_entry.remaining_to_pay = self.balance_amount_to_pay
				stock_entry.total_amount = self.total_amount
				stock_entry.save()	
					
	
