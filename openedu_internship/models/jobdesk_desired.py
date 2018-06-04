# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OeJobdeskDesired(models.Model):
	_name = "oe.jobdesk.desired"

	name = fields.Char(string="Jobdesk Name")
