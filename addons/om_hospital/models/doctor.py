from odoo import api, models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor records'
    #_inherit = 'mail.thread'

    name = fields.Char(string='Name', required=True) #tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    reference = fields.Char(string='Reference')
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')