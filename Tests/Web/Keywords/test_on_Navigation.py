import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators
from Keywords.test_to_login_catalog import LoginCatalogPage

class NavigationPage:
    def __init__(self, driver):
        self.driver = driver

    ##--PRODUCTS--##
    def navigate_to_products(self):
        login_page = LoginCatalogPage(self.driver)
        login_page.navigate_to_main_page()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locators.Product_button_id))).click()
        self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Web", "Results", "Products.png"))

    ##--CATEGORIES--##
    def navigate_to_categories(self):
        login_page = LoginCatalogPage(self.driver)        
        login_page.navigate_to_main_page()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Categories_button_id))).click()
        self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Web", "Results", "Categories.png"))

    ##--MANUFACTURERS--##    
    def navigate_to_manufacturers(self):
        login_page = LoginCatalogPage(self.driver)
        login_page.navigate_to_main_page()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Manufacturers_button_id))).click()
        self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Web", "Results", "Manufacturers.png"))

    ##--REVIEWS--##    
    def navigate_to_reviews(self):
        login_page = LoginCatalogPage(self.driver)
        login_page.navigate_to_main_page()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Reviews_button_id))).click()
        self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Web", "Results", "Reviews.png"))

    ##--TAGS--##    
    def navigate_to_tags(self):
        login_page = LoginCatalogPage(self.driver)
        login_page.navigate_to_main_page()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Tags_button_id))).click()
        self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Web", "Results", "Tags.png"))

    ##--ATTRIBUTES--##        
    def navigate_to_attributes(self):
        login_page = LoginCatalogPage(self.driver)
        login_page.navigate_to_main_page()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Attributes))).click()
        self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Web", "Results", "Attributes.png"))

    ##--PRODUCT-ATTRIBUTES--##
    def navigate_to_prod_Att(self):
        login_page = LoginCatalogPage(self.driver)
        login_page.navigate_to_main_page()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Attributes))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Product_att))).click()
        self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Web", "Results", "Product_att.png"))

    ##--SPECIFICATION-ATTRIBUTES--##
    def navigate_to_speci_att(self):
            login_page = LoginCatalogPage(self.driver)
            login_page.navigate_to_main_page()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Attributes))).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Specification_att))).click()
            self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Web", "Results", "Specification_att.png"))

    ##--CHECKOUT-ATTRIBUTES--##
    def navigate_to_check_Att(self):
        login_page = LoginCatalogPage(self.driver)
        login_page.navigate_to_main_page()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Attributes))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Checkout_att))).click()
        self.driver.save_screenshot(os.path.join(os.getcwd(), "Tests", "Web", "Results", "Checkout.png"))

    

 