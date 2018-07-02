# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeResultMapping(models.Model):
	_name = "oe.result.mapping"
	_rec_name = "name"

	student_id = fields.Many2one("op.student", "Student", required=True, ondelete="cascade")
	nim = fields.Char(related="student_id.gr_no", store=True)
	company_id = fields.Many2one("openedu.company", "Company", required=True, index=True, domain="[('isApproved','=',True)]")
	name = fields.Char(related="student_id.name", store=True)

