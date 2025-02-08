from selenium import webdriver
from selenium.webdriver.common.by import By

from faker import Faker
fake = Faker()

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
#email.send_keys("smith12@nomail.com")
email.send_keys(fake.email())

telephone = driver.find_element(By.CSS_SELECTOR,"#input-telephone")
telephone.send_keys("12345678")

password = driver.find_element(By.CSS_SELECTOR,"#input-password")
password.send_keys("123456")

password_confirm = driver.find_element(By.CSS_SELECTOR,"#input-confirm")
password_confirm.send_keys("123456")

privacy_policy = driver.find_element(By.CSS_SELECTOR,"input[name='agree']")
privacy_policy.click()

continue_btn = driver.find_element(By.CSS_SELECTOR,"input[value='Continue']")
continue_btn.click()

# Validate account registration or not
expected_success_message = "Your Account Has Been Created!"
actual_success_message = driver.find_element(By.CSS_SELECTOR,"#content h1").text
assert expected_success_message == actual_success_message, f"Registration failed !!"

print("Test registration Passed!")

driver.quit()




