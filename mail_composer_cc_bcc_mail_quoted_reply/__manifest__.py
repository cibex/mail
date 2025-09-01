# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Email CC when replying to all",
    "summary": """This module changes the behavior of reply to all.
    All original recipients are now cc recipients.""",
    "version": "18.0.1.0.0",
    "category": "Social",
    "website": "https://github.com/OCA/mail",
    "author": "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "auto_install": True,
    "depends": [
        "mail_composer_cc_bcc",
        "mail_quoted_reply",
    ],
}
