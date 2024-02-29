from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def search_item(self, search_locator, product_name, search_btn):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_locator))
        )
        search_input.click()
        search_input.send_keys(product_name)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, search_btn))).click()
       

    ##--PRODUCTS--##
    def search_Product(self, product_name):
        self.search_item(Locators.Search_Prod, product_name, Locators.Search_btn)

    ##--CATEGORIES--##
    def search_Categories(self, category_name):
        self.search_item(Locators.Search_Cat, category_name, Locators.Search_btn_Cat)

    ##--MANUFACTURERS--##
    def search_Manufacturers(self, category_name):
        self.search_item(Locators.Search_Man, category_name, Locators.Search_btn_Man)

    ##--REVIEWS--##
    def search_Reviews(self, category_name):
        self.search_item(Locators.Search_Review, category_name, Locators.Search_btn_Review)

    ##--TAGS--##           
    def search_Tags(self, category_name):
        self.search_item(Locators.Search_tags, category_name, Locators.Search_btn_tags)

    



