import frappe

@frappe.whitelist()
def get_name():
    return "Dan Kalutu"