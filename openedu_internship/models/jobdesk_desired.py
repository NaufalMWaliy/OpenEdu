# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeJobdeskDesired(models.Model):
	_name = "oe.jobdesk.desired"

	name = fields.Char(string="Jobdesk Name")

	_sql_constraints = [
		('unique_jobdesk_name',
			'unique(name)', 'Jobdesk Name should be unique!, Please search first before creating new!')]
