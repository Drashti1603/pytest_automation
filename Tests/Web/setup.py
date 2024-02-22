from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)
