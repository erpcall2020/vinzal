

from odoo import fields, models
from datetime import date, datetime


class VisitorsRegister(models.Model):
    _name = 'visitors.register'

    name = fields.Char(string='Name', required=True, help="Name of the visitors")
    phone = fields.Char(string='Phone')
    purpose = fields.Text(string='Purpose')
    address = fields.Text(string='Address')
    check_out_time = fields.Datetime(string='Check Out Time')


