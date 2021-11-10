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
    'version': '12.0.2.0',

    'depends': ['crm','mail','base'],

    'data': [
        'views/res_partner_views_inherit.xml'],
    
    'installable':True,
    'application':False

}