from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys
import re


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if 0 == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def clear(s):
    return re.sub("['`\/]", "", s)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(map(lambda x: clear(x), [random.choice(symbols) for i in range(random.randrange(maxlen))]))


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    phone_home="", phone_mobile="", phone_work="", fax="", email="", email2="", email3="", homepage="",
                    bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", address2="", phone2="",
                    notes="")] + [
    Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
            title=random_string("title", 20), company=random_string("company", 20),
            address=random_string("address", 30), phone_home=random_string("phone_home", 20),
            phone_mobile=random_string("phone_mobile", 20), phone_work=random_string("phone_work", 20),
            fax=random_string("fax", 20), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20), homepage=random_string("homepage", 20),
            bday=str(random.randrange(1, 32)), bmonth=random.choice(months), byear=str(random.randrange(1, 3001)),
            aday=str(random.randrange(1, 32)), amonth=random.choice(months), ayear=str(random.randrange(1, 3001)),
            address2=random_string("address2", 30), phone2=random_string("phone2", 9), notes=random_string("notes", 30))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
