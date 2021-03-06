# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeProjectExperience(models.Model):
	_name = "oe.project.experience"

	name = fields.Char(string="Task Name", required=True)
	subject_id = fields.Many2one("op.subject", string="Subject", required=True)
	subject_name = fields.Char(related="subject_id.name", string="Subject", store=True)
	description = fields.Text(string="Description")
	start_date = fields.Date(string="Start Date", required=True)
	end_date = fields.Date(string="End Date", required=True)
	tech_and_tools = fields.Char(string="Technology and Tools")
	position = fields.Char(string="Position in Team", required=True)
	achievement = fields.Text(string="Achievement")
	learning_outcome = fields.Text(string="Learning Outcomes")
	cv_id = fields.Many2one("oe.cv", string="Curriculum Vitae", ondelete="set null")

	_sql_constraints = [
		('unique_task_name',
			'unique(name)', 'Task Name should be unique!, Please search first before creating new!')]