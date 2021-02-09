import requests
from flight_data import FlightData
import pprint

from datetime import datetime, timedelta

Tequila_Location_Endpoint = "https://tequila-api.kiwi.com/"
FLIGHT_KEY = "VKQs2BY4u3PFgziqSGgiwE8EuPE74l0p"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{Tequila_Location_Endpoint}/locations/query"
        headers = {"apikey": FLIGHT_KEY}
        params = {"term": city_name, "location_types": "airport", "limit": 1,}
        response = requests.get(url=location_endpoint, headers=headers, params=params)
        results = response.json()
        code = results["locations"][0]["city"]["code"]# <-- self.city_name? then put parameter in to main
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": FLIGHT_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(
            url=f"{Tequila_Location_Endpoint}v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data





# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(6*30))


# header = {"apikey": FLIGHT_KEY}

# query = {
#     "fly_from": "LON",
#     "fly_to": "FRA",
#     "date_from": "01/04/2021",
#     "date_to": "05/04/2021",
#     "nights_in_dst_from": 2,
#     "nights_in_dst_to": 3,
#     "flight_type": "round",
#     "one_for_city": 1,
#     "max_stopovers": 0,
#     "curr": "GBP",
# }

# response = requests.get(url=f"{Tequila_Location_Endpoint}v2/search", headers=header, params=query)

# data = response.json()["data"][0]

# print(data["price"])
# print(data["route"][0]["cityFrom"])
# data["route"][1]["local_departure"].spit("T")[0]
    