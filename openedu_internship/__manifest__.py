# -*- coding: utf-8 -*-
{
    'name': "OpenEdu Internship",
    'summary': """Manage intership""",
    'description': """
        Open Academy module for managing trainings:
            - CV Submission
            - Company Submission
            - Result Mapping
    """,
    'author': "A4",
    'category': 'Education',
    'version': '0.1',
    'depends': ['base','openeducat_erp','openedu'],
    'data': [
        'security/oe_security.xml',
        'security/ir.model.access.csv',
        'views/internship_view.xml',
        'views/religion_view.xml',
        'views/company_submission_view.xml',
        'views/educational_history.xml',
        'views/project_experience.xml',
        'views/organization_history_view.xml',
        'views/result_mapping_view.xml',
        'views/additional_information_view.xml',
        'menu/internship_menu.xml',
    ],
    'demo': [
    ],
    'application': True,
}