from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.CSS_SELECTOR, "#input-firstname")
        self.last_name = (By.CSS_SELECTOR, "#input-lastname")
        self.email = (By.CSS_SELECTOR, "#input-email")
        self.telephone = (By.CSS_SELECTOR, "#input-telephone")
        self.password = (By.CSS_SELECTOR, "#input-password")
        self.password_confirm = (By.CSS_SELECTOR, "#input-confirm")
        self.privacy_policy = (By.CSS_SELECTOR, "input[name='agree']")
        self.continue_btn = (By.CSS_SELECTOR, "input[value='Continue']")
        self.success_message = (By.CSS_SELECTOR, "#content h1")

    def fill_registration_form(self, unique_email, password):
        self.driver.find_element(*self.first_name).send_keys(fake.first_name())
        self.driver.find_element(*self.last_name).send_keys(fake.last_name())
        self.driver.find_element(*self.email).send_keys(unique_email)
        self.driver.find_element(*self.telephone).send_keys("12345678")
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.password_confirm).send_keys(password)
        self.driver.find_element(*self.privacy_policy).click()
        self.driver.find_element(*self.continue_btn).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text