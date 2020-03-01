# -*- coding: utf-8 -*-
import logging
import re
import time
from subprocess import CalledProcessError
from odoo import models, fields, api
from odoo.osv import expression

_logger = logging.getLogger(__name__)


class BranchGroup(models.Model):

    _name = "runbot.branch_group"
    _description = "Branch Group"
    _order = 'name'

    name = fields.Char('Branches name', required=True)
    branch_ids = fields.One2many('runbot.branch', compute='_compute_branch_ids')

    @api.depends('name')
    def _compute_branch_ids(self):
        for branch_group in self:
            branch_group.branch_ids = self.env['runbot.branch'].search(['|', ('branch_name', '=', branch_group.name), ('pull_head_name', '=like', '%%:%s' % branch_group.name)])
