from email import header
import requests as req
from datetime import datetime

pixela_endpoint="https://pixe.la/v1/users"
USERNAME= "asaini2"
TOKEN= "afgg2ngin2sf"

user_params={

    "token":"afgg2ngin2sf",
    "username": "asaini2",
    "agreeTermsOfService": "yes",
    'notMinor':"yes"
}


# response = req.post(url= pixela_endpoint, json=user_params)
# #Below will return the text from the response.
# print(response.text)

"""
After creating the username we comment out the above code since username is created and we can access their API service
"""

#Creating a graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id": "graphcode1",
    "name":"CodingTracker Graph",
    "unit": "Hours",
    'type': "float",
    "color": "ajisai"
    }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = req.post(url=graph_endpoint, json=graph_config, headers =  headers) 
# print(response.text)



#Adding a pixel to the graph using API POST
pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

"""
Below will convert the datetime.now into any format we want using the strftime() stringftime method
"""

today = datetime(year = 2022, month = 7, day=13 )
today = today.strftime("%Y%m%d")

pixel_config={
    "date": f"{today}",
    "quantity": "5"
}

# response = req.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)


"""
Using the PUT request here which is used to update information done by the POST
"""

update_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today}"

update_config={
    "quantity": "2.4"
}

response =  req.put(url=update_endpoint, json=update_config, headers=headers)
print(response.text)


"""
Using the DELETE request we will delete a pixel using the delete()
"""

delete_endpoint = update_endpoint

response = req.delete(url=delete_endpoint, headers=headers)
print(response.text)