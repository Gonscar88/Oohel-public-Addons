# -*- coding: utf-8 -*-
# Created by Oohel at 8/03/19
# Oohel Extra Tools 2019
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Sessions Management",

    'summary': """
            Sessions Management
        """,

    'description':
        """
          Functionalities:
            * Close all Odoo sessions
        """,

    'version': "1.0",

    'author': "Oohel Technologies",

    'license': "AGPL-3",
    'website': "https://www.oohel.net",
    'category': "Extra Tools",

    'depends': [
        'base',
    ],

    'data': [
    	'views/close_sessions_wizard_view.xml',
    ],

    'application': True,
    'installable': True,
}
