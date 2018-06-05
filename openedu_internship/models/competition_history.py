# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeCompetitionHistory(models.Model):
	_name = "oe.competition.history"

	name = fields.Char(string="Competition's Name")
	year = fields.Char(string="Year")
	achievement = fields.Char(string="Achievement")