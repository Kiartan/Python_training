# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_mod = Group(name="New group")
    app.group.modify_group_by_id(group.id, group_mod)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    position = old_groups.index(group)
    group_mod.id = group.id
    old_groups[position] = group_mod
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
    # if app.group.count() == 0:
        # app.group.create(Group(name="test"))
    # old_groups = app.group.get_group_list()
    # app.group.modify_first_group(Group(header="New header"))
    # new_groups = app.group.get_group_list()
    # assert len(old_groups) == len(new_groups)
