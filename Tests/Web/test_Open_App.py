import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Locators import Locators
from Keywords.test_on_Navigation import NavigationPage

@pytest.fixture

def chrome_browser():
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    yield driver

def test_open_website(chrome_browser):
    chrome_browser.get(Locators.url)
    chrome_browser.maximize_window()
    screenshot_path = '/home/drashti/Documents/Android_Automation/python/pytest/Tests/Web/Results/Open.png'
    chrome_browser.save_screenshot(screenshot_path)
