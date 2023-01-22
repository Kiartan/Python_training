from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init and create group
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # edit
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        # update and return
        wd.find_element(By.NAME, "update").click()
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()
