from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.common.by import By


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "IE":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements(By.NAME, "user")) > 0:  # checking if
            # logging page is open
            return
        elif wd.current_url.endswith("/addressbook/") \
                and len(wd.find_elements(By.XPATH, "//input[@value='Send_e-Mail']")) > 0:  # checking if contact list
            # is open
            return
        else:
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
