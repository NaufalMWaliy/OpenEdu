# -*- coding: utf-8 -*-
from odoo import http

# class Openedu(http.Controller):
#     @http.route('/openedu/openedu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openedu/openedu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openedu.listing', {
#             'root': '/openedu/openedu',
#             'objects': http.request.env['openedu.openedu'].search([]),
#         })

#     @http.route('/openedu/openedu/objects/<model("openedu.openedu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openedu.object', {
#             'object': obj
#         })