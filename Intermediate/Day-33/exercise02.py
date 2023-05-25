import requests
from datetime import datetime

MY_LAT = 59.436962
MY_LONG = 24.753574

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
time_now = datetime.now()
print(time_now)

print(sunrise, sunset)
