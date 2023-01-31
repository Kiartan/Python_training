# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="edit1", middlename="edit1", lastname="edit1", nickname="edit1",
                                             title="edit1", company="edit1", address="edit1", phone_home="edit2",
                                             phone_mobile="edit2", phone_work="edit2", fax="edit2", email="edit2",
                                             email2="edit2", email3="edit2", homepage="edit2", bday="18", bmonth="May",
                                             byear="1992", aday="13", amonth="June", ayear="edit3", address2="edit4",
                                             phone2="edit4", notes="edit4")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)
