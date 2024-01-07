from odoo import fields, models


class InquiryRegister(models.Model):
    _name = 'inquiry.register'

    name = fields.Char(string='Parent Name')
    student_name = fields.Char(string='Student Name')
    child_age = fields.Integer(string='Child Age')
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    purpose = fields.Text(string='Purpose')