
# Data for filling the new contact form

class Primary_data:
    def __init__(self, firstname, middlename, lastname, nickname, title, company, address):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address


class Contact_data:
    def __init__(self, home, mobile, work, fax, email, email2, email3, homepage):
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage


class Birthday:
    def __init__(self, bday, bmonth, byear, aday, amonth, ayear):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear


class Secondary_data:
    def __init__(self, address2, phone2, notes):
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
