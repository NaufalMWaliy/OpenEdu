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
    'depends': ['base','openeducat_erp'],
    'data': [
        'views/internship_view.xml',
        'views/religion_view.xml',
        'views/company_submission_view.xml',
        'views/educational_history.xml',
        'views/project_experience.xml',
        'menu/internship_menu.xml',
    ],
    'demo': [
    ],
    'application': True,
}