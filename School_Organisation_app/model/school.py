from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import format_time
from datetime import date, datetime, timedelta, time
from time import time
import datetime
import time
import calendar
import logging

_logger=logging.getLogger(__name__)


class School(models.Model):
    _name = "school.name"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "School config Fields"


    name = fields.Char(string='Name', required=True)
    school_goal_amount = fields.Integer(string='Goal Amount',tracking=True)

    amount=fields.Integer(string="Amount Collection",default=250000)
    percentage=fields.Integer(string="Percentage of collection",compute="_value_add")    
    
    logo=fields.Binary(string="Logo")
    cover_photo=fields.Binary(string='Cover Photo',required=True)
    state=fields.Selection([
        ('update', 'No Event'),
        ('done', 'Up Coming'),
        ('normal', 'On Going'),
        ('finised', 'Finished'),
    ],compute="_check_date", inverse="_inver_check" ,tracking=True ,string="Status",store=True)
    assign_members=fields.Char(string='Assign Members')
    event = fields.Selection([
        ('run', 'Run'),
        ('read', 'Read'),
    ], default='read', string="Event")
    max_right=fields.Integer(string='Max right', default=100)
    funds_state=fields.Boolean(string="Funds Accept",compute="_fund_stat",store=True)
    #Not in used in the main fram but only to show today.
    today= fields.Date.today()
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Good'),
        ('2', 'Very Good'),
        ('3', 'Excellent')], string="Appreciation", default='0')
    event_date=fields.Date(string='Event Date')
    
    note = fields.Text(string='Description')

   



    # Declearing all the button for the  state bar 
    def action_noevent(self):
        for rec in self:  
          rec.state='update'
    def action_start(self):
        for rec in self: 
          rec.state='done'  
    def action_going(self):
        for rec in self: 
           rec.state='normal' 
    def action_finished(self):
        for rec in self: 
          rec.state='finised'
    
    def action_date(self):
        date='event_date'

    # def action_fund(self):
    #     for rec in self:
    #         rec.school_goal_amount= 


   # Giving automation  with  state bar and event date 
    @api.depends("event_date")
    def _check_date(self):
        if  self.event_date == False :
            self.state='update'
        else:
            fmt = '%Y-%m-%d'
            event_date=self.event_date
            to_day=datetime.datetime.strptime(str(self.today),"%Y-%m-%d")
            evn_date=datetime.datetime.strptime(str(event_date),"%Y-%m-%d")
           # Only to check wheater all values are working or not
            # _logger.info("<<==============================================>>")
            # _logger.info("Today date is : %s" %to_day)
            # _logger.info("Today date is : %s" %date)
            # _logger.info("<<==============================================>>")
            for rec in self:
                if to_day == evn_date:
                    rec.state='normal'
                elif to_day >  evn_date:
                    rec.state ='finised'
                elif to_day < evn_date:
                    rec.state ='done'


    @api.depends("event_date")
    def _inver_check(self):
        if  self.event_date == False:
                self.state = 'done'                 
        else:
            fmt = '%Y-%m-%d'
            event_date=self.event_date
            to_day=datetime.datetime.strptime(str(self.today),"%Y-%m-%d")
            evn_date=datetime.datetime.strptime(str(event_date),"%Y-%m-%d")
            for ram in self:
                if to_day == evn_date:                     
                       ram.state == ['normal','finised']             
                elif to_day >  evn_date:                    
                         ram.state ='finised'                                 
                elif to_day < evn_date:                   
                         ram.state == ['done','normal']
    #Finding the percentage of amount is doneted.

    @api.depends("school_goal_amount","amount")
    def _value_add(self):
        for rec in self:
            if rec.amount >0:
                rec.percentage=(rec.school_goal_amount/rec.amount)*100
    
    
   
    #Now to compute fields value in there respective value
    @api.depends("school_goal_amount")
    def _compute_field(self):
        count=0
        for r in self:
                count += r.school_goal_amount
        self.total_val=count   
    
    total_val=fields.Integer("Total value",compute="_compute_field")
    validates=fields.Integer("Validates",compute="_validate_fund")


    @api.onchange("total_val")
    def _fund_stat(self):
        for rec in self:
            if rec.total_val < rec.amount:
                rec.funds_state=True
            else:
                rec.funds_state=False


    @api.constrains('school_goal_amount')
    def _validate_fund(self):
        val=self.total_val
        equ=0
        for f in self:
            if val > f.amount:
                equ= val- f.amount
                f.school_goal_amount = equ
                _logger.info("<<==============================================>>")
                _logger.info("1ST date is : %s" %equ)
                _logger.info("2ND date is : %s" %f.total_val)
                _logger.info("3RD date is : %s" %f.school_goal_amount)
                
                
                return {
                        'name'      : ('Fund Validation Wizard'),
                        'type'      : 'ir.actions.act_window',
                        'res_model' : 'school.fund.wizard',
                        'view_id'   : 'fund_valid_wizard',
                        'view_type' : 'form',
                        'view_mode' : 'form',
                        'target'    : 'new'
                       }

                # raise ValidationError ("Ok we have not done yet")
            
                