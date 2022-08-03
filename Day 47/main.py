"""
Price tracker amazon 
"""
import requests
from bs4 import BeautifulSoup
import smtplib

URL= "https://www.amazon.com/dp/B09V3JJT5D"

response = requests.get("https://www.amazon.com/dp/B09V3JJT5D", headers={"Accept-Language":'en-GB,en-US;q=0.9,en;q=0.8',"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
#print(response.text)

#Creating a beautiful soup object
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())
title = soup.title.string

#Gathering the price of the items using soup 

price = soup.find(name="span", class_="a-offscreen")
price = price.string.split("$")[1]


# if float(price) < 500:
#My email credentials 
email = "aryansaini117@gmail.com "
password ="xvfqmdlrqwusdhji"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email , 
        to_addrs="aryansaini117@gmail.com", 
        msg=f"Subject:Amazon IPad Price alert\n\n {title} is now available at {price} LINK: {URL}"
        )



    


