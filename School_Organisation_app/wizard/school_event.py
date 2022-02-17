from odoo import models, fields


class School_events_wiz(models.TransientModel):
    _name = "school.event.wizard"
    _description = "Create School Event Wizard"

    event_name = fields.Many2one("school.name",string='School Name', required=True)
    appointment_date = fields.Date(string="Event Date",related="event_name.event_date",tracking=True)

    def delete_event(self):
        for rec in self:
            rec.event_name.unlink()

    def get_data(self):
        name = self.env['school.name'].search([])
        for rec in name:
            print("School Name", rec.name)

        return{
            "type": "ir.actions.do_nothing"
        }

    
