from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators

class LoginCatalogPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_main_page(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Login_button_id))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Catalog_button_id))).click()
