from selenium import webdriver
from selenium.webdriver.common.by import By
import json

def registration_valid():
    from faker import Faker
    fake = Faker()

    unique_email = fake.email()
    password = "123456"

    # Define the file path
    file_path = 'valid_credentials.json'

    data = {'email': unique_email,
            "password": password}

    # Write data to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    driver = webdriver.Firefox()

    driver.get("https://tutorialsninja.com/demo/")

    my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
    my_account.click()

    register = driver.find_element(By.LINK_TEXT, "Register")
    register.click()

    first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    first_name.send_keys(fake.name())

    last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    last_name.send_keys(fake.name())

    email = driver.find_element(By.CSS_SELECTOR, "#input-email")
    # email.send_keys("smith12@nomail.com")
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

    # Validate account registration or not
    expected_success_message = "Your Account Has Been Created!"
    actual_success_message = driver.find_element(By.CSS_SELECTOR, "#content h1").text
    assert expected_success_message == actual_success_message, f"Registration failed !!"

    print("Test registration Passed!")

    driver.quit()




