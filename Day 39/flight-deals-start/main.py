# #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# from data_manager import DataManager
# from flight_search import FlightSearch

# API_ENDNPOINT_SHEETY = "https://api.sheety.co/ee104b0ed113f19e4089a547163bd7e4/myFlightDeals/prices"
# API_ENDNPOINT_FLIGHTSEARCH = "https://tequila-api.kiwi.com/"

# #Creating a data_manager object
# data_m =  DataManager(API_ENDNPOINT_SHEETY)
# sheet_data = data_m.get_response()


# #Creating a FlightSearch object
# flight_search =  FlightSearch()


# for row in sheet_data:
#     if row['iataCode'] == '':
#         iatacode  = flight_search.iatacode(row['city'])
#         print(iatacode)
#         row['iataCode'] = iatacode
#     print(sheet_data)    


 
# #Passing the sheet_data into the data_manager class method
# data_m.put_request(sheet_data)
# print(sheet_data)



#############################
from data_manager import DataManager
from datetime import datetime,timedelta
from flight_search import FlightSearch


ORIGIN_CITY_IATA ="LON"
data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)
    
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )    