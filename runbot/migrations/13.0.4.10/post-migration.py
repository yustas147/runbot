# -*- coding: utf-8 -*-


def migrate(cr, version):

    cr.execute("""
        INSERT INTO runbot_branch_group (name)
        SELECT distinct(branch_name)
        FROM runbot_branch
        WHERE name LIKE 'refs/heads/%'
    """)
