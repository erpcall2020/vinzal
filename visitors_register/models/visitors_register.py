

from odoo import fields, models
from datetime import date, datetime


class VisitorsRegister(models.Model):
    _name = 'visitors.register'

    name = fields.Char(string='Name', required=True, help="Name of the visitors")
    phone = fields.Char(string='Phone', required=True)
    purpose = fields.Text(string='Purpose' , required=True)
    address = fields.Text(string='Address')
    check_out_time = fields.Datetime(string='Check Out Time', required=True)


