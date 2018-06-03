# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeCV(models.Model):
	_name = "oe.cv"
	_inherits = {'op.student': 'student_id'}

	student_id = fields.Many2one("op.student", "Student", required=True, ondelete="cascade")
	full_name = fields.Char(string="Name")
	display_full_name = fields.Char(compute="_compute_full_name", store=True, index=True)
	short_name = fields.Char(string="Short Name")

	@api.depends("student_id")
	def _compute_full_name(self):
		str_name = ""
		for student in self:
			if student.name:
				str_name = str_name + student.name
			if student.middle_name:
				str_name = str_name + " " + student.middle_name
			if student.last_name:
				str_name = str_name + " " + student.last_name
			student.display_full_name = str_name

	@api.onchange("display_full_name")
	def set_full_name(self):
		self.full_name = self.display_full_name