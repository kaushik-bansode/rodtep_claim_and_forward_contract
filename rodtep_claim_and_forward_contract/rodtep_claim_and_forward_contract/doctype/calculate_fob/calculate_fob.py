# Copyright (c) 2025, sf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class CalculateFOB(Document):
	def on_submit(self):
		self.create_jv()
	def on_cancel(self):
		self.cancel_jv()
	@frappe.whitelist()
	def update_sales_invoice(self):
		si_doc = frappe.get_doc("Sales Invoice", self.sales_invoice)
		for row in si_doc.get("items"):
			rate_details = frappe.db.get_value("Item", row.item_code, ["custom_duty_drawback_rate", "custom_rodtep_rate"], as_dict=True)
			self.append("sales_invoice_items", {
				"item": row.item_code,
				"item_name":row.item_name,
				"base_amount": row.base_amount,
				"amount":row.amount,
				"rodtep_rate": rate_details.get("custom_rodtep_rate"),
				"duty_drawback_rate": rate_details.get("custom_duty_drawback_rate")
			})
	
	def create_jv(self):
		if self.total_duty_drawback:
			drawback_receivable_account = frappe.get_value("Company", self.company, "custom_duty_drawback_receivable_account")
			# frappe.throw(str(drawback_receivable_account))
			drawback_income_account = frappe.get_value("Company", self.company, "custom_duty_drawback_income_account")
			drawback_cost_center = frappe.get_value("Company", self.company, "custom_duty_drawback_cost_center")
			if not drawback_receivable_account:
				frappe.throw(_("Set Duty Drawback Receivable Account in Company"))
			elif not drawback_income_account:
				frappe.throw(_("Set Duty Drawback Income Account in Company"))
			elif not drawback_cost_center:
				frappe.throw(_("Set Duty Drawback Cost Center in Company"))
			else:
				jv = frappe.new_doc("Journal Entry")
				jv.voucher_type = "Duty Drawback Entry"
				jv.posting_date = self.posting_date
				jv.company = self.company
				jv.cheque_no = self.name
				jv.cheque_date = self.posting_date
				jv.user_remark = "Duty draw back against " + self.name + " for " + self.customer
				jv.append("accounts", {
					"account": drawback_receivable_account,
					"cost_center": drawback_cost_center,
					"debit_in_account_currency": self.total_duty_drawback
				})
				jv.append("accounts", {
					"account": drawback_income_account,
					"cost_center": drawback_cost_center,
					"credit_in_account_currency": self.total_duty_drawback
				})
				try:
					jv.save(ignore_permissions=True)
					jv.submit()
				except Exception as e:
					frappe.throw(str(e))
				else:
					self.db_set('duty_drawback_jv',jv.name)

		if self.get('total_rodtep'):
			meis_receivable_account = frappe.db.get_value("Company", { "company_name": self.company}, "custom_rodtep_receivabale_account")
			meis_income_account = frappe.db.get_value("Company", { "company_name": self.company}, "custom_rodtep_income_account")
			meis_cost_center = frappe.db.get_value("Company", { "company_name": self.company}, "custom_rodtep_cost_center")
			if not meis_receivable_account:
				frappe.throw(_("Set RODTEP Receivable Account in Company"))
			elif not meis_income_account:
				frappe.throw(_("Set RODTEP Income Account in Company"))
			elif not meis_cost_center:
				frappe.throw(_("Set RODTEP Cost Center in Company"))
			else:
				meis_jv = frappe.new_doc("Journal Entry")
				meis_jv.voucher_type = "RODTEP Entry"
				meis_jv.posting_date = self.posting_date
				meis_jv.company = self.company
				meis_jv.cheque_no = self.name
				meis_jv.cheque_date = self.posting_date
				meis_jv.user_remark = "RODTEP against " + self.name + " for " + self.customer
				meis_jv.append("accounts", {
					"account": meis_receivable_account,
					"cost_center": meis_cost_center,
					"debit_in_account_currency": self.total_rodtep
				})
				meis_jv.append("accounts", {
					"account": meis_income_account,
					"cost_center": meis_cost_center,
					"credit_in_account_currency": self.total_rodtep
				})
				
				try:
					meis_jv.save(ignore_permissions=True)
					meis_jv.submit()
					
				except Exception as e:
					frappe.throw(str(e))
				else:
					self.db_set('rodtep_jv',meis_jv.name)
	def cancel_jv(self):
		if self.duty_drawback_jv:
			jv = frappe.get_doc("Journal Entry", self.duty_drawback_jv)
			jv.cancel()
			self.duty_drawback_jv = ''
		if self.get('rodtep_jv'):
			jv = frappe.get_doc("Journal Entry", self.rodtep_jv)
			jv.cancel()
			self.rodtep_jv = ''