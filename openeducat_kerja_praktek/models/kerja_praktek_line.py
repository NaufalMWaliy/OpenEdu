from odoo import models,fields

class Kerjapraktek(models.Model):
	_name = 'op.kerjapraktek.line'
	_inherit = ['mail.thread']
	_rec_name = 'kerja_praktek_id'
	
	student_id = fields.Many2one(
		'op.student','Student',required=True)
	cv = fields.Char(
		'cv')
	pengajuan_perusahaan = fields.Char(
		'pengajuan_perusahaan')
	kerja_praktek_id = fields.Many2one(
		'op.kerjapraktek', 'Kerja Praktek', required=True)