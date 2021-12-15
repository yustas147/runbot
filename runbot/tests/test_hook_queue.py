from odoo.tests.common import HttpCase

from .common import RunbotCase


class TestHookQueue(RunbotCase):

    def test_json_field(self):
        HookQueue = self.env['runbot.hook.queue']
        hook_queue = HookQueue.create({'payload': '{"action": "edited"}'})
        self.assertEqual(hook_queue.payload, {'action': 'edited'}, "payload should return a valid python object")

        hook_queue = HookQueue.create({'payload': '{}'})
        self.assertEqual(hook_queue.payload, {}, "payload should return a valid python object")

        hook_queue = HookQueue.create({'payload': '[]'})
        self.assertEqual(hook_queue.payload, [], "payload should return a valid python object")

        hook_queue = HookQueue.create({'payload': 'false'})
        self.assertFalse(hook_queue.payload, "Falsy json should be False")

        hook_queue = HookQueue.create({'payload': 'null'})
        self.assertFalse(hook_queue.payload, "Falsy json should be False")


class TestHookController(HttpCase):

    def setUp(self):
        super().setUp()
        self.project = self.env['runbot.project'].create({'name': 'Tests'})
        self.repo_server = self.env['runbot.repo'].create({
            'name': 'server',
            'project_id': self.project.id,
            'server_files': 'server.py',
            'addons_paths': 'addons,core/addons'
        })

        self.remote_server = self.env['runbot.remote'].create({
            'name': 'bla@example.com:base/server',
            'repo_id': self.repo_server.id,
            'token': '123',
        })

    def test_hook_controller(self):

        res = self.url_open(f'/runbot/hook/{self.remote_server.id}')
        self.assertEqual(res.status_code, 200)
