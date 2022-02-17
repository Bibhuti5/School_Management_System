from odoo import api, models

class InvoiceCardReport(models.AbstractModel):
    _name = 'report.school.report_invoice_details'
    _description = 'Invoice  Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['school.invoice'].browse(docids[0])
        appointments = self.env['school.invoice'].search([('amount', '=', docids[0])])
        amount_lis = []
        return {
            'doc_model': 'school.invoice',
            'docs': docs,
            'amount_list': amount_list,
        }
