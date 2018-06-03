from odoo import models,fields

class Kerjapraktek(models.Model):
	_name = 'op.kerjapraktek'
	_inherit = ['mail.thread']
	
	name = fields.Char('nama',required=True)
	course_id = fields.Many2one(
		'op.course','Course',required=True)
	subject_id = fields.Many2one(
		'op.subject', 'Subject', required=True)
	tahun_ajar =fields.Char(
		'tahun_ajar',required=True)
	start_date = fields.Date(
		'Start Date', required=True)
	end_date = fields.Date(
		'End Date', required=True)
	kerjapraktek_line = fields.One2many(
		'op.kerjapraktek.line', 'kerja_praktek_id', 'Kerjapraktek Line')
	