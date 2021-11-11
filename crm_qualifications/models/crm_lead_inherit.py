# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    reminder_date = fields.Date(string='Reminder date')  # next action date

   # create onchange partner name function that check if customer already exist
    @api.onchange('partner_name')
    def onchange_partner_name(self):
        partner_obj = self.env['res.partner']
        if self.partner_name:
            partner_id = partner_obj.search(
                [('name', 'ilike', self.partner_name)], limit=1)

            if partner_id:
                child_id = partner_obj.search(
                    [('parent_id', '=', partner_id.id)], limit=1)
                if child_id:
                    self.update({'contact_name': child_id.name,
                                 'title': child_id.title.id if child_id.title.id else False})
