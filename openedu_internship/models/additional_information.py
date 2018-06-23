# -*- coding: utf-8 -*-

from odoo import models, fields, api

SKILL_VALUE = fields.Selection([
	('deficient', 'Deficient'),
	('fair', 'Fair'),
	('good', 'Good'),
	('very_good','Very Good'),
])

class OeProgramming(models.Model):
	_name = "oe.additional.information.progamming"

	progamming = fields.Selection([
		('desktop_lang', 'Desktop Language'),
		('web_lang', 'Web Programming Language'),
		('framework', 'Framework'),
		('database_lang', 'Database'),
	], 'Type')
	name = fields.Char(string='Name')
	skill = fields.Selection(SKILL_VALUE, 'Skill')

class OeSoftwareEnginering(models.Model):
	_name = "oe.additional.information.software.enginering"

	software_enginering = fields.Selection([
		('medelling_tools', 'Modelling Tools'),
		('modelling_tools_app', 'Modelling Tools Applicatio'),
	], 'Software Enginering')
	name = fields.Char(string="Name")
	skill = fields.Selection(SKILL_VALUE, 'Skill')

class OeInfrastructur(models.Model):
	_name = "oe.additional.information.infrastructure"

	infrastructure = fields.Selection([
		('administration', 'Administration'),
		('virtualization', 'Virtualization'),
	], 'Infrastructure')
	name = fields.Char(string="Name")
	skill = fields.Selection(SKILL_VALUE, 'Skill')

class OeEtc(models.Model):
	_name = "oe.additional.information.etc"

	etc = fields.Selection([
		('office_tools', 'Office Tools'),
		('ide', 'IDE'),
		('graphics_design', 'Graphics Design'),
	], 'Etc')
	name = fields.Char(string="Name")
	skill = fields.Selection(SKILL_VALUE, 'Skill')

class OeCommunication(models.Model):
	_name = "oe.additional.information.communication"

	name = fields.Many2one('oe.language', string="Language", ondelete="restrict")
	reading_skill = fields.Selection(SKILL_VALUE, 'Reading Skill')
	speaking_skill = fields.Selection(SKILL_VALUE, 'Speaking Skill')
	listening_skill = fields.Selection(SKILL_VALUE, 'Listening Skill')
	writing_skill = fields.Selection(SKILL_VALUE, 'Writing Skill')