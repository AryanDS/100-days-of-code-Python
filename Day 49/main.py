"""
Creating a Linkedin bot which will automate the EASY APPLY job application
"""

chrome_driver_path ="/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 48/chromedriver"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import time 
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3203270693&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

USERNAME = "aryansaini117@gmail.com"
PASSWORD = "sudhirkumar"
PHONE  = "7169037801"

sign_in_button = driver.find_element(By.LINK_TEXT,"Sign in")

sign_in_button.click()

# Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(USERNAME)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)


time.sleep(5)
quick_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
quick_apply.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
# phone = driver.find_element(By.CSS_SELECTOR, "fb-single-line-text__input")
# if phone.text == "":
#     phone.send_keys(PHONE)

#Submit the application
submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()
while True:
    pass