# -*- coding: utf-8 -*-
###############################################################################
#    A part of Educational ERP Project <https://www.educationalerp.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2020-TODAY Cybrosys Technologies (<https://www.cybrosys.com>)
#    Author: Hajaj Roshan (hajaj@cybrosys.in)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class EducationSubject(models.Model):
    _name = 'education.subject'

    name = fields.Char(string='Name', required=True, help="Name of the Subject")
    is_language = fields.Boolean(string="Language",
                                 help="Tick if this subject is a language")
    is_lab = fields.Boolean(string="Lab", help="Tick if this subject is a Lab")
    code = fields.Char(string="Code", help="Enter the Subject Code")
    type = fields.Selection(
        [('compulsory', 'Compulsory'), ('elective', 'Elective')],
        string='Type', default="compulsory",
        help="Choose the type of the subject")
    weightage = fields.Float(string='Weightage', default=1.0,
                             help="Enter the weightage for this subject")
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('code', 'unique(code)',
         "Another Subject already exists with this code!"),
    ]

    @api.constrains('weightage')
    def check_weightage(self):
        """return warning if the weightage given is not a possitive value"""
        for rec in self:
            if rec.weightage <= 0:
                raise ValidationError(_('Weightage must be Possitive'))


class StandardMedium(models.Model):
    _name = "education.medium"
    _description = "Standard Medium"

    name = fields.Char(string='Name', required=True,
                       help="Enter the Name of the Medium")
    code = fields.Char(string='Code', help="Enter the Medium Code")
    description = fields.Text(string='Description')


class EducationMotherTongue(models.Model):
    _name = "education.mother.tongue"
    _description = "Mother Tongue Language"

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code')


class EducationSyllabus(models.Model):
    _name = 'education.syllabus'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name', required=True)
    class_id = fields.Many2one('education.class', string='Class')
    subject_id = fields.Many2one('education.subject', string='Subject')
    total_hours = fields.Float(string='Total Hours')
    oral_description = fields.Text(string='Oral Activities')
    written_description = fields.Text(string='Written Activities')
    description = fields.Text(string='Activities')
    month = fields.Selection([('january', 'January'),
                                      ('february', 'February'),
                                        ('march', 'March'),
                                        ('afril', 'April'),
                              ('march', 'March'),
                              ('april', 'April'),('may', 'May'), ('june', 'June'), ('july', 'July'),
                              ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'),
                              ('december', 'December')],
                             string='Month',
                             track_visibility='onchange')
    week = fields.Selection([('week1', 'Week 1'),
                              ('week2', 'Week 2'),
                              ('week3', 'Week 3'),
                              ('week4', 'Week 4')],
                             string='Week',
                             track_visibility='onchange')
    day = fields.Selection([('monday', 'Monday'),
                             ('tuesday', 'Tuesday'),
                             ('wednesday', 'Wednesday'),
                             ('thursday', 'Thursday'),
                             ('friday', 'Friday'),
                             ('saturday', 'Saturday')],
                            string='Day',
                            track_visibility='onchange')
    period = fields.Selection([('1st', '1st'),
                             ('2nd', '2nd'),
                             ('3rd', '3rd'),
                             ('4th', '4th'),
                             ('5th', '5th'),
                             ('6th', '6th')],
                            string='Period',
                            track_visibility='onchange')
    time = fields.Selection([('10:00 to 10:15', '10:00 TO 10:15'),
                             ('10:15 to 10:30', '10:15 TO 10:30'),
                             ('10:30 to 11:00', '10:30 TO 11:00'),
                             ('11:00 to 11:30', '11:00 TO 11:30'),
                             ('11:30 to 12:00', '11:30 TO 12:00'),
                             ('12:00 to 12:30', '12:00 TO 12:30'),
                             ('12:30 to 1:00', '12:30 TO 1:00')],
                            string='Time',
                            track_visibility='onchange')
   # # type = fields.Selection([('oral', 'Oral'),
   #                           ('written', 'Written')],
   #                          string='Type',
   #                          track_visibility='onchange')

    state = fields.Selection([('planned', 'Planned'), ('going_on', 'Going-on'), ('done', 'Done')],
                             string='State', required=True, default='planned',)
    assignee_id = fields.Many2one('education.faculty', string='Assignee')
    assign_date = fields.Date(string="Assign Date")

    @api.constrains('total_hours')
    def validate_time(self):
        """returns validation error if the hours is not a possitive value"""
        for rec in self:
            if rec.total_hours <= 0:
                raise ValidationError(_('Hours must be greater than Zero'))
