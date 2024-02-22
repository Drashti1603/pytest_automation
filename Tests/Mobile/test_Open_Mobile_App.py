import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def chrome_browser():
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_open_website(chrome_browser):
    chrome_browser.get("https://admin-demo.nopcommerce.com/Admin")
    chrome_browser.maximize_window()
    screenshot_path = '/home/drashti/Documents/Android_Automation/robot-files/Web_Automation/Robot_Files/Nopcommerce_Automation/Results/Web/Open.png'
    chrome_browser.save_screenshot(screenshot_path)
    # You can add assertions or further verifications here if needed
