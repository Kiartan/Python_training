# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group_contact import *
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def Open_main_page(self, wd):
        wd.get("http://localhost/addressbook/addressbook/")

    def login(self, wd, username, password):
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.ID, "LoginForm").click()
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def Create_contact(self, wd, Primary_data, Contact_data, Secondary_data):
        # Init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        # Filling the form
        # Primary data
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(Primary_data.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(Primary_data.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(Primary_data.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(Primary_data.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(Primary_data.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(Primary_data.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(Primary_data.address)
        # Contact data
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(Contact_data.home)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(Contact_data.mobile)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(Contact_data.work)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(Contact_data.fax)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(Contact_data.email)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(Contact_data.email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(Contact_data.email3)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(Contact_data.homepage)
        # Secondary data
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(Secondary_data.address2)
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(Secondary_data.phone2)
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(Secondary_data.notes)

    def birthday(self, wd, Birthday):
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(Birthday.bday)
        wd.find_element(By.XPATH, "//option[@value='10']").click()
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(Birthday.bmonth)
        wd.find_element(By.XPATH, "//option[@value='January']").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(Birthday.byear)
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(Birthday.aday)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[3]/option[7]").click()
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(Birthday.amonth)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[4]/option[3]").click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(Birthday.ayear)

    def Submiting_the_form(self, wd):
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def Logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.Open_main_page(wd)
        self.login(wd, username="admin", password="secret")
        self.Create_contact(wd, Primary_data(firstname="test", middlename="test test", lastname="ccc", nickname="ddd",
                                             title="eee", company="fff", address="ggg"),
            Contact_data(home="hhh", mobile="iii", work="jjj", fax="kkk", email="lll", email2="mmm", email3="nnn",
                         homepage="ooo"),
            Secondary_data(address2="ppp", phone2="qqq", notes="rrr"))
        self.birthday(wd, Birthday(bday="10", bmonth="January", byear="2000", aday="5", amonth="February",
                                   ayear="2010"))
        self.Submiting_the_form(wd)
        self.Logout(wd)

# for empty contact the test runs without birthday method
    def test_add_empty_contact(self):
        wd = self.wd
        self.Open_main_page(wd)
        self.login(wd, username="admin", password="secret")
        self.Create_contact(wd, Primary_data(firstname="", middlename="", lastname="", nickname="",
                                             title="", company="", address=""),
            Contact_data(home="", mobile="", work="", fax="", email="", email2="", email3="",
                         homepage=""),
            Secondary_data(address2="", phone2="", notes=""))
        self.Submiting_the_form(wd)
        self.Logout(wd)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
