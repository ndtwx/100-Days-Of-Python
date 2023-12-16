# https://pixe.la/
# https://docs.pixe.la/
import requests
# https://www.w3schools.com/python/python_datetime.asp
import datetime

USERNAME = "andylau"
TOKEN = "sjf93jt39sewerage9g3"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # Used to create user for first time user
# response= requests.post(url=pixela_endpoint, json=user_params)
# # Print the response to see if it success or not
# print(response.text)

# Used to create the graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# https://pixe.la/v1/users/andylau/graphs/graph1.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()

# Creating Request Body
pixeL_data = {
    "date": today.strftime("%Y%m%d"),  # Format the date to specify format
    "quantity": input("How many kilometers did you cycle today?: "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixeL_data, headers=headers)
print(response.text)

# # Delete specify pixel data
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
