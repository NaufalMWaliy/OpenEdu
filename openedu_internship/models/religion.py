# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeReligion(models.Model):
	_name = "oe.religion"

	name = fields.Char(string="Religion Name", required=True)