from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'

# Set path to Chromedriver executable
chromedriver_path = '/usr/bin/chromedriver'

# Create a Chromedriver service
service = webdriver.ChromeService(executable_path=chromedriver_path)

# Initialize Chromedriver with the service and options
driver = webdriver.Chrome(service=service, options=options)
