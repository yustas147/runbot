# -*- coding: utf-8 -*-
from .common import RunbotCase

class Test_BranchGroup(RunbotCase):

    def setUp(self):
        super(Test_BranchGroup, self).setUp()
        Repo = self.env['runbot.repo']
        self.repo = Repo.create({'name': 'bla@example.com:foo/bar', 'token': '123'})
        self.repo_dev = Repo.create({'name': 'bla@example.com:foo-dev/bar', 'token': '123'})
        self.Branch = self.env['runbot.branch']

    def test_branch_creation_creates_branch_group(self):
        """ test that a BranchGroup is created a branch/pr creation """
        branch = self.Branch.create({
            'repo_id': self.repo_dev.id,
            'name': 'refs/head/master-feature'
        })

        mock_github = self.patchers['github_patcher']
        mock_github.return_value = {
            'head' : {'label': 'foo-dev:master-feature'},
            'base' : {'ref': 'master'},
        }
        pr = self.Branch.create({
            'repo_id': self.repo.id,
            'name': 'refs/pull/12345'
        })

        branch_group = self.env['runbot.branch_group'].search([('name', '=', 'master-feature')])
        self.assertEqual(branch_group.name, branch.branch_name)
        self.assertEqual(branch_group.name, branch.pull_branch_name)
        self.assertIn(branch, branch_group.branch_ids)

        self.assertEqual(branch_group.name, pr.pull_branch_name)
        self.assertIn(pr, branch_group.branch_ids)
