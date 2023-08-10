from odoo import api, models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patients Record'
    #_inherit = 'mail.thread'

    name = fields.Char(string='Name', required=True) #tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string='is_child?')
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')
    doctor_id= fields.Many2one('hospital.doctor', string='Doctor')