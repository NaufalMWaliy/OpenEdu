# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
	_inherit = "op.student"

	class_id = fields.Many2one("oe.student.class", ondelete="set null", string="Class", readonly=True)
	class_of_id = fields.Char(related="class_id.class_of", store=True, readonly=True)