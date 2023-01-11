# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/addressbook/")
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys("admin")
        driver.find_element(By.ID, "LoginForm").click()
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys("secret")
        driver.find_element(By.XPATH, "//input[@value='Login']").click()
        driver.find_element(By.LINK_TEXT, "add new").click()
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys("aaa")
        driver.find_element(By.NAME, "middlename").click()
        driver.find_element(By.NAME, "middlename").clear()
        driver.find_element(By.NAME, "middlename").send_keys("bbb")
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").clear()
        driver.find_element(By.NAME, "lastname").send_keys("ccc")
        driver.find_element(By.NAME, "nickname").click()
        driver.find_element(By.NAME, "nickname").clear()
        driver.find_element(By.NAME, "nickname").send_keys("ddd")
        driver.find_element(By.NAME, "title").click()
        driver.find_element(By.NAME, "title").clear()
        driver.find_element(By.NAME, "title").send_keys("eee")
        driver.find_element(By.NAME, "company").click()
        driver.find_element(By.NAME, "company").clear()
        driver.find_element(By.NAME, "company").send_keys("fff")
        driver.find_element(By.NAME, "address").click()
        driver.find_element(By.NAME, "address").clear()
        driver.find_element(By.NAME, "address").send_keys("ggg")
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "theform").click()
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "home").clear()
        driver.find_element(By.NAME, "home").send_keys("hhh")
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").clear()
        driver.find_element(By.NAME, "mobile").send_keys("iii")
        driver.find_element(By.NAME, "work").click()
        driver.find_element(By.NAME, "work").clear()
        driver.find_element(By.NAME, "work").send_keys("jjj")
        driver.find_element(By.NAME, "fax").click()
        driver.find_element(By.NAME, "fax").clear()
        driver.find_element(By.NAME, "fax").send_keys("kkk")
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys("lll")
        driver.find_element(By.NAME, "email2").click()
        driver.find_element(By.NAME, "email2").clear()
        driver.find_element(By.NAME, "email2").send_keys("mmm")
        driver.find_element(By.NAME, "email3").click()
        driver.find_element(By.NAME, "email3").clear()
        driver.find_element(By.NAME, "email3").send_keys("nnn")
        driver.find_element(By.NAME, "homepage").click()
        driver.find_element(By.NAME, "homepage").clear()
        driver.find_element(By.NAME, "homepage").send_keys("ooo")
        driver.find_element(By.NAME, "bday").click()
        Select(driver.find_element(By.NAME, "bday")).select_by_visible_text("10")
        driver.find_element(By.XPATH, "//option[@value='10']").click()
        driver.find_element(By.NAME, "bmonth").click()
        Select(driver.find_element(By.NAME, "bmonth")).select_by_visible_text("January")
        driver.find_element(By.XPATH, "//option[@value='January']").click()
        driver.find_element(By.NAME, "byear").click()
        driver.find_element(By.NAME, "byear").clear()
        driver.find_element(By.NAME, "byear").send_keys("2000")
        driver.find_element(By.NAME, "aday").click()
        Select(driver.find_element(By.NAME, "aday")).select_by_visible_text("5")
        driver.find_element(By.XPATH, "//div[@id='content']/form/select[3]/option[7]").click()
        driver.find_element(By.NAME, "amonth").click()
        Select(driver.find_element(By.NAME, "amonth")).select_by_visible_text("February")
        driver.find_element(By.XPATH, "//div[@id='content']/form/select[4]/option[3]").click()
        driver.find_element(By.NAME, "ayear").click()
        driver.find_element(By.NAME, "ayear").clear()
        driver.find_element(By.NAME, "ayear").send_keys("2010")
        driver.find_element(By.NAME, "address2").click()
        driver.find_element(By.NAME, "address2").clear()
        driver.find_element(By.NAME, "address2").send_keys("ppp")
        driver.find_element(By.NAME, "phone2").click()
        driver.find_element(By.NAME, "phone2").clear()
        driver.find_element(By.NAME, "phone2").send_keys("qqq")
        driver.find_element(By.NAME, "notes").click()
        driver.find_element(By.NAME, "notes").clear()
        driver.find_element(By.NAME, "notes").send_keys("rrr")
        driver.find_element(By.NAME, "theform").click()
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
