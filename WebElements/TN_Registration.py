from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/")

my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
my_account.click()

register = driver.find_element(By.LINK_TEXT, "Register")
register.click()

first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
first_name.send_keys("Mr. John Doe")




