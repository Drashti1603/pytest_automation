from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators

class ReviewsPage:
    def __init__(self, driver):
        self.driver = driver
    
    def approve_disapprove_review(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Checkbox_Review))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Approve_Review))).click()


