import re
# from model.group import Group
# from random import randrange

# test comparing all fields shown in home page with information from database for all contacts


def test_contact_on_home_page(app, db):
    # contact_list = app.contact.get_contact_list()
    # index = randrange(len(contact_list))
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    # contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contacts_from_home_page.lastname == contacts_from_db.lastname  # lastname
    assert contacts_from_home_page.firstname == contacts_from_db.firstname  # firstname
    assert contacts_from_home_page.address == contacts_from_db.address  # address
    # emails
    assert contacts_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db)
    # phones
    assert contacts_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.phone_home, contact.phone_mobile,
                                        contact.phone_work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
