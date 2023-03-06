import frappe
from frappe.utils import getdate

def set_loyalty_balance(doc, method):
	if not frappe.db.exists("Sales Invoice", doc.name):
		return

	# check if loyalty_balance custom field exists and create it otherwise
	if not frappe.db.exists("Custom Field", {"dt": "Sales Invoice", "fieldname": "loyalty_balance"}):
		frappe.get_doc({
			"doctype": "Custom Field",
			"dt": "Sales Invoice",
			"fieldname": "loyalty_balance",
			"label": "Loyalty Balance",
			"fieldtype": "Int",
			"insert_after": "loyalty_points",
			"read_only": 1
		}).insert(ignore_permissions=True)
		
	loyalty_balance = get_loyalty_balance(doc)

	if int(doc.loyalty_balance) != int(loyalty_balance):
		doc.reload()
		doc.loyalty_balance = loyalty_balance
		doc.save()
		frappe.db.commit()
		frappe.reload_doc("ERPNext Loyalty Enhancements", "doctype", "Sales Invoice")
		

@frappe.whitelist()
def get_loyalty_balance(doc):
	company = doc.company

	loyalty_point_details = []

	loyalty_point_details = frappe._dict(
		frappe.get_all(
			"Loyalty Point Entry",
			filters={
				"customer": doc.customer,
				"expiry_date": (">=", getdate()),
			},
			group_by="company",
			fields=["company", "sum(loyalty_points) as loyalty_points"],
			as_list=1,
		)
	)

	loyalty_balance = 0

	if loyalty_point_details:
		loyalty_balance = loyalty_point_details.get(company)

	return loyalty_balance