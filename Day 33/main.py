from ast import FormattedValue
from urllib import response
from pandas import reset_option
import requests as req
import datetime as dt

response = req.get(url="http://api.open-notify.org/iss-now.json")
#this will give us the response code. 200 success
print(response)

print(response.status_code)


"""
There are many response status code for which we can raise exceptions.
https://www.webfx.com/web-development/glossary/http-status-codes/
"""

if response.status_code == 404:
    raise Exception("The resource does not exists.")

elif response.status_code == 401:
    raise Exception("You are not authorised to use the data.")

"""
However it is impossible to create so many if statement for each exceptions 
To tackle this we would be using the python's requests module!
"""    
#below will raise an error in case it needs to.
response.raise_for_status()

# Getting json data from the API endpoint 

def iss_overhead():
        
    data = response.json()
    latitude =  float(response.json()["iss_position"]["latitude"])
    longitude = float(response.json()["iss_position"]["longitude"])
    if MY_LAT-5 <= latitude >= MY_LAT +5 and MY_LNG -5 <= longitude <= MY_LNG+5:
        return True 

"""
To see where in the world is the ISS,
goto: https://www.latlong.net/Show-Latitude-Longitude.html
"""


#######################
#Sunrise and Sunset 
MY_LAT = 42.886448
MY_LNG = -78.878372


response1 = req.get("https://api.sunrise-sunset.org/json")
response1.raise_for_status()
#Below worked without providing required parameters, lat lng
print(response1.json())

def is_night():
    #Providing the default parameters
    parameter ={
        "lat":MY_LAT,
        "lng":MY_LNG
    }

    res =  req.get("https://api.sunrise-sunset.org/json?formatted=0", params=parameter)
    res.raise_for_status()
    data= res.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    #Figuring out the current time in terms of hour 
    time_now =dt.datetime.now().hour
    if time_now >= sunset and time_now <= sunrise:
        return True 


"""
Putting the parameters into the URL:
https://www.latlong.net/c/?lat=42.886448&long=-78.878372
after '?' and to add another parameter use &
"""

    
#Now if the its night time and iss_overhead, then send an email 
import smtplib
if iss_overhead and is_night:
    email = "hiddenhills@gmail.com "
    password ="ola"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email , 
            to_addrs="helloworld@gmail.com", 
            msg=f"Subject:ISS Lookup! \n\n Please look up for the ISS "
            )

