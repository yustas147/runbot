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

    def test_hook_controller(self):
        res = self.url_open('/runbot/hook/')
        print(res)