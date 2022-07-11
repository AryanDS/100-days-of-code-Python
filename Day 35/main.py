import requests as req
from twilio.rest import Client


account_sid = "AC6b271361dcc327aea75cfc9c168f4eee"
auth_token = "474e23f5182bbbf8f6d899424f5d97a0"

api_key="38ecb78bf0ffefe69ad8b36668a5feeb"

# response =  req.get("https://api.openweathermap.org/data/2.5/onecall?lat=42.886448&lon=-78.878372&appid=39661e776365451bc003ca4ec317ad4e")
# response.raise_for_status()
# #Below worked without providing required parameters, lat lng
# weather_data = response.json()


#Above method is not working, throwing 401 error
owm_endpoint="https://api.openweathermap.org/data/2.5/onecall"
parameter={
    "lat":42.886448,
    "lon":-78.878372,
    "appid":api_key
}

response = req.get(owm_endpoint, params=parameter)
response.raise_for_status()
#Below worked without providing required parameters, lat lng
weather_data = response.json()
#slicing the data to get 12 hours data
sliced_data = weather_data['hourly'][:12]
print(sliced_data)
#print(weather_data["hourly"][0]['weather'])

will_rain=False

for hour_data in sliced_data:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain=True

#Setting will_rain to true so that the text message would be triggered, 
#Could've changed the lattitude and longitude of a place where it is RAINING!
will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              body='Hi there!, It is probably going to rain today!',
                              from_='+13168006176',
                              to='+17169037801'
                          )        
    print(message.status)                          