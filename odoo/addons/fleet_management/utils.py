from odoo.tools import config


def get_url():
    return "http://" + config.get("api_url", "service:80")
