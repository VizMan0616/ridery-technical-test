from odoo import _, api, fields, models


class EndpointLog(models.Model):
    _name = "endpoint.log"
    _description = "Log"

    create_date = fields.Datetime("Response Date", readonly=True)
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("wait", "Waiting"),
            ("success", "Success"),
            ("error", "Error"),
        ],
        string="Response State",
        default="draft"
    )
    message = fields.Text(string="Response Message")

    @api.model
    def pull_log(self, status_code: int, msg: str):
        state_vals = {"state": "success", "message": msg}

        if status_code >= 400 or status_code >= 500:
            state_vals["state"] = "error"
        self.create(state_vals)