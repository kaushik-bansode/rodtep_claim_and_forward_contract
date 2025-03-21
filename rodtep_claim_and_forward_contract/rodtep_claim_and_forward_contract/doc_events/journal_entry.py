import frappe
from frappe.utils import flt
from forward_contract.forward_contract.doctype.forward_contract.forward_contract import ForwardContract

def before_cancel(self, method):
    fwc, parent = frappe.db.get_value("Forward Contract Cancellation", {'journal_entry' : self.name}, ["name", 'parent'])
    
    if fwc:
        frappe.db.sql(f"DELETE FROM `tabForward Contract Cancellation` WHERE name = '{fwc}'")
    
    if parent:
        doc = frappe.get_doc("Forward Contract", parent)
        ForwardContract.calculate_cancellation(doc)
        doc.save()
