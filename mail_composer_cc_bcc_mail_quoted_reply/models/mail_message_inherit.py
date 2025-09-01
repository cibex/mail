from odoo import models


class MailMessageInherit(models.Model):
    _inherit = "mail.message"

    def _default_reply_partner(self, reply_all: bool = False):
        default_partner_ids = super()._default_reply_partner(reply_all=reply_all)
        if reply_all:
            default_partner_ids.extend(
                (self.recipient_cc_ids - self.env.user.partner_id).ids
            )
        return default_partner_ids

    def reply_message(self, reply_all: bool = False):
        action = super().reply_message(reply_all=False)
        if reply_all:
            context = action.get("context", None)
            if context:
                cc_partner_ids = list(
                    set(self._default_reply_partner(reply_all=True))
                    - set(context.get("default_partner_ids", []))
                )
                context.update(default_cc_partner_ids=cc_partner_ids)
        return action
