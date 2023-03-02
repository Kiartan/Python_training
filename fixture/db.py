import mysql.connector
from model.group import Group
from model.contact import Contact
import random
import time


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, email=email,
                                    email2=email2, email3=email3, phone_home=home, phone_mobile=mobile, phone_work=work,
                                    phone2=phone2))
        finally:
            cursor.close()
            # time.sleep(1)
            return list

    def get_group_list_with_added_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups")
            for row in cursor:
                (id) = row
                list.append(Group(id=str(id)))
        finally:
            cursor.close()
        return list

    def delete_contact_from_group_by_id(self, id1, id2):
        # id1 = contact id
        # id2 = group id
        cursor = self.connection.cursor()
        try:
            cursor.execute("delete from address_in_groups where `address_in_groups`.`id` = id1  "
                           "and `address_in_groups`.`group_id` = id2")
        finally:
            cursor.close()

    def destroy(self):
        self.connection.close()
