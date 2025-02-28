import requests

from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    vehicle_ids = fields.One2many("vehicle", "partner_id", string="Vehicles")
    vehicle_count = fields.Integer(compute="_compute_vehicle_count")
    is_driver = fields.Boolean()

    @api.depends("vehicle_ids")
    def _compute_vehicle_count(self):
        for partner in self:
            partner.vehicle_count = 0
            if partner.vehicle_ids:
                partner.vehicle_count = len(partner.vehicle_ids)

    def action_send_vehicles(self):
        return True

    def action_view_vehicles(self):
        action = self.env["ir.actions.actions"]._for_xml_id("fleet_management.vehicle_action")

        if self.vehicle_count > 1:
            action["domain"] = [("id", "in", self.vehicle_ids.ids)]
            return action

        form_view = [(self.env.ref("fleet_management.vehicle_form_view").id, "form")]

        views = form_view
        if "views" in action:
            views = form_view + [(state, view) for state, view in action["views"] if view != "form"]

        action["views"] = views
        action["res_id"] = self.vehicle_ids.id
        return action