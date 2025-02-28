from odoo import fields, models


class VehicleBrand(models.Model):
    _name = "vehicle.brand"
    _description = "Vehicle Brand"

    name = fields.Char()
    active = fields.Boolean(default=True)
