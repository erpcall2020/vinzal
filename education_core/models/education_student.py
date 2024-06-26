from odoo import fields, models, api, _


class EducationStudent(models.Model):
    _name = 'education.student'
    _inherit = ['mail.thread']
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Student record'
    _rec_name = 'name'

    def student_documents(self):
        """Return the documents student submitted
        along with the admission application"""
        self.ensure_one()
        if self.application_id.id:
            documents = self.env['education.documents'].search(
                [('application_ref', '=', self.application_id.id)])
            documents_list = documents.mapped('id')
            return {
                'domain': [('id', 'in', documents_list)],
                'name': _('Documents'),
                'view_mode': 'tree,form',
                'res_model': 'education.documents',
                'view_id': False,
                'context': {'default_application_ref': self.application_id.id},
                'type': 'ir.actions.act_window'
            }

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if name:
            recs = self.search(
                [('name', operator, name)] + (args or []), limit=limit)
            if not recs:
                recs = self.search(
                    [('ad_no', operator, name)] + (args or []), limit=limit)
            return recs.name_get()
        return super(EducationStudent, self).name_search(
            name, args=args, operator=operator, limit=limit)

    @api.model
    def create(self, vals):
        """Over riding the create method to assign
        sequence for the newly creating the record"""
        vals['ad_no'] = self.env['ir.sequence'].next_by_code(
            'education.student')
        res = super(EducationStudent, self).create(vals)
        return res

    # create invoice header action method
    def action_create_invoice(self, rec=None):
        invoice: object = self.env['account.move'].create({
            'partner_id': self.student_user_id.partner_id.id,
            'move_type': 'out_invoice',
            'invoice_date': fields.Date.today(),
        })
        # You can also perform other actions related to the invoice creation here
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'account.move',
            'res_id': invoice.id,
            'target': 'current',
        }

    def action_send_email(self):
        template = self.env.ref('education_core.student_mail_template')
        ctx = {
            'default_model': self._name,
            'default_res_id': self.id,
            'default_use_template': bool(template),
            'default_template_id': template.id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'force_email': True,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'target': 'new',
            'context': ctx,
        }


    # Here we are going to write action for view of total invoice
    def action_view_partner_invoices(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoice',
            'res_model': 'account.move',
            'domain': [
                ('partner_id', '=', self.student_user_id.partner_id.id),
                ('move_type', 'in', ('out_invoice', 'out_refund'))
            ],
            'view_mode': 'tree,form',
            'target': 'current',
        }

    partner_id = fields.Many2one(
        'res.partner', string='Partner', required=True, ondelete="cascade")
    # middle_name = fields.Char(string='Middle Name')
    # last_name = fields.Char(string='Last Name')
    application_no = fields.Char(string="Application No")
    date_of_birth = fields.Date(string="Date of Birth", requird=True)
    guardian_name = fields.Many2one('res.partner', string="Guardian",
                                    domain=[('is_parent', '=', True)])
    father_name = fields.Char(string="Father")
    mother_name = fields.Char(string="Mother")
    class_id = fields.Many2one('education.class.division', string="Class")
    admission_class = fields.Many2one('education.class',
                                      string="Admission Class")
    ad_no = fields.Char(string="Admission Number", readonly=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')],
                              string='Gender', required=True, default='male',
                              track_visibility='onchange')
    blood_group = fields.Selection([('a+', 'A+'),
                                    ('a-', 'A-'),
                                    ('b+', 'B+'),
                                    ('o+', 'O+'),
                                    ('o-', 'O-'),
                                    ('ab-', 'AB-'),
                                    ('ab+', 'AB+')],
                                   string='Blood Group', required=True,
                                   default='a+', track_visibility='onchange')
    company_id = fields.Many2one('res.company', string='Company')
    per_street = fields.Char()
    per_street2 = fields.Char()
    per_zip = fields.Char(change_default=True)
    per_city = fields.Char()
    per_state_id = fields.Many2one("res.country.state", string='State',
                                   ondelete='restrict')
    per_country_id = fields.Many2one('res.country', string='Country',
                                     ondelete='restrict')
    medium = fields.Many2one('education.medium', string="Medium", )
    sec_lang = fields.Many2one('education.subject', string="Second language",
                               required=True,
                               domain=[('is_language', '=', True)])
    mother_tongue = fields.Many2one('education.mother.tongue',
                                    string="Mother Tongue", required=True,
                                    domain=[('is_language', '=', True)])
    caste_id = fields.Many2one('religion.caste', string="Caste")
    religion_id = fields.Many2one('religion.religion', string="Religion")
    is_same_address = fields.Boolean(string="Is same Address?")
    nationality = fields.Many2one('res.country', string='Nationality',
                                  ondelete='restrict')
    application_id = fields.Many2one('education.application',
                                     string="Application No")
    class_history_ids = fields.One2many('education.class.history', 'student_id',
                                        string="Application No")
    father_image = fields.Binary()

    _sql_constraints = [
        ('ad_no', 'unique(ad_no)',
         "Another Student already exists with this admission number!"),
    ]
