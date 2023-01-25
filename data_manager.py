import requests
from pprint import pprint
import os

SHEET_ENDPOINT = os.environ['SHEET_API']
SHEET_USERS_ENDPOINT = os.environ['SHEET_USERS_API']
TOKEN = os.environ['SHEETY_TOKEN']


sheet_headers = {
    'Authorization': f'Basic {TOKEN}'
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheet_data = {}
        self.customer_data = {}

    def get_data(self):
        data = requests.get(url=SHEET_ENDPOINT, headers=sheet_headers)
        self.sheet_data = data.json()['prices']
        # pprint(self.sheet_data)
        return self.sheet_data

    def update_destination_codes(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    'iataCode': city['iataCode']
                }
            }
            data = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", headers=sheet_headers, json=new_data)
            print(data.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEET_USERS_ENDPOINT, headers=sheet_headers)
        data = response.json()['users']
        self.customer_data = data
        return self.customer_data

