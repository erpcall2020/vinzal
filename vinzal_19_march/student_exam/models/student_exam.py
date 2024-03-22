import datetime

from odoo import models, fields, api, _


class OpExam(models.Model):
    _name = "op.exam"
    _description = "Exam"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = 'partner_id'

    #  partner_id = fields.Many2one('education.student', string='Student')
    #  date_of_birth = fields.Date(related='partner_id.date_of_birth', string='Date of Birth', store=True)

    start_time = fields.Datetime(string='Start Time', required=True)
    end_time = fields.Datetime(string='End Time', required=True)
    note = fields.Text(string='Remarks')
    attaudence = fields.Char(string='Attaudence')
    total_marks = fields.Integer(string='Total Marks', required=True)
    #  min_marks = fields.Integer(string='Passing Marks', required=True)
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one(
        'res.partner',
        string='Student',
        domain=[('is_student', '=', True)],
        help="Select the student related to this attendance.")
    student_class = fields.Many2one(
        'education.class',
        string="Exam",
        help="Select the Class to which the students applied")
    # date_of_birth = fields.Date(related='partner_id.date_of_birth', string='Date of Birth', store=True)
    partner_phone_number = fields.Char(related='partner_id.mobile', string='Phone Number', readonly=True)
    partner_address = fields.Char(related='partner_id.street', string='Address', readonly=True)
    #  partner_guardian_name = fields.Char(related='partner_id.guardian_name', string='Father Name', readonly=True)
    subject_id = fields.Many2one('education.subject', string='Subject')
    marks_obtained = fields.Char(string="Marks Obtained")
    grade = fields.Char(string="Grade")
    exam_line_ids = fields.One2many('op.exam.line', 'exam_id', string='Exam Lines')
    personality_line_ids = fields.One2many('op.person.line', 'personality_id', string='Personality Development')

    @api.constrains('start_time', 'end_time')
    def _check_start_end_time(self):
        for rec in self:
            if rec.start_time >= rec.end_time:
                raise ValidationError(_("End Time must be after Start Time"))


class OpExamLine(models.Model):
    _name = 'op.exam.line'
    _description = 'Exam Line'

    exam_id = fields.Many2one('op.exam', string='Exam')
    subject_id = fields.Many2one('education.subject', string='Subject')
    marks_obtained = fields.Float(string='Marks Obtained')
    # grade = fields.Char(string='Grade')
    grade = fields.Selection([('a', 'A'),
                              ('b', 'B'),
                              ('c', 'C'), ('d', 'D'),
                              ('e', 'E')],
                             string='Grade',
                             track_visibility='onchange')
    min_marks = fields.Integer(string='Passing Marks', required=True)

    class OpPersonalityExamLine(models.Model):
        _name = 'op.person.line'
        _description = 'Exam Line'

        personality_id = fields.Many2one('op.exam', string='Personality development')
        grade = fields.Selection([('a', 'A'),
                                  ('b', 'B'),
                                  ('c', 'C'), ('d', 'D'),
                                  ('e', 'E')],
                                 string='Grade',
                                 track_visibility='onchange')
        points1 = fields.Selection([
            ('courteousness', 'Courteousness'),
            ('confidence', 'Confidence'),
            ('enthusiastic', 'Enthusiastic'),
            ('discipline', 'Discipline'),
            ('leadership', 'Leadership'),
            ('regularity', 'Regularity'),
        ], string='Points 1', track_visibility='onchange')

        points2 = fields.Selection([
            ('attentive', 'Attentive'),
            ('cleanliness', 'Cleanliness'),
            ('punctuality', 'Punctuality'),
            ('neatness_in_work', 'Neatness in Work'),
            ('a_hentine', 'A Hentine'),
            ('cooperative', 'Cooperative'),
        ], string='Points 2', track_visibility='onchange')
