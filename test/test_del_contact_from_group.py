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
        contact_list = orm.get_contact_list()
        contact = random.choice(contact_list)
        group_list = orm.get_group_list()
        group = random.choice(group_list)
        app.contact.add_contact_to_group_by_id(contact.id, group.id)

    groups_with_contacts = db.get_group_list_with_added_contacts()
    group1 = random.choice(groups_with_contacts)
    #start_list = orm.get_contacts_not_in_group(group1)

    before_list = orm.get_contacts_in_group(group1)
    contact = random.choice(before_list)

    db.delete_contact_from_group_by_id(contact.id, group1.id)
    after_list = orm.get_contacts_in_group(group1)
    print(group1, contact, before_list, after_list)
    #check_list = orm.get_contacts_not_in_group(group1)

    #assert len(before_list) - 1 == len(after_list)
    #assert len(start_list) + 1 == len(check_list)
    #before_list.remove(contact)
    #assert sorted(before_list, key=Group.id_or_max) == sorted(after_list, key=Group.id_or_max)

    # old_contacts = db.get_contact_list()
    # contact = random.choice(old_contacts)
    # app.contact.delete_contact_by_id(contact.id)
    # new_contacts = db.get_contact_list()
    # assert len(old_contacts) - 1 == len(new_contacts)
    # old_contacts.remove(contact)
    # assert old_contacts == new_contacts
    # if check_ui:
        # assert sorted(new_contacts, key=Group.id_or_max) == sorted(app.contact.get_contact_list(), key=Group.id_or_max)
