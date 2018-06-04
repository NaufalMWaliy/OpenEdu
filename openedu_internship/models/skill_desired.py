# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeSkillDesired(models.Model):
	_name = "oe.skill.desired"

	name = fields.Char(string="Skill Name")
