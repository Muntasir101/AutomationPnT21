from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_address = (By.CSS_SELECTOR, "#input-email")
        self.password = (By.CSS_SELECTOR, "#input-password")
        self.login_btn = (By.CSS_SELECTOR, "[action] .btn-primary")

    def fill_login_form(self, email, password):
        self.driver.find_element(*self.email_address).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()