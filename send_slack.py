import requests
import os
from dotenv import load_dotenv

load_dotenv()
SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL = "#test-api"

def send_message(channel, message):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }
    body = {
        "channel": channel,
        "text": message
    }
    response = requests.post(url, headers=headers, json=body)
    result = response.json()
    if result["ok"]:
        print("✅ メッセージを送信しました！")
        print(f"📢 チャンネル: {channel}")
        print(f"💬 メッセージ: {message}")
    else:
        print(f"❌ エラー: {result['error']}")

if __name__ == "__main__":
    send_message(CHANNEL, "Slack APIからのテストメッセージです！🚀")
