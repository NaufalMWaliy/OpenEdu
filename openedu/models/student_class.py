# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StudentClass(models.Model):
	_name = "oe.student.class"
	
	name = fields.Char("Class Name", required=True)
	class_of = fields.Char("Class of", required=True)
	no_of_person = fields.Integer("Number of person", compute="_no_of_person", readonly=True)

	student_ids = fields.One2many("op.student", "class_id", string="Student")
	classroom_id = fields.Many2one("op.classroom", string="Classroom")
	capacity = fields.Integer(related="classroom_id.capacity", string="Classroom Capacity", readonly=True)

	@api.depends("student_ids")
	def _no_of_person(self):
		for r in self:
			r.no_of_person = len(r.student_ids)

	@api.onchange("no_of_person","classroom_id.capacity")
	def _verify_value_students(self):
		if self.no_of_person > self.classroom_id.capacity:
			return {
				'warning': {
					'title': "To Many Student",
					'message': "Please increase room capacity or move excess student"
				}
			}

	# @api.onchange("classroom_id")
	# def onchange_classroom_id(self, cr, uid, ids, classroom, context=None):
	# 	self.pool.get("op.classroom").write(cr, uid, [classroom], {"student_class_id": ids[0]})
	# 	return True

