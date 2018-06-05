# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeSeminarHistory(models.Model):
	_name = "oe.seminar.history"

	name = fields.Char(string="Seminar's Name")
	year = fields.Char(string="Year")
	role = fields.Char(string="Role")