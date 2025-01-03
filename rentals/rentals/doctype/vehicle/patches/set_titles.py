import frappe

def execute():
    vehicles = frappe.db.get_all("Vehicle")

    for v in vehicles:
        vehicle = frappe.get_doc("Vehicle",v)
        vehicle.set_title()
        vehicle.save()

    frappe.db.commit()
