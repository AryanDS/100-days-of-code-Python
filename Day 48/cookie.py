"""
Cookie project

"""
chrome_driver_path ="/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 48/chromedriver"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://secure-retreat-92358.herokuapp.com/")

cookie_button = driver.find_element(By.ID, 'cookie')
cookie_button.click()

while True:
    pass