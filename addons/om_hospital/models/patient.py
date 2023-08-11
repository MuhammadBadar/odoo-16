from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patients Record'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name', required=True) #tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string='is_child?')
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')
    doctor_id= fields.Many2one('hospital.doctor', string='Doctor')
    tag_id=fields.Many2many('res.partner.category','hospital_patient_tag','patient_id','tag_id', string='tags')

    @api.constrains('age')
    def _check_name(self):
        for record in self:
            if not record.age:
                raise ValidationError("Age is a required field.")