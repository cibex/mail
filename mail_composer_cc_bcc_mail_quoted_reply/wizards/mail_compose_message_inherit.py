from odoo import Command, models


class MailComposeMessageInherit(models.TransientModel):
    _inherit = "mail.compose.message"

    def default_get(self, fields_list):
        vals = super().default_get(fields_list=fields_list)
        default_cc_partner_ids = self._context.get("default_cc_partner_ids", [])
        if default_cc_partner_ids:
            link_partner_list = [
                Command.link(partner) for partner in default_cc_partner_ids
            ]
            vals.update(partner_cc_ids=link_partner_list)
        return vals
