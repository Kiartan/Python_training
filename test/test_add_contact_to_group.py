# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test_add"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_add"))

    contact = db.choose_random_contact()
    group = db.choose_random_group()
    start_list = orm.get_contacts_in_group(group.id)
    app.contact.add_contact_to_group_by_id(contact.id, group.name)
    check_list = orm.get_contacts_in_group(group.id)
    for contact.id in check_list:
        pass
    assert len(start_list) + 1 == len(check_list)
    start_list.append(contact)
    assert start_list == check_list


    # old_contacts = db.get_contact_list()
    # app.contact.create(contact)
    # new_contacts = db.get_contact_list()
    # old_contacts.append(contact)
    # assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)
    # if check_ui:
        # assert sorted(new_contacts, key=Group.id_or_max) == sorted(app.contact.get_contact_list(), key=Group.id_or_max)
