from odoo import fields, models, api


class InquiryRegister(models.Model):
    _name = 'inquiry.register'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Parent Name')
    student_name = fields.Char(string='Student Name')
    child_age = fields.Float(string='Child Age')
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    purpose = fields.Text(string='Purpose')
    father_occupation = fields.Text(string='Father Occupation')
    mother_occupation = fields.Text(string='Mother Occupation')
    residence = fields.Text(string='Area Of Residence')
    reference = fields.Text(string='Reference')
    remark = fields.Text(string='Remark')
    interested_in_class = fields.Selection([('pre_nursery', 'Pre Nursery'),
                             ('nursery', 'Nursery'),
                             ('kgi', 'KGI'),
                             ('kgii', 'KGII')],
                            string='Class',
                            track_visibility='onchange')
