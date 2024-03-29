{
    'name': 'Student Admission',
    'version': '16.0.1.0.1',
    'summary': """Core Module of Educational ERP""",
    'description': 'Core Module of Educational ERP',
    'category': 'Educational',
    'author': 'Pranshu',
    'company': 'Odoo Hosting',
    'website': "http://www.erpcall.com",
    'depends': ['base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_attendance.xml',
    ],
    'demo': [

    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
