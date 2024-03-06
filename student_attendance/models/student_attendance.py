from odoo import models, fields

# class EducationAttendance(models.Model):
#     _name = 'student.attendance'
#     _inherit = 'hr.attendance'
#     _description = 'Student Attendance'
#
#     student_id = fields.Many2one('education.student', string='Student', required=True, ondelete='cascade')

class StudentAttendance(models.Model):
    _name = 'student.attendance'
    _inherit = 'hr.attendance'

    partner_id = fields.Many2one(
        'res.partner',
        string='Student',
        domain=[('is_student', '=', True)],
        help="Select the student related to this attendance."
    )
    check_in = fields.Datetime(string="Check In", default=fields.Datetime.now, required=True)
    check_out = fields.Datetime(string="Check Out")
