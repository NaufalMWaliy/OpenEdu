# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Classroom(models.Model):
	_inherit = "op.classroom"

	student_class_id = fields.Many2one("oe.student.class")