from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
from model.group import Group
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]") [index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def fill_the_contact(self, contact):
        # Primary data
        self.app.group.change_field_value("firstname", contact.firstname)
        self.app.group.change_field_value("middlename", contact.middlename)
        self.app.group.change_field_value("lastname", contact.lastname)
        self.app.group.change_field_value("nickname", contact.nickname)
        self.app.group.change_field_value("title", contact.title)
        self.app.group.change_field_value("company", contact.company)
        self.app.group.change_field_value("address", contact.address)
        # Contact data
        self.app.group.change_field_value("home", contact.phone_home)
        self.app.group.change_field_value("mobile", contact.phone_mobile)
        self.app.group.change_field_value("work", contact.phone_work)
        self.app.group.change_field_value("fax", contact.fax)
        self.app.group.change_field_value("email", contact.email)
        self.app.group.change_field_value("email2", contact.email2)
        self.app.group.change_field_value("email3", contact.email3)
        self.app.group.change_field_value("homepage", contact.homepage)
        # Birthday
        self.change_date_value("bday", contact.bday)
        self.change_date_value("bmonth", contact.bmonth)
        self.app.group.change_field_value("byear", contact.byear)
        self.change_date_value("aday", contact.aday)
        self.change_date_value("amonth", contact.amonth)
        self.app.group.change_field_value("ayear", contact.ayear)
        # Secondary data
        self.app.group.change_field_value("address2", contact.address2)
        self.app.group.change_field_value("phone2", contact.phone2)
        self.app.group.change_field_value("notes", contact.notes)

    def change_date_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)

    def create(self, contact):
        wd = self.app.wd
        # Open page with contacts
        self.app.open_home_page()
        # Init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        # Filling the form
        self.fill_the_contact(contact)
        # submitting the form
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        # Open page with contacts
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # edit
        wd.find_elements(By.XPATH, "//img[@alt='Edit']") [index].click()
        self.fill_the_contact(contact)
        # update and return
        wd.find_element(By.NAME, "update").click()
        wd.find_element(By.LINK_TEXT, "home page").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        # Open page with contacts
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # edit
        wd.find_element(By.XPATH, "//a[@href='edit.php?id=%s']" % id).click()
        self.fill_the_contact(contact)
        # update and return
        wd.find_element(By.NAME, "update").click()
        wd.find_element(By.LINK_TEXT, "home page").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # Open page with contacts
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        wd.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # Open page with contacts
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        # wd.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
                last = cells[1].text
                first = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=last, firstname=first, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        phone_home = wd.find_element(By.NAME, "home").get_attribute("value")
        phone_mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        phone_work = wd.find_element(By.NAME, "work").get_attribute("value")
        phone2 = wd.find_element(By.NAME, "phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       email=email, email2=email2, email3=email3,
                       phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        phone_home = re.search("H: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work, phone2=phone2)

    def add_contact_to_group_by_id(self, id, group_id):
        wd = self.app.wd
        # Open contact page and select one
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # Add selected contact into one group
        self.add_to_certain_group(group_id)
        # Return to home page
        wd.find_element(By.LINK_TEXT, "home").click()
        self.contact_cache = None

    def add_to_certain_group(self, id):
        wd = self.app.wd
        wd.find_element(By. NAME, "to_group").click()
        wd.find_element(By.XPATH, "//option[@value='%s']" % int(id)).click()
        wd.find_element(By.NAME, "add").click()


#/html/body/div/div[4]/form[2]/div[4]/select/option[6]