"""
Web scraping the wikipidia page
"""
chrome_driver_path ="/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 48/chromedriver"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element("name", "fName")
first_name.send_keys("Aryan ")
last_name = driver.find_element("name", "lName")
last_name.send_keys("Saini ")
email = driver.find_element("name", "email")
email.send_keys("asai@gmail.com ")


submit = driver.find_element(By.CSS_SELECTOR, "button")
submit.click()

while(True):
    pass
# XPATH ='//*[@id="articlecount"]/a[1]'

# num_articles = driver.find_element(By.XPATH, XPATH)
# print(num_articles.text)


# #Using CSS selectors
# num_articles1 = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# print(num_articles1.tag_name)
# #If we want to click on the hyperlink without clicking it then 
# num_articles1.click()

# # #find element by link
# # all_portals = driver.find_element(By.LINK_TEXT, "All Portals")

# # #finding the search bar
# search = driver.find_element("name", "search")
# search.send_keys("Python")


# # #To close the website 
driver.close()