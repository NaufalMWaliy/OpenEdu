from odoo import models,fields,api

class CompanySubmission(models.Model):
	_name = 'openedu.company'
	_description = 'model form company submission'
	
	nama = fields.Many2one('op.student','Students',required=True)
	date = fields.Date('Date', required=True)
	company_name = fields.Char('Company Name',required=True)
	address = fields.Char('Address',required=True)
	name_contact_person = fields.Char('Name Contact Person',required=True)
	email = fields.Char('Email',required=True)
	official_website = fields.Char('Official Website')
	numberofemployee = fields.Char('Number Of Employee')
	standingcompany = fields.Char('Standing Company')
	phone_number=fields.Char('Phone Number',required=True)
	contact_person = fields.Char('Contact Person',required=True)
	company_adventage=fields.Text('Company Adventage',required=True)
	mechanism_internship=fields.Text('Mechanism Internship',required=True)
	company_criteria=fields.Text('Company Criteria',required=True)
	implementation_technology=fields.Text('Implementation Technology',required=True)