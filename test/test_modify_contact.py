# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_mod = Contact(firstname="edit1", middlename="edit1", lastname="edit1", nickname="edit1", title="edit1",
                          company="edit1", address="edit1", phone_home="edit2", phone_mobile="edit2",
                          phone_work="edit2", fax="edit2", email="edit2", email2="edit2", email3="edit2",
                          homepage="edit2", bday="18", bmonth="May", byear="1992", aday="13", amonth="June",
                          ayear="edit3", address2="edit4", phone2="edit4", notes="edit4")
    app.contact.modify_contact_by_id(contact.id, contact_mod)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    position = old_contacts.index(contact)
    contact_mod.id = contact.id
    old_contacts[position] = contact_mod
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Group.id_or_max) == sorted(app.contact.get_contact_list(), key=Group.id_or_max)
