# Copyright (c) 2025, Kalutu and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		total_distance = 0
		for item in self.items:
			total_distance += item.distance
		
		self.total_amount = total_distance * self.rate
