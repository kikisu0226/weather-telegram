import os
import requests

# ==========================================

# 1. 設定地點

# ==========================================

# 台北市

LATITUDE = 25.0330
LONGITUDE = 121.5654

# ==========================================

# 2. 降雨機率通知門檻

# ==========================================

# 降雨機率超過 30% 就發送 Telegram 通知

THRESHOLD = 30

# ==========================================

# 3. 從 Open-Meteo 取得天氣資料

# ==========================================

def get_weather():

```
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "daily": "precipitation_probability_max",
    "timezone": "Asia/Taipei",
    "forecast_days": 1
}

response = requests.get(
    url,
    params=params,
    timeout=10
)

# 確認 API 是否正常
response.raise_for_status()

data = response.json()

# 今天日期
date = data["daily"]["time"][0]

# 今天最高降雨機率
rain_probability = data["daily"]["precipitation_probability_max"][0]

return date, rain_probability
```

# ==========================================

# 4. 傳送 Telegram 訊息

# ==========================================

def send_telegram(message):

```
# 從環境變數取得 Telegram Token
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")

# 從環境變數取得 Telegram Chat ID
chat_id = os.environ.get("TELEGRAM_CHAT_ID")

# 確認 Token
if not bot_token:
    raise ValueError("找不到 TELEGRAM_BOT_TOKEN")

# 確認 Chat ID
if not chat_id:
    raise ValueError("找不到 TELEGRAM_CHAT_ID")

# Telegram Bot API
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

data = {
    "chat_id": chat_id,
    "text": message
}

response = requests.post(
    url,
    data=data,
    timeout=10
)

# 確認 Telegram 是否成功
response.raise_for_status()
```

# ==========================================

# 5. 主程式

# ==========================================

def main():

```
print("================================")
print("🌧️ 今日降雨機率偵測系統")
print("================================")

# 取得天氣
date, rain_probability = get_weather()

print(f"日期：{date}")
print(f"今日最高降雨機率：{rain_probability}%")
print(f"通知門檻：{THRESHOLD}%")


# ======================================
# 判斷降雨機率
# ======================================

if rain_probability > THRESHOLD:

    print("⚠️ 降雨機率超過 30%")
    print("正在傳送 Telegram 通知...")

    message = (
        "☔ 今日下雨提醒！\n\n"
        f"📅 日期：{date}\n"
        f"🌧️ 最高降雨機率：{rain_probability}%\n\n"
        "⚠️ 今天下雨機率較高，\n"
        "記得帶傘喔！☔"
    )

    # 傳送 Telegram
    send_telegram(message)

    print("✅ Telegram 通知發送成功！")

else:

    print("✅ 降雨機率沒有超過 30%")
    print("今天不需要傳送 Telegram 通知。")
```

# ==========================================

# 6. 執行

# ==========================================

if **name** == "**main**":
main()

