# -*- coding: utf-8 -*-
from odoo import http

# class OpeneduInternship(http.Controller):
#     @http.route('/openedu_internship/openedu_internship/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openedu_internship/openedu_internship/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openedu_internship.listing', {
#             'root': '/openedu_internship/openedu_internship',
#             'objects': http.request.env['openedu_internship.openedu_internship'].search([]),
#         })

#     @http.route('/openedu_internship/openedu_internship/objects/<model("openedu_internship.openedu_internship"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openedu_internship.object', {
#             'object': obj
#         })