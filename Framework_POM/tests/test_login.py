import json
import os

from faker import Faker
from Framework_POM.pages.page_home import HomePage
from Framework_POM.pages.page_login import LoginPage

def test_login_valid(driver):
    # Load the email from the user.json file
    file_path = '../valid_credentials.json'

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        email = data["email"],
        password = data["password"]

    home_page = HomePage(driver)
    home_page.navigate_to_login()

    login_page = LoginPage(driver)
    login_page.fill_login_form(email, password)

    # Save screenshot after test
    screenshot_path = os.path.join("screenshots", "test_login.png")
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    driver.save_screenshot(screenshot_path)