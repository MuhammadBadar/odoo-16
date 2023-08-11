from odoo import api, models, fields


class HospitalNurse(models.Model):
    _name = 'hospital.nurse'
    _description = 'Nurses records'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name', required=True) #tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')
    patient_id=fields.Many2one('hospital.patient',string='Pateint')