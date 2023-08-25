import selenium
from selenium import webdriver
PATH = "/Users/bar2/Desktop"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://google.com/')
print("Chrome Browser Invoked")
driver.quit()
