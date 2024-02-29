import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Locators import Locators
from Config import Config
from Keywords.test_on_Navigation import  NavigationPage   
from Keywords.test_to_login_catalog import LoginCatalogPage
from Keywords.test_on_Adding import AdditionPage
from Keywords.test_on_Approve_Review import ReviewsPage
from Keywords.test_on_Deletion import DeletionPage
from Keywords.test_on_Download import ProductsPage
from Keywords.test_on_Excel import CategoriesPage
from Keywords.test_on_Searching import SearchPage 



@pytest.fixture
def chrome_browser():
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.mark.first
##--CATALOG--##
def test_Catalog(chrome_browser):
    chrome_browser.get(Locators.url)
    LoginCatalogPage(chrome_browser).navigate_to_main_page()

@pytest.mark.second
##--PRODUCTS--##
def test_to_Products(chrome_browser):  
    chrome_browser.get(Locators.url)
    NavigationPage(chrome_browser).navigate_to_products()
    AdditionPage(chrome_browser).add_new_product("Laptop")
    SearchPage(chrome_browser).search_Product("Laptop")
    ProductsPage(chrome_browser).download_products()
    CategoriesPage(chrome_browser).export_products_to_excel()
    DeletionPage(chrome_browser).select_and_delete_product()

##--CATEGORIES--##    
def test_to_Categories(chrome_browser):
    chrome_browser.get(Locators.url)
    NavigationPage(chrome_browser).navigate_to_categories()
    AdditionPage(chrome_browser).add_new_categories("ROM")
    SearchPage(chrome_browser).search_Categories("ROM")
    CategoriesPage(chrome_browser).export_categories_to_excel()
    DeletionPage(chrome_browser).select_and_delete_categories()

##--MANUFACTURERS--##
def test_to_Manufacturers(chrome_browser):
    chrome_browser.get(Locators.url)
    NavigationPage(chrome_browser).navigate_to_manufacturers()
    AdditionPage(chrome_browser).add_new_Manufacturer("Dell")
    SearchPage(chrome_browser).search_Manufacturers("Dell")
    CategoriesPage(chrome_browser).export_manufacturers_to_excel()
    DeletionPage(chrome_browser).select_and_delete_Manufacturers()

##--REVIEWS--##    
def test_to_reviews(chrome_browser):
    chrome_browser.get(Locators.url)
    NavigationPage(chrome_browser).navigate_to_reviews()
    SearchPage(chrome_browser).search_Reviews("03/13/2017")
    ReviewsPage(chrome_browser).approve_disapprove_review()
    DeletionPage(chrome_browser).select_and_delete_Reviews()

##--TAGS--##    
def test_to_Tags(chrome_browser):
    chrome_browser.get(Locators.url)
    Config.NavigationPage(chrome_browser).navigate_to_tags()
    Config.SearchPage(chrome_browser).search_Tags("awesome")
    Config.DeletionPage(chrome_browser).select_and_delete_Tags()

##--ATTRIBUTES--##    
def test_to_Attributes(chrome_browser):
    chrome_browser.get(Locators.url)
    NavigationPage(chrome_browser).navigate_to_attributes()

##--PRODUCT-ATTRIBUTES--##        
def test_to_Prod_Att(chrome_browser):
    chrome_browser.get(Locators.url)
    NavigationPage(chrome_browser).navigate_to_prod_Att()
    AdditionPage(chrome_browser).add_new_prod_att("ROM")
    DeletionPage(chrome_browser).select_and_delete_Prod_att()

##--SPECIFICATION-ATTRIBUTES--## 
def test_to_speci_att(chrome_browser):
    chrome_browser.get(Locators.url)
    NavigationPage(chrome_browser).navigate_to_speci_att()
    AdditionPage(chrome_browser).add_new_speci_att("RAM")
    DeletionPage(chrome_browser).select_and_delete_Speci_att()

##--CHECKOUT-ATTRIBUTES--## 
def test_to_Check_att(chrome_browser):
    chrome_browser.get(Locators.url)
    NavigationPage(chrome_browser).navigate_to_check_Att()
    AdditionPage(chrome_browser).add_new_check_att("ROM")
    DeletionPage(chrome_browser).select_and_delete_Check_att()
















    ##run only a particular test case pytest test_Main.py::test_Catalog ##