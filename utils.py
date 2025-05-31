import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def load_products():
    products = []
    try:
        with open("products.csv", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("link"):
                    products.append(row)
    except Exception as e:
        print("❌ שגיאה בטעינת מוצרים:", e)
    return products

def send_affiliate_message(product):
    name = product.get("name", "מוצר ללא שם")
    features = product.get("features", "")
    rating = product.get("rating", "5")
    link = product.get("link", "#")
    deal_until = product.get("deal_until", "חצות בלבד!")

    message = f"""🔥 מוצר חם במיוחד!
{name} – {features}
📦 כולל מוזיקה + חימום + רטט | משלוח חינם
✅ דירוג: {'⭐'*int(float(rating))}

🔗 קנה עכשיו >> {link}

📉 מבצע עד {deal_until}!
"""

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        print(f"📤 סטטוס שליחה: {response.status_code}")
        print(response.text)
    except Exception as e:
        print("❌ שגיאה בשליחה לטלגרם:", e)
