# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeSkillDesired(models.Model):
	_name = "oe.skill.desired"

	name = fields.Char(string="Skill Name")

	_sql_constraints = [
		('unique_skill_name',
			'unique(name)', 'Skill Name should be unique!, Please search first before creating new!')]