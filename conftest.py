import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Create a fixture to initialize and quit the WebDriver
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()
