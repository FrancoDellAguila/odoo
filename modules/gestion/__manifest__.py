# -*- coding: utf-8 -*-
{
    'name': "Sistema de Gestión de Franquicias",

    'summary': "Plataforma diseñada para automatizar y optimizar los procesos administrativos relacionados con la gestión de franquicias",

    'description': """
Herramienta digital que centraliza y automatiza la administración de franquicias. Diseñada para franquiciantes y franquiciados, la app optimiza tareas como la gestión de contratos, el cálculo de regalías, la facturación y el monitoreo de indicadores clave de desempeño (KPIs). Su diseño intuitivo y modular permite personalizar funciones según las necesidades específicas del usuario, asegurando una experiencia eficiente y escalable.
    """,

    'author': "Franco Dell Aguila Ureña",
    'website': "https://www.linkedin.com/in/franco-dell-aguila/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Franchising',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

