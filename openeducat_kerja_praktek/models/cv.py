
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class OpCV(models.Model):
	_name = 'op.curriculum'
	_inherits = {'res.partner': 'partner_id'}
	
	name = fields.Char('Nama Lengkap',required=True)
	nama_panggilan = fields.Char('Nama Panggilan', required=True)
	birth_date = fields.Date('Tanggal Lahir')
	gender = fields.Selection(
        [('m', 'Laki - Laki'), ('f', 'Perempuan')], 'Jenis Kelamin')
	nationality = fields.Many2one('res.country', 'Kewarganegaraan')
	contact = fields.Char('No. Telepon/HP')
	
	@api.multi
	@api.constrains('birth_date')
	def _check_birthdate(self):
		for record in self:
			if record.birth_date > fields.Date.today():
				raise ValidationError(_("Birth Date can't be greater than current date!"))
