# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test", middlename="test test", lastname="ccc", nickname="ddd",
                               title="eee", company="fff", address="ggg", phone_home="hhh", phone_mobile="iii",
                               phone_work="jjj", fax="kkk", email="lll", email2="mmm", email3="nnn",
                               homepage="ooo", bday="10", bmonth="January", byear="2000", aday="5",
                               amonth="February", ayear="2010", address2="ppp", phone2="qqq", notes="rrr")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", phone_home="", phone_mobile="",
                               phone_work="", fax="", email="", email2="", email3="",
                               homepage="", bday="-", bmonth="-", byear="", aday="-",
                               amonth="-", ayear="", address2="", phone2="", notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)
