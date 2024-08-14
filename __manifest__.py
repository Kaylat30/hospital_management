{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Manage hospital patients and records',
    'description': 'A module to manage hospital patients, their records, and related information.',
    'category': 'Healthcare',
    'author': 'Kayondo',
    'depends': ['base'],
    'data': [
        'views/patient.xml',
        'views/doctor.xml',
        'security/ir.model.access.csv',
        'reports/reports.xml',
    ],
    'installable': True,
    'application': True,
}
