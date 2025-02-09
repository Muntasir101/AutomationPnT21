import pytest
from selenium import webdriver

# WebDriver fixture
@pytest.fixture(scope="function")
def driver():
    # Setup: initialize WebDriver
    driver = webdriver.Firefox()

    # Yield driver to the test
    yield driver

    # Teardown: quit WebDriver after the test
    driver.quit()
