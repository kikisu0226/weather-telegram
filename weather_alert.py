import os
import requests

LATITUDE = 25.0330
LONGITUDE = 121.5654

THRESHOLD = 30

def get_weather():
url = "https://api.open-meteo.com/v1/forecast"

```
params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "daily": "precipitation_probability_max,precipitation_sum",
    "timezone": "Asia/Taipei",
    "forecast_days": 1
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()

data = response.json()

date = data["daily"]["time"][0]

rain_probability = data["daily"][
    "precipitation_probability_max"
][0]

rain
```
