import os
import requests

LATITUDE = 25.0330
LONGITUDE = 121.5654
THRESHOLD = 30

def get_weather():
url = "https://api.open-meteo.com/v1/forecast"
print("Open-Meteo URL:", url)
return True

print("Python 程式開始執行")
get_weather()


```
url = f"https://api.telegram.org/bot{token}/sendMessage"

data = {
    "chat_id": chat_id,
    "text": message
}

response = requests.post(
    url,
    data=data,
    timeout=10
)

response.raise_for_status()
```

def main():
date, rain_probability = get_rain_probability()

```
print(f"日期：{date}")
print(f"今日最高降雨機率：{rain_probability}%")

if rain_probability > THRESHOLD:

    message = (
        "☔ 下雨提醒！\n\n"
        f"日期：{date}\n"
        f"今日最高降雨機率：{rain_probability}%\n\n"
        "降雨機率超過 30%，記得帶傘喔！☔"
    )

    send_telegram(message)

    print("Telegram 通知已發送！")

else:
    print("降雨機率未超過 30%，不發送通知。")
```

if **name** == "**main**":
main()


