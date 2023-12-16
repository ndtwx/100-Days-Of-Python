import requests
import datetime
import os
from pprint import pprint

sheet_endpoint = "https://api.sheety.co/fd06d92c96d48f638e9fd66de8e8af9c/flightDeals/prices"
bearer_headers = {
            "Authorization": "Bearer iwanttoflyhighlikeasohai"
        }
class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}


    def get_destination_data(self):
        response = requests.get(url=sheet_endpoint, headers=bearer_headers)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheet_endpoint}/{city['id']}",json=new_data,headers=bearer_headers)
            print(response.text)
