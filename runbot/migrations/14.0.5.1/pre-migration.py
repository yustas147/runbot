# -*- coding: utf-8 -*-

from odoo.upgrade import util

def migrate(cr, _version):
    util.remove_view(cr, 'runbot.layout')
    util.remove_view(cr, 'runbot.bundles')

    # to remove
    util.remove_field(cr, 'runbot.build.stat', 'write_date')
    util.remove_field(cr, 'runbot.build.stat', 'create_date')
    util.remove_field(cr, 'runbot.build.stat', 'write_uid')
    util.remove_field(cr, 'runbot.build.stat', 'create_uid')
