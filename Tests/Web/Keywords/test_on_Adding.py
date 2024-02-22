from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class AdditionPage:
    def __init__(self, driver):
        self.driver = driver
    def enter_product_details(self, product_name):
        prod_name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.Prod_name))
        )
        prod_name_input.click()
        prod_name_input.send_keys(product_name) 
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.Save))
        )
        save_button.click()

    ##--PRODUCTS--##
    def add_new_product(self, product_name):
        self.driver.get(Locators.Add_new_p)
        self.enter_product_details(product_name)

    ##--CATEGORIES--##
    def add_new_categories(self, category_name):
        self.driver.get(Locators.Add_new_Cat)
        self.enter_product_details(category_name)

    ##--MANUFACTURERS--##
    def add_new_Manufacturer(self, category_name):
        self.driver.get(Locators.Add_new_Man)
        self.enter_product_details(category_name)
    
    

    ##--PRODUCT-ATTRIBUTES--##
    def add_new_prod_att(self, category_name):
        self.driver.get(Locators.Add_new_pa)
        self.enter_product_details(category_name)

    ##--SPECIFICATION-ATTRIBUTES--##   
    def add_new_speci_att(self, category_name):
        self.driver.get(Locators.Add_new_sa)
        self.enter_product_details(category_name)

    ##--CHECKOUT-ATTRIBUTES--##
    def add_new_check_att(self, category_name):
        self.driver.get(Locators.Add_new_Ca)
        self.enter_product_details(category_name)

    
