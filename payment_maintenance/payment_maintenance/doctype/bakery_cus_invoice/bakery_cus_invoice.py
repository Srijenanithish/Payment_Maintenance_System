# Copyright (c) 2021, Srijena_Nithish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BakeryCusInvoice(Document):
	def validate(self):
		if self.qty >0:
			if frappe.db.exists("Bakery Cus Payment",{'customer': self.customer}):
				existing_amt = frappe.db.get_value("Bakery Cus Payment",{'customer':self.customer},"amount_paid")
				exist_balance_amt = frappe.db.get_value("Bakery Cus Payment",{'customer':self.customer},"balance_amount")
				exist_total_amt = frappe.db.get_value("Bakery Cus Payment",{'customer':self.customer},"total_amount")
				updated_balance_amt = self.balance_amount_to_pay
				updated_amt = self.amount_paid
				updated_total_amt = self.total_amount
				if existing_amt and exist_balance_amt:
					existing_amt = updated_amt
					exist_balance_amt = updated_balance_amt
					exist_total_amt = updated_total_amt
				frappe.db.set_value("Bakery Cus Payment",{'customer': self.customer},"amount_paid",existing_amt)
				frappe.db.set_value("Bakery Cus Payment",{'customer': self.customer},"balance_amount",exist_balance_amt)
				frappe.db.set_value("Bakery Cus Payment",{'customer': self.customer},"balance_amount",exist_total_amt)
			else:
				stock_entry = frappe.new_doc("Bakery Cus Payment")
				stock_entry.customer = self.customer
				stock_entry.balance_amount = self.balance_amount_to_pay
				stock_entry.amount_paid = self.amount_paid
				stock_entry.total_amount = self.total_amount
				stock_entry.save()	

		if self.qty >0:
			if frappe.db.exists("Bakery Warehouse",{'item': self.items}):
				existing_qty = frappe.db.get_value("Bakery Warehouse",{'item':self.items},"qty")
				if existing_qty > self.qty:
					updated_qty = self.qty
					if existing_qty:
						updated_qty -= existing_qty
					frappe.db.set_value("Bakery Warehouse",{'item': self.items},"qty",abs(updated_qty))
				else:
					frappe.throw("---------     There is no Stock Available for this Item      -------<br>-------    Buy some other Item or wait for that Item     -------")	
			else:
				frappe.throw("--------        Sorry The Item chosen is not Available      --------<br>--------     Please request the shop owner for that Item       --------  ")
				#frappe.msgprint("The Item is not Available")
				
				#stock_entry = frappe.new_doc("Bakery Warehouse")
				#stock_entry.item = self.items
				#stock_entry.qty = self.qty
				#stock_entry.save()		
