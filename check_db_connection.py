from fixture.orm import ORMFixture
from model.group import Group
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

group_list = db.get_group_list()
group = random.choice(group_list)
try:
    l = db.get_contacts_in_group(Group(id="80"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()
