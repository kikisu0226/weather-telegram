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
    "daily": "precipitation_probability_max",
    "timezone": "Asia/Taipei",
    "forecast_days": 1
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()

data = response.json()

date = data["daily"]["time"][0]
rain_probability = data["daily"]["precipitation_probability_max"][0]

return date, rain_probability
```

def send_telegram(message):
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")

```
if not bot_token:
    raise ValueError("找不到 TELEGRAM_BOT_TOKEN")

if not chat_id:
    raise ValueError("找不到 TELEGRAM_CHAT_ID")

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

data = {
    "chat_id": chat_id,
    "text": message
}

response = requests.post(url, data=data, timeout=10)
response.raise_for_status()
```

def main():
print("開始取得天氣資料...")

```
date, rain_probability = get_weather()

print(f"日期：{date}")
print(f"最高降雨機率：{rain_probability}%")

message = (
    "☔ Telegram 測試成功！\n\n"
    f"日期：{date}\n"
    f"最高降雨機率：{rain_probability}%\n\n"
    "如果你收到這則訊息，代表 Telegram 設定成功！"
)

send_telegram(message)

print("Telegram 通知發送成功！")
```

if **name** == "**main**":
main()
