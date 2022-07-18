# import requests as req


# API_ENDNPOINT_SHEETY = "https://api.sheety.co/ee104b0ed113f19e4089a547163bd7e4/myFlightDeals/prices"

# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
    
#     def __init__(self, API_ENDPOINT):
#         self.api = API_ENDPOINT

#     def get_response(self):
#         self.response =  req.get(url=self.api)   
#         self.response_data = self.response.json()
#         return self.response_data['prices']

#     def put_request(self, sheet_data):
#         for row in sheet_data:
#             row_id = row['id']
#             put_dict = {
#                  "price": {
#                     "iataCode": row["iataCode"]
#                 }
#             }
#             response = req.put(url=f"{self.api}/{row_id}", json = put_dict)
#             print(response.text)
            
       


#########################################
from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ee104b0ed113f19e4089a547163bd7e4/myFlightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint().
        # pprint(data)
        return self.destination_data


    # 6. In the DataManager Class make a PUT request and use the row id  from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)