# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeEducationalHistory(models.Model):
	_name = "oe.educational.history"

	name = fields.Char(string="School")
	year = fields.Char(string="Year")

	_sql_constraints = [
		('unique_school_name',
			'unique(name)', 'School Name should be unique!, Please search first before creating new!')]