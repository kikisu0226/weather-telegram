import os
import requests

THRESHOLD = 30
if True:
    message = (
        "☔ Telegram 測試成功！\n\n"
        f"日期：{date}\n"
        f"最高降雨機率：{rain_probability}%\n\n"
        "如果你看到這則訊息，代表 Telegram 設定成功！"
    )

    send_telegram(message)
    print("Telegram 通知發送成功！")
