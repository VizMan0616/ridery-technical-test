import json
import logging

import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout

from odoo import _, api, fields, models

from ..utils import get_url

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    vehicle_ids = fields.One2many("vehicle", "partner_id", string="Vehicles")
    vehicle_count = fields.Integer(compute="_compute_vehicle_count")
    is_driver = fields.Boolean()

    def _get_vehicles_vals(self) -> list:
        self.ensure_one()

        vehicle_vals = []
        if not self.vehicle_ids:
            return vehicle_vals

        for vehicle in self.vehicle_ids:
            vehicle_vals.append(
                {
                    "model_name": vehicle.name,
                    "driver_name": self.name,
                    "plate_code": vehicle.plate_code,
                    "brand_name": vehicle.brand_id.name,
                    "year": vehicle.release_year,
                    "color": vehicle.color,
                }
            )
        return vehicle_vals

    @api.depends("vehicle_ids")
    def _compute_vehicle_count(self):
        for partner in self:
            partner.vehicle_count = 0
            if partner.vehicle_ids:
                partner.vehicle_count = len(partner.vehicle_ids)

    def action_send_vehicles(self):
        self.ensure_one()

        log_obj = self.env["endpoint.log"]
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        url = get_url() + "/vehicles"

        payload = self._get_vehicles_vals()
        status, state = "success", "success"
        msg, endpoint_res_message = "", _("Vehicles were registered sucessfully!")

        try:
            response = requests.post(url, timeout=10, json=payload, headers=headers)
            response.raise_for_status()

            content = response.content.decode("utf-8")
            msg, endpoint_res_message = content, json.loads(content)["message"]
        except HTTPError as http_err:
            status, state = "danger", "error"
            content = http_err.response.content.decode("utf-8")
            msg, endpoint_res_message = content, json.loads(content)["message"]
        except Exception as ex:
            _logger.error(ex)
            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "type": "danger",
                    "message": _("There was an error during execution."),
                },
            }

        log_obj.pull_log(state, msg)
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "type": status,
                "message": endpoint_res_message,
            },
        }

    def action_view_vehicles(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "fleet_management.vehicle_action"
        )

        if self.vehicle_count > 1:
            action["domain"] = [("id", "in", self.vehicle_ids.ids)]
            return action

        form_view = [(self.env.ref("fleet_management.vehicle_form_view").id, "form")]

        views = form_view
        if "views" in action:
            views = form_view + [
                (state, view) for state, view in action["views"] if view != "form"
            ]

        action["views"] = views
        action["res_id"] = self.vehicle_ids.id
        return action
