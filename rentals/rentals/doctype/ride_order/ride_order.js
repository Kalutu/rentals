// Copyright (c) 2025, Kalutu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
		if (frm.doc.status == "New") {
			frm.add_custom_button(
				"Accept",
				() => {
					// change status to accepted
					frm.set_value("status", "Accepted");
					// Save form
					frm.save();
				},
				"Actions"
			);
			frm.add_custom_button(
				"Reject",
				() => {
					// change status to accepted
					frm.set_value("status", "Rejected");
					// Save form
					frm.save();
				},
				"Actions"
			);
		}
	},
});
