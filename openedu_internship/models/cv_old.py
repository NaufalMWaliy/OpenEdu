# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeCV(models.Model):
	_name = "oe.cv"
	_inherits = {'op.student': 'student_id'}
	_rec_name = "full_name"

	student_id = fields.Many2one("op.student", "Student", required=True, ondelete="cascade")
	full_name = fields.Char(string="Name")
	display_full_name = fields.Char(compute="_compute_full_name", store=True, index=True)
	nick_name = fields.Char(string="Nickname")
	religion = fields.Selection([
		('islam', 'Islam'),
		('christian','Christian'),
		('catholic','Catholic'),
		('hindu', 'Hindu'),
		('buddha', 'Buddha')
	], "Religion")
	birth_country = fields.Many2one('res.country', string='Birth Country', ondelete='restrict')
	birth_city = fields.Char("Birth City")
	marital_status = fields.Selection([
		('single', 'Single')
	])
	state = fields.Selection([
		('draft', 'Draft'),
		('submit', 'Submitted'),
		('approve', 'Approved'),
	], 'State', readonly=True, default='draft', track_visibility='onchange')
	jobdesk_desired_id = fields.Many2many("oe.jobdesk.desired", string="Jobdesk Desired")
	skill_desired_id = fields.Many2many("oe.skill.desired")
	educational_history_id = fields.Many2many("oe.educational.history", string="Educational History")
	subject_id = fields.Many2many("op.subject", string="Subject")
	project_experience_ids = fields.One2many("oe.project.experience", "cv_id",string="Project Experience")
	organization_history_id = fields.Many2many("oe.organization.history", string="Organization History")
	seminar_history_id = fields.Many2many("oe.seminar.history", string="Seminar")
	competition_history_id = fields.Many2many("oe.competition.history", string="Competition")
	adt_info_programming_id = fields.One2many("oe.additional.information.programming", "cv_id", string="Programming")
	adt_info_software_enginering_id = fields.One2many("oe.additional.information.software.enginering", "cv_id", string="Software Enginering")
	adt_info_infrastructure_id = fields.One2many("oe.additional.information.infrastructure", "cv_id", string="Infrastructure")
	adt_info_etc_id = fields.One2many("oe.additional.information.etc", "cv_id", string="Etc")
	adt_info_communtication_id = fields.One2many("oe.additional.information.communication", "cv_id", string="Communication")
	is_approved = fields.Boolean(default=False)

	@api.depends("student_id")
	def _compute_full_name(self):
		str_name = ""
		for student in self:
			if student.name:
				str_name = str_name + student.name
			if student.middle_name:
				str_name = str_name + " " + student.middle_name
			if student.last_name:
				str_name = str_name + " " + student.last_name
			student.display_full_name = str_name

	@api.onchange("display_full_name")
	def set_full_name(self):
		self.full_name = self.display_full_name

	@api.multi
	def act_submit(self):
		self.state = 'submit'
		return True

	@api.multi
	def act_draft(self):
		self.state = 'draft'
		return True

	@api.multi
	def act_approve(self):
		self.state = 'approve'
		return True