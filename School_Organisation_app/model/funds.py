from odoo import api, fields, models

class Funds(models.Model):
    _name = 'school.funds'

    _rec_name="school_name"
    school_name=fields.Many2one('school.name', string='School Name')
    fund_id = fields.Integer(string='Amount Collection',related='school_name.school_goal_amount',tracking=True)
    assign_members = fields.Char(string='Assign Member' ,related='school_name.assign_members',tracking=True)
    phot=fields.Binary('Photo',related='school_name.logo',tracking=True)
    footer_ids=fields.One2many('school.footer','name_id',string='Footer Details')

class Footer(models.Model):
    _name = 'school.footer'
    _description='Footer for all the value presentation'
 
    name_id=fields.Many2one("school.funds",string="Name of School")
    member=fields.Char(string="Assign Member",related='name_id.assign_members',tracking=True)
    fund=fields.Integer(string="Funds",related='name_id.fund_id',tracking=True)
    