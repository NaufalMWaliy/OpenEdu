from odoo import models,fields,api
from datetime import datetime

class CompanySubmission(models.Model):
	_name = 'openedu.company'
	_rec_name = "company_name"

	proposer_ids = fields.Many2many("op.student", string="Proposer")
	date = fields.Date('Date', required=True)
	day_name = fields.Char(compute="_get_day_name", string="Day", store=True, index=True)
	company_name = fields.Char('Company Name',required=True)
	address = fields.Char('Address',required=True)
	name_contact_person = fields.Char('Name Contact Person',required=True)
	email = fields.Char('Email')
	official_website = fields.Char('Official Website')
	numberofemployee = fields.Char('Number Of Employee')
	standingcompany = fields.Char('Standing Company')
	phone_number=fields.Char('Phone Number',required=True)
	contact_person = fields.Char('Contact Person',required=True)
	company_adventage=fields.Text('Company Adventage')
	mechanism_internship=fields.Text('Mechanism Internship')
	company_criteria=fields.Text('Company Criteria')
	implementation_technology=fields.Text('Implementation Technology',required=True)
	isApproved = fields.Boolean(default=False)
	state = fields.Selection([
		('draft', 'Draft'),
		('approve', 'Approved'),
	], 'state', readonly=True, default='draft', track_visibility='onchange')

	@api.depends("date")
	def _get_day_name(self):
		for data in self:
			if data.date:
				now = data.date
				day = datetime.strptime(now, "%Y-%m-%d")
				data.day_name = day.strftime("%A")

	def act_approve(self):
		self.isApproved = True
		self.state = 'approve'
		return True