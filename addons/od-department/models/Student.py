from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class student(models.Model):
    _name = 'academy.record'
    _description = 'Academy Students'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name', required=True, tracking=True)
    id = fields.Integer(string='ID', tracking=True)
    Age = fields.Integer(string='Age', tracking=True)
    Subjects = fields.Char(string='Subject', tracking=True)
    #is_child = fields.Boolean(string='is_child?', tracking=True)
    capitalized_name = fields.Char(string='capitalized_name', compute='_compute_capitalized_name', store='True')

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''

    @api.onchange('Age')
    def onchange_age(self):
        if self.Age <= 10:
            self.is_child = True
        else:
            self.is_child = False

    @api.constrains('Age', 'is_child')
    def for_validation(self):
        for rec in self:
            if rec.Age and rec.is_child == False:
                raise ValidationError(_('is_child option has to be checked'))

    @api.constrains('Age', 'is_child')
    def for_validation_age(self):
        for rec in self:
            if rec.is_child and rec.Age == 0:
                raise ValidationError(_('Age  has to be recorded'))

    @api.model_create_multi
    def create(self, value):
        for val in value:
            val['Subjects'] = 'computer science'
        return super(student, self).create(value)
