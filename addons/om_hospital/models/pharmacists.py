from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class HospitalPharmacists(models.Model):
    _name = 'hospital.pharmacists'
    _description = 'Pharmacists Record'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name', required=True) #tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')
