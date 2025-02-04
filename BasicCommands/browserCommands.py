from selenium import webdriver

#driver1 = webdriver.Firefox()
#driver2 = webdriver.Chrome()
#driver3 = webdriver.Edge()

driver = webdriver.Chrome()

#driver.maximize_window()

#driver.set_window_size(712, 1138)

driver.get("https://google.com")

"""
# verification by title
expected_title = "Google"
actual_title = driver.title

if actual_title == expected_title:
    print("Title Matched. Google Open Successfully")
else:
    print("Another/Wrong page open !!")

# verification by URl
expected_url = "https://www.google.com/"
actual_url = driver.current_url

if actual_url == expected_url:
    print("URl Matched. Google Open Success")
else:
    print("Another/Wrong page open")
"""

# Verify the title
expected_title = "Google"
actual_title = driver.title
assert expected_title in actual_title, f"Title verification failed. Expected: {expected_title}, but got: {actual_title}"

# Verify the URL
expected_url = "https://www.google.com/"
actual_url = driver.current_url
assert expected_url == actual_url, f"URL verification failed. Expected: {expected_url}, but got: {actual_url}"

print("Title and URL verification passed!")

#driver.close()

#driver.quit()