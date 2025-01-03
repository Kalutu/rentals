# Copyright (c) 2025, Kalutu and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Driver(WebsiteGenerator):
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"	
