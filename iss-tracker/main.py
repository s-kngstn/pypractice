import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def within_position(target_lat, target_long, my_lat, my_long):
    if target_lat in range(my_lat - 5, my_lat + 5) and target_long in range(my_long -5, my_long + 5):
        return True
    else:
        return False
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(f"lat {iss_latitude}, long {iss_longitude}")
#Your position is within +5 or -5 degrees of the ISS position.
iss_latitude = int(iss_latitude)
iss_longitude = int(iss_longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

my_lat = int(parameters["lat"])
my_long = int(parameters["lng"])

while True:
    time.sleep(60)
    if within_position(iss_latitude, iss_longitude, my_lat, my_long):
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        time_now = datetime.now()
        hour_now = time_now.hour

        my_email = "rooteduzr@gmail.com"
        passwd = "password_goes_here"
        message = "Look up! The ISS is overhead!"
        if hour_now not in range(sunrise, sunset):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=passwd)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="rooteduzr@gmail.com",
                    msg=f"Subject: Look up!\n\n{message}"
                )
        else:
            print("ISS is in position, but its too light outside to see it.")
    else:
        print("ISS is not in position.")




