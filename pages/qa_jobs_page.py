import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pages.base_page import BasePage

class QAJobsPage(BasePage):

    # Buttons & Dropdowns
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//a[contains(@href,'department=qualityassurance') and text()='See all QA jobs']")
    LOCATION_SPAN = (By.XPATH, "//span[@aria-labelledby='select2-filter-by-location-container']")
    DEPARTMENT_SPAN = (By.XPATH, "//span[@aria-labelledby='select2-filter-by-department-container']")
    LOCATION_OPTION = "//li[contains(text(),'{location}')]"
    # DEPARTMENT_OPTION = "//li[contains(text(),'{department}')]" # Not used in the current implementation

    # Jobs list & buttons
    # JOB_LIST = (By.XPATH, "//div[contains(@class,'job-item')]") # Not used in the current implementation
    VIEW_ROLE_BUTTON = (By.XPATH, "(//a[contains(text(),'View Role')])[1]")  # First job
    JOB_CARD = (By.CSS_SELECTOR, "div.position-list-item") # First job card

    # Cookie banner
    COOKIE_BANNER_CLOSE = (By.XPATH, "//div[contains(@class,'cli-close')]")

    ### Methods ###
    # Close cookie banner if it appears
    def close_cookie_banner(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.COOKIE_BANNER_CLOSE)
            ).click()
        except:
            pass 

    # Wait for page to load and close cookie banner
    def open_page_and_wait(self, url):
        self.driver.get(url)
        time.sleep(5)
        self.close_cookie_banner()

    # Click "See all QA jobs" button
    def click_see_all_jobs(self):
        element = self.driver.find_element(*self.SEE_ALL_QA_JOBS_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    # Filter jobs by location and department
    def filter_jobs(self, location="Istanbul, Turkiye", department="Quality Assurance"):

        # Wait for job listings to load
        time.sleep(5)
        # Find the filter element and scroll into view
        filter_element = self.driver.find_element(*self.LOCATION_SPAN)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", filter_element
        )
        time.sleep(5)
        # Open the location dropdown
        # Wait for the dropdown to be clickable 
        location_span_xpath = "(//span[@class='selection'])"
        location_span = WebDriverWait(self.driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, location_span_xpath))
        )
        
        # Find and click the location span to open the dropdown
        location_span.click()
        time.sleep(5)

        ### 
        # 
        # Istanbul, Turkiye is the 11th option in the list. The index may change if options are added/removed.
        #
        ###

        first_option_xpath = "//ul[@id='select2-filter-by-location-results']/li[contains(@class,'select2-results__option')][11]"
        first_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, first_option_xpath))
        )

        # Click the first option
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", first_option)
        time.sleep(2)  # Wait a bit after scrolling
        first_option.click()
        time.sleep(5)  # Wait for the page to refresh with filtered results

    def get_jobs(self):
        time.sleep(5)  # Wait for jobs to load
        job_elements = self.driver.find_elements(By.CSS_SELECTOR, "#deneme")
        return job_elements
    
    def get_job_count(self):
        # Get the count of job listings after filtering
        jobs = self.get_jobs()
        return len(jobs)
    
    def check_jobs_details(self):
        # Check the job's title and location
        job_detail_title = self.driver.find_elements(By.CSS_SELECTOR, "span.position-department.text-large.font-weight-600.text-primary")[0].text
        job_detail_location = self.driver.find_elements(By.CSS_SELECTOR, "div.position-location.text-large")[0].text
        jobs = [job_detail_title, job_detail_location]
        return jobs
    
    def click_view_role(self):
        # Find the job card and its "View Role" button
        job_card_element = self.driver.find_element(*self.JOB_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", job_card_element)
        time.sleep(2) # Wait a bit after scrolling
        view_role_button = self.driver.find_element(*self.VIEW_ROLE_BUTTON)
        # Make sure the button is clickable
        actions = ActionChains(self.driver)
        actions.move_to_element(job_card_element).pause(0.5).move_to_element(view_role_button).click().perform()
        # Wait for the new tab to open
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        # Navigate to the new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # Check the URL of the new tab
        new_tab_url = self.driver.current_url
        #print("New tab URL:", new_tab_url)
