# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeOrganizationHistory(models.Model):
	_name = "oe.organization.history"

	name = fields.Char(string="Information")
	year = fields.Char(string="Year")

	_sql_constraints = [
		('unique_organization_name',
			'unique(name)', 'Organizationl Name should be unique!, Please search first before creating new!')]