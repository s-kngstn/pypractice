import requests

NAME = "Gladys"

parameters = {
    "name": NAME,
}

age_res = requests.get("https://api.agify.io/", params=parameters)
gender_res = requests.get("https://api.genderize.io/", params=parameters)

age = age_res.json()['age']
gender = gender_res.json()['gender']

print(age, gender)