import requests
import os

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

headers = {
    "Authorization": f"Bearer {TOKEN}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.users_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)

    def get_users_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        data = response.json()
        self.users_data = data["users"]
        return self.users_data
