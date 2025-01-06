# Copyright (c) 2025, Kalutu and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Driver(WebsiteGenerator):
	def before_save(self):
		if self.last_name:
			self.full_name = f"{self.first_name} {self.last_name}"	
		else:
			self.full_name = self.first_name
