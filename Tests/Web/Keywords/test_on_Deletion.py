from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class DeletionPage:
    def __init__(self, driver):
        self.driver = driver
        
    def select_and_delete_item(self, checkbox_locator,need_confirmation):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox_locator))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Delete_Selected))).click()
        
        if need_confirmation:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.yes))).click()

    ##--PRODUCTS--##
    def select_and_delete_product(self):
        self.select_and_delete_item(Locators.Checkbox,  need_confirmation=False)

    ##--CATEGORIES--##
    def select_and_delete_categories(self):
        self.select_and_delete_item(Locators.Checkbox_cat,  need_confirmation=False)

    ##--MANUFACTURERS--##    
    def select_and_delete_Manufacturers(self):
        self.select_and_delete_item(Locators.Checkbox_Man,  need_confirmation=False)

    ##--REVIEWS--##
    def select_and_delete_Reviews(self):
        self.select_and_delete_item(Locators.Checkbox_Review, need_confirmation=True)

    ##--TAGS--##
    def select_and_delete_Tags(self):
        self.select_and_delete_item(Locators.Checkbox_Tags,  need_confirmation=False)

    ##--PRODUCT-ATTRIBUTES--##
    def select_and_delete_Prod_att(self):
        self.select_and_delete_item(Locators.Checkbox_pa, need_confirmation=True)

    ##--SPECIFICATION-ATTRIBUTES--##
    def select_and_delete_Speci_att(self):
        Grp_Hover = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.Grp_Hover))
        )
        Grp_Hover.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Checkbox_sa))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.Delete_Selected_Sa))).click()
        yes_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Locators.yes_sa))
        )
        yes_button.click()    

    ##--CHECKOUT-ATTRIBUTES--##
    def select_and_delete_Check_att(self):
        self.select_and_delete_item(Locators.Checkbox_Ca, need_confirmation=True)

    




    
  