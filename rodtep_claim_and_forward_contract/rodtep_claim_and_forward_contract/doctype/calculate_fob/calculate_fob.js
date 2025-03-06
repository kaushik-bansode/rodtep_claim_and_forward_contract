// Copyright (c) 2025, sf and contributors
// For license information, please see license.txt
let currency = null
function calculate_total_fob_value(frm, cdt, cdn){
	let d=locals[cdt][cdn]
	if(currency=='INR'){
        d.fob_value = d.base_amount-(d.insurance+d.freight)
        d.fob_value_inr = d.base_amount-(d.insurance+d.freight)
        console.log(d.fob_value_inr,d.base_amount,d.insurance,d.freight)
        d.duty_drawback_amount = d.fob_value_inr*d.duty_drawback_rate/100
        d.rodtep_value = d.fob_value_inr*d.rodtep_rate/100
	}
	else{
        d.fob_value = d.amount-(d.insurance+d.freight)
        d.fob_value_inr = d.base_amount-(d.freight*frm.doc.conversion_rate+frm.doc.conversion_rate*d.insurance)
        d.duty_drawback_amount = d.fob_value_inr*d.duty_drawback_rate/100
        d.rodtep_value = d.fob_value_inr*d.rodtep_rate/100
		
    }
    frm.refresh_fields()

}

frappe.ui.form.on("Calculate FOB", {
    onload: frm => {
        currency = frm.doc.currency
    },
    sales_invoice: frm => {
        frm.clear_table("sales_invoice_items")
        if(frm.doc.sales_invoice){
            frm.call({
                method:"update_sales_invoice",
                doc:frm.doc
            })
        }
        currency = frm.doc.currency
    },
    before_save:async frm => {
        frm.doc.sales_invoice_items.forEach(row => {
            frm.doc.total_fob_value += row.fob_value
            frm.doc.total_duty_drawback += row.duty_drawback_rate
            frm.doc.insurance += row.insurance
            frm.doc.freight += row.freight
            frm.doc.total_rodtep += row.rodtep_value
        })
    }
    });

frappe.ui.form.on("Calculate FOB Details", {
    freight:function(frm,cdt,cdn){            	
        calculate_total_fob_value(frm, cdt, cdn)
     },
     insurance:function(frm,cdt,cdn){
        calculate_total_fob_value(frm, cdt, cdn)
     },
     duty_drawback_rate:function(frm,cdt,cdn){
        calculate_total_fob_value(frm, cdt, cdn)
     },
     rodtep_rate:function(frm,cdt,cdn){
        calculate_total_fob_value(frm, cdt, cdn)
     },
});
