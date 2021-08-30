# Copyright (c) 2021, Srijena_Nithish and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class BakeryItems(WebsiteGenerator):
	def on_submit(self):
		if self.selling_cost > 0 :
			if frappe.db.exists("Bakery Warehouse",{'item': self.item_name}):
				frappe.msgprint(__('This Item Already exists'));
			else:
				stock_entry = frappe.new_doc("Bakery Warehouse")
				stock_entry.item = self.item_name
				#stock_entry.qty = self.qty
				stock_entry.save()		
