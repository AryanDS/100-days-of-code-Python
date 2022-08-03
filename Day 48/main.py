"""
Selenium 
"""
chrome_driver_path ="/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 48/chromedriver"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Creating a chrome webdriver object
#Below is the method that we need to use the webdrive in which we pass the service object!
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Opening amazon website using selenium 

driver.get("https://www.python.org/")
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)


#finding elements using CSS selector 
# documentation_link =  driver.find_element(By.CSS_SELECTOR, '')
# print(documentation_link.text)


#Finding element by using XPATH
# documentation_link =  driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
# print(documentation_link.text)






##########################################
#Challenge 


dict1 ={}
#getting the dates
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget  time ')
for i in range(len(event_times)):
    event_times[i] = event_times[i].text


#getting the description of the events
events = driver.find_elements(By.CSS_SELECTOR, '.event-widget  a ')
for i in range(len(events)):
    events[i] = events[i].text


#we need to remove the first element from the list 
events.pop(0)


#creating the required dictionary 

for i in range(len(event_times)):
    dict1[i]={
        "time": event_times[i],
        "name": events[i]
    }

# dict1[i]['time']   = event_times[i]
# dict1[i]['name']   = events[i]

print(dict1)

#To close the website 
# driver.close()

#below will close the entire browser in case we have multiple tabs open 
#driver.quit()



