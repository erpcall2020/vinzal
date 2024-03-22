  # -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class PartnerForm(http.Controller):

    @http.route(['/inquiry_new'], type='http', auth="public", website=True)
    def partner_form(self, **post):

        return request.render("inquiry_register.tmp_customer_form", {})
    @http.route(['/customer/form/submit'], type='http', auth="public", website=True)
    def customer_form_submit(self, **post):
        partner = request.env['inquiry.register'].sudo().create({
            'name': post.get('name'),
            'student_name': post.get('student_name'),
            'email': post.get('email'),
            'phone_number': post.get('phone_number'),
            'child_age': post.get('child_age'),
            'father_occupation': post.get('father_occupation'),
            'mother_occupation': post.get('mother_occupation'),
            'reference': post.get('reference'),
            'interested_in_class': post.get('interested_in_class'),
            'residence': post.get('residence'),
            'reference': post.get('reference'),
            'purpose': post.get('purpose'),
        })

        vals = {
            'partner': partner,
        }

        return request.render("inquiry_register.tmp_customer_form_success", vals)
