from odoo import models, fields

class UserStage(models.Model):
    _name = 'user.stage'
    _description = 'User Stage'

    name = fields.Char(string='Name', required=True)


from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    stage_id = fields.Many2one('user.stage', string='Stage')