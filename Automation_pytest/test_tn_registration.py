import json
from faker import Faker
from selenium.webdriver.common.by import By

fake = Faker()

def test_registration_valid(driver):
    # Generate a unique email and password
    unique_email = fake.email()
    password = "123456"

    # Define the file path
    file_path = 'valid_credentials.json'

    # Write data to the JSON file
    data = {'email': unique_email,
            "password": password}

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    driver.get("https://tutorialsninja.com/demo/")

    # Navigate to registration page
    my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
    my_account.click()

    register = driver.find_element(By.LINK_TEXT, "Register")
    register.click()

    # Fill in registration form
    first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    first_name.send_keys(fake.name())

    last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    last_name.send_keys(fake.name())

    email = driver.find_element(By.CSS_SELECTOR, "#input-email")
    email.send_keys(unique_email)

    telephone = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
    telephone.send_keys("12345678")

    password_input = driver.find_element(By.CSS_SELECTOR, "#input-password")
    password_input.send_keys(password)

    password_confirm = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    password_confirm.send_keys(password)

    privacy_policy = driver.find_element(By.CSS_SELECTOR, "input[name='agree']")
    privacy_policy.click()

    continue_btn = driver.find_element(By.CSS_SELECTOR, "input[value='Continue']")
    continue_btn.click()

    # Validate account registration
    expected_success_message = "Your Account Has Been Created!"
    actual_success_message = driver.find_element(By.CSS_SELECTOR, "#content h1").text
    assert expected_success_message == actual_success_message, f"Registration failed !!"

    print("Test registration Passed!")
