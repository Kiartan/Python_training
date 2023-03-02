import re
from model.group import Group

# test comparing all fields shown in home page with information from database for all contacts


def test_contact_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Group.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Group.id_or_max)
    # assert contacts_from_home_page == contacts_from_db
    for x in contacts_from_home_page:
        for y in contacts_from_db:
            assert x.lastname == y.lastname  # lastname
            assert x.firstname == y.firstname  # firstname
            assert x.address == y.address  # address
            # emails
            assert x.all_emails_from_home_page == merge_emails_like_on_home_page(y)
            # phones
            assert x.all_phones_from_home_page == merge_phones_like_on_home_page(y)


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
