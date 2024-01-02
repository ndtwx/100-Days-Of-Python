import requests

URL = "https://api.agify.io"
URL_2 = "https://api.genderize.io"
params = {
    "name": "andy"
}

response = requests.get(url=URL, params=params)
response_2 = requests.get(url=URL_2, params=params)
response.raise_for_status()
data = response.json()
data_2 = response_2.json()
print(data)
print(data_2)
# print(data["name"])
print(data_2['gender'])
