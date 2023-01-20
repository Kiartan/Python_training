# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact(firstname="edit1", middlename="edit1", lastname="edit1", nickname="edit1",
                                             title="edit1", company="edit1", address="edit1", phone_home="edit2",
                                             phone_mobile="edit2", phone_work="edit2", fax="edit2", email="edit2",
                                             email2="edit2", email3="edit2", homepage="edit2", bday="18", bmonth="May",
                                             byear="edit3", aday="13", amonth="June", ayear="edit3", address2="edit4",
                                             phone2="edit4", notes="edit4"))
