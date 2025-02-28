from odoo import _, api, fields, models


class Vehicle(models.Model):
    _name = "vehicle"
    _inherit = ["mail.thread", "mail.activity.mixin", "image.mixin"]
    _description = "Vehicle"
    _check_company_auto = True
    _order = "id asc, sequence asc"

    company_id = fields.Char("res.company", default=lambda self: self.env.company.id)
    active = fields.Boolean(default=True)
    name = fields.Char("Model Name", required=True, tracking=True)
    sequence = fields.Char("Sequence", default="00000")
    plate_code = fields.Char("Plate", size=7, required=True, tracking=True, unaccent=True)
    partner_id = fields.Many2one(
        "res.partner",
        string="Driver",
        domain="[('is_driver', '=', True)]",
        required=True,
        index=True,
        tracking=True,
    )
    brand_id = fields.Many2one(
        "vehicle.brand",
        string="Brand",
        required=True,
        index=True,
        tracking=True,
    )
    color = fields.Char(required=True, tracking=True)
    release_year = fields.Char("Release Year", tracking=True)

    @api.depends("name", "sequence", "brand_id")
    def _compute_display_name(self):
        super()._compute_display_name()

        for vehicle in self:
            name = ""
            if vehicle.sequence:
                name += f"[{vehicle.sequence}]"
            name += " " + " - ".join(
                [
                    vehicle.brand_id.name or "",
                    vehicle.name or "",
                ]
            )
            vehicle.display_name = name

    @api.model_create_multi
    def create(self, vals_list: list[dict]):
        seq_obj = self.env["ir.sequence"]
        for vals in vals_list:
            if vals.get("sequence", "00000") == "00000":
                vals["sequence"] = seq_obj.next_by_code(self._name) or "00000"
        return super().create(vals_list)

