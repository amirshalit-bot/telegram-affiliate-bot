import time
import schedule
from utils import load_products, send_affiliate_message

def post_affiliate_products():
    print("🚀 שולח מוצרים...")
    products = load_products()
    if not products:
        print("📭 אין מוצרים זמינים לשליחה.")
        return

    for product in products:
        send_affiliate_message(product)
        time.sleep(1)

post_affiliate_products()

schedule.every().day.at("00:00").do(post_affiliate_products)
schedule.every().day.at("03:00").do(post_affiliate_products)
schedule.every().day.at("06:00").do(post_affiliate_products)
schedule.every().day.at("09:00").do(post_affiliate_products)
schedule.every().day.at("12:00").do(post_affiliate_products)
schedule.every().day.at("15:00").do(post_affiliate_products)
schedule.every().day.at("18:00").do(post_affiliate_products)
schedule.every().day.at("21:00").do(post_affiliate_products)

print("🤖 הבוט פועל! ממתין לשליחות הקרובות...")

while True:
    schedule.run_pending()
    time.sleep(30)
