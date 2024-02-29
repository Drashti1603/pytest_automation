import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Locators import Locators
from selenium.webdriver.common.by import By
from Keywords.test_on_Navigation import NavigationPage


@pytest.fixture

def test_login(chrome_browser):
    chrome_browser.get(Locators.url)
    chrome_browser.implicitly_wait(5)  # Use chrome_browser instead of driver
    login_button = chrome_browser.find_element(By.XPATH, Locators.Login_button_id)
    login_button.click()
    chrome_browser.save_screenshot("/home/drashti/Documents/Android_Automation/python/pytest/Tests/Web/Results/Login.png")
