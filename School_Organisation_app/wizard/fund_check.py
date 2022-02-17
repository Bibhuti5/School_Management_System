from odoo import models, fields
import logging

_logger=logging.getLogger(__name__)

class confirm_wizard(models.TransientModel):
    _name = 'school.fund.wizard'
    _description = "Funds Validate for use"
    
    event_name = fields.Many2one("school.name",string='School Name', required=True)
    amount=fields.Integer("Amount",related="event_name.school_goal_amount",tracking=True)
    yes_no =fields.Char(default="Are you sure to donote all the amount")
    total_val=fields.Integer('Total Amount',related='event_name.total_val',tracking=True)
    


    def yes(self):
        count=0
        for r in self: 
            _logger.info("<<==============================================>>")
            _logger.info("Amount date is : %s" %r.amount)       
            count += r.amount        
        self.total_val=count
        _logger.info("<<==============================================>>")
        _logger.info("NEW amount  is : %s" %self.total_val)
      
            
