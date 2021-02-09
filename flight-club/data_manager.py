import requests

Sheety_Prices_Endpoint = "https://api.sheety.co/5bfbc5d944fbd9bebc73be327905bd56/myFlightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}
    #This class is responsible for talking to the Google Sheet.
    
    def get_destination_data(self):
        response = requests.get(url=Sheety_Prices_Endpoint)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }

            response = requests.put(
                url=f"{Sheety_Prices_Endpoint}/{city['id']}", 
                json=new_data
            )

            print(response.text)