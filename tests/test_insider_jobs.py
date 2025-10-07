import sys
import os
import pytest
# Adding the parent directory to sys.path to access the pages module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage

from selenium.webdriver.common.by import By

# Test function to validate the job application flow
def test_insider_job_flow(driver):
    home = HomePage(driver)
    home.load()
    home.close_cookie_banner()
    assert home.is_home_opened(), "Home page did not load correctly"

    home.go_to_careers()
    careers = CareersPage(driver)
    careers.close_cookie_banner()
    assert careers.is_careers_opened(), "Careers page did not load correctly"

    careers.go_to_qa_page()
    qa_page = QAJobsPage(driver)
    qa_page.click_see_all_jobs()
    qa_page.filter_jobs()
    assert qa_page.get_job_count() > 0, "No jobs found after filtering"
    assert "Quality Assurance" in qa_page.check_jobs_details()[0], "Job title does not match"
    assert "Istanbul, Turkiye" in qa_page.check_jobs_details()[1], "Job location does not match"
    qa_page.click_view_role()
    assert "lever.co" in qa_page.driver.current_url, "Did not navigate to job detail page"
