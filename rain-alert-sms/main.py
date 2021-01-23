import requests
from twilio.rest import Client

API_KEY = "9634d26a0b6a64137351a2e33df482c9"
account_sid = "ACac835b04475cdd448438da6dd732b99b"
auth_token = "d469e9e45bca81f551eab6238dccc4b7"
MY_LAT = 50.110924
MY_LNG = 8.682127
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(OMW_Endpoint,
                        params=parameters)
response.raise_for_status()
data = response.json()

num = 0
weather_list = []
for weather in range(0, 12):
    weather_id = data["hourly"][num]["weather"][0]["id"]
    num += 1
    weather_list.append(weather_id)

rain_list = [ID for ID in weather_list if ID < 700]

if len(rain_list) > 0:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Bring an umbrella, its going to rain today",
                     from_="+17344186562",
                     to="+4407538313413"
                 )

    print(message.status)
    print("Bring an umbrella")
else:
    print("Its not going to rain today")


