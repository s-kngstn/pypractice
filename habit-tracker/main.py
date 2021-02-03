#Advanced Authentication Methods & POST / PUT / DELETE Requests

# HTTP Requests
# Get, Post, Put, Delete

# 'Get' Request is made where we ask an external system for a particular piece of data and they give that to 
# us in a response.

# 'Post' Request is where WE give the external system a piece of data and we are not so interested in
# the response we are getting back other than if it was successful or not.
# An example of this is we could use the twitter API to post a tweet, my program would send the data through a 
# 'Post' request.

# 'Put' Request is where you simply update a piece of data in the exernal service. So for example if you had a 
# spreadsheet in Google Sheets and maybe you wanted to update some of the values in the spreadsheet then you would
# use a 'Put' request.

# 'Delete' Reqest is where you would want to delete a piece of data in the external service. Like removing a 
# tweet that you posted or a reddit post.
import requests
from datetime import datetime

USERNAME = "skngstn"
TOKEN = "sh2fdn2ff3da7e2dn31qo9s"
GRAPH_ID = "graph1"
QUANTITY = "2.0"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USER_PARAMS = {
    "token": "sh2fdn2ff3da7e2dn31qo9s",
    "username": "skngstn",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response.text)
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "hour",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": QUANTITY,
}

# repsonse = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
# print(repsonse.text)
date_change = "20200202"

UPDATE_ENDPOINT = f"{PIXEL_ENDPOINT}/{date_change}"

new_pixel_data = {
    "quantity": QUANTITY,
}

# response = requests.put(url=UPDATE_ENDPOINT, json=new_pixel_data, headers=headers)
# print(response.text) 
DELETE_ENDPOINT = f"{PIXEL_ENDPOINT}/{date_change}"

response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(response.text)





