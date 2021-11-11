# -*- coding: utf-8 -*-
{
    'name': "CRM Qualifications",

    'summary': """
        Qualify leads
        Link lead to existing customer""",

    'description': """
            Add information for which the customer must be contacted , but without crezting an opportunity
    """,

    'author': "ABDELILAH OUAMAMOU",
    'website': "",
    'category': 'CRM',
    'version': '12.0.3.1',

    'depends': ['crm', 'mail', 'base'],

    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views_inherit.xml',
        'views/res_partner_views_inherit.xml',
        'wizard/lead_define_date_wizard_view.xml',
        'wizard/crm_lead_wizard_view.xml',
        'wizard/lead_next_action_wizard_view.xml',
        'views/crm_menuitems.xml'],

    'installable': True,
    'application': False

}
