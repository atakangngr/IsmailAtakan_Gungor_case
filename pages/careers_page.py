from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CareersPage(BasePage):

    # Close cookie banner if it appears
    def close_cookie_banner(self):
        try:
            self.driver.find_element(By.XPATH, "//button[contains(text(),'Accept All')]").click()
        except:
            pass
    
    
    # Variable elements to verify page load
    LOCATIONS_BLOCK = (By.XPATH, "//h3[contains(text(),'Our Locations')]")
    TEAMS_BLOCK = (By.XPATH, "//h3[contains(text(),'Find your calling')]")
    LIFE_BLOCK = (By.XPATH, "//h2[contains(text(),'Life at Insider')]")

    QA_PAGE_URL = "https://useinsider.com/careers/quality-assurance/"

    # Verify that the Careers page is opened by checking key elements
    def is_careers_opened(self):
        try:
            for block in [self.LOCATIONS_BLOCK, self.TEAMS_BLOCK, self.LIFE_BLOCK]:
                element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(block)
            )
            if not element.is_displayed():
                return False
            return True
        except TimeoutException:
            return False
    # Navigate to the QA Jobs page
    def go_to_qa_page(self):
        self.driver.get(self.QA_PAGE_URL)
