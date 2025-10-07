from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    # Home page URL and key elements
    URL = "https://useinsider.com/"
    CASE_STUDIES_BLOCK = (By.ID, "case-studies-home")
    COMPANY_MENU = (By.XPATH, "//a[contains(text(),'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(),'Careers')]")

    def load(self):
        self.open(self.URL)
        self.close_cookie_banner()

    # Close cookie banner if it appears
    def close_cookie_banner(self):
        try:
            self.driver.find_element(By.XPATH, "//button[contains(text(),'Accept All')]").click()
        except:
            pass
    # Navigate to Careers page
    def go_to_careers(self):
        self.click(self.COMPANY_MENU)
        self.click(self.CAREERS_LINK)

    # Verify that the Home page is opened by checking key elements
    def is_home_opened(self):
        # On main page load, check if the *case studies block* is visible
        return self.is_visible(self.CASE_STUDIES_BLOCK)
