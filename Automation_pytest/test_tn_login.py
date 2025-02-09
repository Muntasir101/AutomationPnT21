from selenium import webdriver
from selenium.webdriver.common.by import By
import json

def login_valid(driver):
    # Load the email from the user.json file
    file_path = 'valid_credentials.json'

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        email = data["email"],
        password = data["password"]


    driver.get("https://tutorialsninja.com/demo/")

    my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
    my_account.click()

    login = driver.find_element(By.LINK_TEXT, "Login")
    login.click()

    email_input = driver.find_element(By.CSS_SELECTOR, "#input-email")
    email_input.send_keys(email)

    password_input = driver.find_element(By.CSS_SELECTOR, "#input-password")
    password_input.send_keys(password)

    login_btn = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
    login_btn.click()

    # Validate Login or not
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/account"
    actual_url = driver.current_url
    assert expected_url == actual_url, f"Login failed !!"

    print("Test Login Passed!")

    logout = driver.find_element(By.CSS_SELECTOR, ".list-group .list-group-item:nth-of-type(13)")
    logout.click()




