from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//form[@action='/addressbook/addressbook/group.php']").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init and create group
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # edit
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        # update and return
        wd.find_element(By.NAME, "update").click()
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()
