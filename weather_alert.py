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
rain_probability = data["daily"]["precipitation_probability_max"][0]
rain_amount = data["daily"]["precipitation_sum"][0]

return date, rain_probability, rain_amount
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
date, rain_probability, rain_amount = get_weather()

```
print(f"日期：{date}")
print(f"最高降雨機率：{rain_probability}%")
print(f"預測降雨量：{rain_amount} mm")

if rain_probability > THRESHOLD:
    message = (
        "☔ 今日下雨提醒！\n\n"
        f"📅 日期：{date}\n"
        f"🌧️ 最高降雨機率：{rain_probability}%\n"
        f"💧 預測降雨量：{rain_amount} mm\n\n"
        "⚠️ 今天下雨機率超過 30%，\n"
        "記得帶傘喔！☔"
    )

    send_telegram(message)

    print("Telegram 通知發送成功！")

else:
    print("降雨機率沒有超過 30%。")
    print("今天不發送 Telegram 通知。")
```

if **name** == "**main**":
main()

