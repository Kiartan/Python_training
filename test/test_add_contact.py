# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="test", middlename="test test", lastname="ccc", nickname="ddd",
                               title="eee", company="fff", address="ggg", home="hhh", mobile="iii",
                               work="jjj", fax="kkk", email="lll", email2="mmm", email3="nnn",
                               homepage="ooo", bday="10", bmonth="January", byear="2000", aday="5",
                               amonth="February", ayear="2010", address2="ppp", phone2="qqq", notes="rrr"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home="", mobile="",
                               work="", fax="", email="", email2="", email3="",
                               homepage="", bday="-", bmonth="-", byear="", aday="",
                               amonth="", ayear="", address2="", phone2="", notes=""))
    app.session.logout()
