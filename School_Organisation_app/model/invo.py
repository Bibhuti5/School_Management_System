from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Invoice(models.Model):
    _name = 'school.invoice'
    _description="School Invoice Description"
    
    _rec_name="school_name"
    school_name=fields.Many2one('school.name', string='School Name')
    date=fields.Date("Invoice Date")
    address=fields.Text("Address",store=True)
    mail=fields.Char("Mail Address")
    phone=fields.Char("Phone" )

    fund_id = fields.Integer(string='Fund Collection',related='school_name.school_goal_amount',tracking=True)
    logo=fields.Binary('School Logo',related='school_name.logo',tracking=True)
    note=fields.Text('Description',related='school_name.note',tracking=True)
    invoice_footer=fields.One2many('invoice.footer','name_footer',string='Invoice Footer Details')
   
   
    def preview_action(self):
        return self.env.ref('school_event.invoice_details').report_action(self,config=False)


class Invoice_Footer(models.Model):
    _name = 'invoice.footer'
    _description='Invoice value'
    
    _rec_name="name_footer"
    name_footer=fields.Many2one("school.invoice",string="Name of School")
    des=fields.Text(string="Description",related='name_footer.note',tracking=True)
    fund=fields.Integer(string="Fund Collected")
    quantity=fields.Float("Qantity")
    logo=fields.Binary(string="Logo",related='name_footer.logo',tracking=True)
    amount=fields.Integer("Amount",compute="_amount")

    @api.onchange("fund")
    def _amount(self):
        for rec in self:
            rec.amount=rec.fund 
