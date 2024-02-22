from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class CategoriesPage:
    def __init__(self, driver):
        self.driver = driver
    
    def export_to_excel(self, export_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Export_hover))).click()
            
    ##--PRODUCTS--##
    def export_products_to_excel(self):
        self.export_to_excel(Locators.Export_Excel)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Export_Excel))).click()

    ##--CATEGORIES--##
    def export_categories_to_excel(self):
        self.export_to_excel(Locators.Export_Excel_Cat)
        self.driver.get(Locators.Export_Excel_Cat)

    ##--MANUFACTURERS--##
    def export_manufacturers_to_excel(self):
        self.export_to_excel(Locators.Export_Excel_Man)
        self.driver.get(Locators.Export_Excel_Man)
    # Add more methods as needed for other functionalities
