from odoo import api, fields, models


class TimesheetsAnalysisReport(models.Model):
    _inherit = "timesheets.analysis.report"

    maintenance_request_id = fields.Many2one(
        "maintenance.request", string="Maintenance Request", readonly=True
    )

    @api.model
    def _select(self):
        return super()._select() + ",\n            A.maintenance_request_id AS maintenance_request_id"
