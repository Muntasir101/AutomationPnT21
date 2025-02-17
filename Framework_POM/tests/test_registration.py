import json
from faker import Faker
from Framework_POM.pages.page_home import HomePage
from Framework_POM.pages.page_registration import RegistrationPage

fake = Faker()


def test_registration_valid(driver):
    # Generate a unique email and password
    unique_email = fake.email()
    password = "123456"

    # Save valid credentials to JSON file
    file_path = '../valid_credentials.json'
    with open(file_path, 'w') as json_file:
        json.dump({'email': unique_email, 'password': password}, json_file, indent=4)

    driver.get("https://tutorialsninja.com/demo/")

    home_page = HomePage(driver)
    home_page.navigate_to_registration()

    registration_page = RegistrationPage(driver)
    registration_page.fill_registration_form(unique_email, password)

    assert registration_page.get_success_message() == "Your Account Has Been Created!", "Registration failed !!"
    print("Test registration Passed!")