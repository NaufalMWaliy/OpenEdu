# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeEducationalHistory(models.Model):
	_name = "oe.educational.history"

	name = fields.Char(string="School")
	year_in = fields.Char(string="Year In")
	year_out = fields.Char(string="Year Out")