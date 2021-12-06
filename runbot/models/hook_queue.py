import json

from odoo import models, fields, api


class Json(fields._String):

    type = 'json'
    column_type = ('json', 'json')
    column_cast_from = ('text', 'varchar')

    def convert_to_column(self, value, record, values=None, validate=True):
        if value is None or value is False:
            return json.dumps(value)
        return json.dumps(json.loads(value))

    def convert_to_cache(self, value, record, validate=True):
        return json.loads(value)


class HookQueue(models.Model):
    _name = 'runbot.hook.queue'
    _description = "Queue of received hooks"

    payload = Json(help="Json content received from github")
    remote_id = fields.Many2one('runbot.remote')
