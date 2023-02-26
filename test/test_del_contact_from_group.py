from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app, db):
    if len(db.get_group_list_with_added_contacts()) == 0:
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="test_add"))
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test_add"))
        contact = db.choose_random_contact()
        group = db.choose_random_group()
        app.contact.add_contact_to_group_by_id(contact.id, group.name)

    groups_with_contacts = db.get_group_list_with_added_contacts()
    group = random.choice(groups_with_contacts)
    start_list = orm.get_contacts_in_group(group.id)
    contact = random.choice(start_list)
    db.delete_contact_from_group_by_id(contact.id, group.id)
    check_list = orm.get_contacts_not_in_group(group.id)
    for contact.id in check_list:
        pass
    assert len(start_list) - 1 == len(check_list)
    start_list.remove(contact)
    assert start_list == check_list

    # old_contacts = db.get_contact_list()
    # contact = random.choice(old_contacts)
    # app.contact.delete_contact_by_id(contact.id)
    # new_contacts = db.get_contact_list()
    # assert len(old_contacts) - 1 == len(new_contacts)
    # old_contacts.remove(contact)
    # assert old_contacts == new_contacts
    # if check_ui:
        # assert sorted(new_contacts, key=Group.id_or_max) == sorted(app.contact.get_contact_list(), key=Group.id_or_max)
