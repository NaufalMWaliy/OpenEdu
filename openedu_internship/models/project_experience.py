# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeProjectExperience(models.Model):
	_name = "oe.project.experience"

	name = fields.Char(string="Task Name", required=True)
	student_id = fields.Many2one("op.student", string="Student", required=True)
	description = fields.Text(string="Description")
	tech_and_tools = fields.Char(string="Technology and Tools")
	position = fields.Char(string="Position in Team", required=True)
	achievement = fields.Text(string="Achievement")
	learning_outcome = fields.Text(string="Learning Outcomes")
	start_date = fields.Date(string="Start Date", required=True)
	end_date = fields.Date(string="End Date", required=True)
