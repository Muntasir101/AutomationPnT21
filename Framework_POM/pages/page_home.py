# pages/home_page.py
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.my_account = (By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
        self.register = (By.LINK_TEXT, "Register")

    def navigate_to_registration(self):
        self.driver.find_element(*self.my_account).click()
        self.driver.find_element(*self.register).click()
