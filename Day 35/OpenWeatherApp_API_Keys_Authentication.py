import requests
from twilio.rest import Client

OWM_endpoint = "api.openweathermap.org/data/2.5/forecast"
account_sid = "AC10bcfdd036b5d3b94b02c9a3cc67f38b"
auth_token = "e5dbc253d46862a323f922cacaeeb45d"

parameters = {
    "lat": 1.372580,
    "lon": 103.893646,
    "cnt": 4,
    "appid": "3dd3eb982d3b816fdf8733a0f9d7f457",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
index = 0
weather_id = []
weather_data = response.json()

will_rain = False

# Loop through the weather id of each list
# if the weather id is less than 700, print "Bring Umbrella"
for hour_data in weather_data['list']:
    condition_code = (hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='It is going to rain! Remember to bring an umbrella',
        from_='whatsapp:+15185120543',
        to='whatsapp: Your verified number'
    )

    print(message.status)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure



