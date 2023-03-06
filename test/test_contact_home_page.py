import re
from model.group import Group

# test comparing all fields shown in home page with information from database for all contacts


def test_contact_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Group.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Group.id_or_max)
    assert len(contacts_from_home_page) == len(contacts_from_db)
    min_length = len(contacts_from_home_page)
    if len(contacts_from_home_page) >= len(contacts_from_db):
        min_length = len(contacts_from_db)

    for i in range(min_length):
        if contacts_from_home_page[i] == contacts_from_db[i]:
        # if x.id == y.id in contacts_from_db:
            assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname  # lastname
            assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname  # firstname
            assert contacts_from_home_page[i].address == contacts_from_db[i].address  # address
            # emails
            assert contacts_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])
            # phones
            assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.phone_home, contact.phone_mobile, contact.phone_work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
