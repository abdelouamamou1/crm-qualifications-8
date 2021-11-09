# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

     
    ## Overide onchange partner function for get contact,partner and title of customer automatically    ##
    def _onchange_partner_id_values(self, partner_id):
        if partner_id:
            partner = self.env['res.partner'].browse(partner_id)
            partner_name = partner.parent_id.name
            if not partner_name and partner.is_company:
                partner_name = partner.name
            
            contact_name = partner.child_ids[0]['name'] if partner.is_company else partner.name
            title = partner.child_ids[0].title.id if partner.is_company else partner.title.id

            return {
                'partner_name': partner_name,
                'contact_name': contact_name ,#partner.name if not partner.is_company else False,
                'title': title, #partner.title.id,
                'street': partner.street,
                'street2': partner.street2,
                'city': partner.city,
                'state_id': partner.state_id.id,
                'country_id': partner.country_id.id,
                'email_from': partner.email,
                'phone': partner.phone,
                'mobile': partner.mobile,
                'zip': partner.zip,
                'function': partner.function,
                'website': partner.website,
            }
        return {}