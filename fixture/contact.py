from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_the_contact(self, contact):
        wd = self.app.wd
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

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # Open page with contacts
        self.app.open_home_page()
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # edit
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_the_contact(contact)
        # update and return
        wd.find_element(By.NAME, "update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # Open page with contacts
        self.app.open_home_page()
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))
