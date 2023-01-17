# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="edit1", middlename="edit1", lastname="edit1", nickname="edit1",
                               title="edit1", company="edit1", address="edit1", home="edit2", mobile="edit2",
                               work="edit2", fax="edit2", email="edit2", email2="edit2", email3="edit2",
                               homepage="edit2", bday="10", bmonth="January", byear="edit3", aday="5",
                               amonth="February", ayear="edit3", address2="edit4", phone2="edit4", notes="edit4"))
    app.session.logout()
