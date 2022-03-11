# -*- coding: utf-8 -*-
{
    'name' : 'School Event Mangement ',
    'version' : '14.0.1.0.0',
    'summary': 'School Annual Funtion Organisation ',
    'author': 'Bibhuti Bhusan Sahoo',
    'sequence': 20,
    'description': """ Organisaiton School Fuction """,
    'company': 'Bibhuti Bhusan Sahoo',
    'maintainer': 'Bibhuti Bhusan Sahoo',
    'category': 'Accounting',
    'depends' : ['board','project','mail','web','web_tour'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/fund_check.xml',
        'wizard/school_event.xml',
        'views/school.xml',
        'views/assets.xml',
        'views/funds.xml',
        'views/dashboard.xml',
        'views/invoice.xml',
        # 'reports/custom_header.xml',
        # 'reports/custom_footer.xml',
        'reports/report.xml',
        'reports/invoice_report.xml',
        'reports/school_card.xml'

    ],
    'demo':[],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
