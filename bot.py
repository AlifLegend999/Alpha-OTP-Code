import os, requests, time
from telegram.ext import Updater, CommandHandler
from telegram import Update

# Get credentials from environment variables
TELEGRAM_TOKEN = os.getenv('8441226655:AAFhKpQw04D8yO0HA3zF1-ext0u39dukeHs')
FIVESIM_API_KEY = os.getenv('eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODU1MzU1NTgsImlhdCI6MTc1Mzk5OTU1OCwicmF5IjoiZmE3Y2ZlMzQ3ZDhhNDJjMDFhNzJkN2U0NzM0YWQ4MTAiLCJzdWIiOjMyNDU4MzV9.oxkAxDIcFdch_dp0w_6-wPyLK-gEtHdMaduYWS72c02Ijh6XXYQSRsHfjV9OCVRf5cycYoNW4xjRalTG1Addu2PjDcFFpJkWWsYgHsJjg8VuKW-FwT8-9EUjBvCsfL663KUN8nEsitIuTNPu5bc5eLWt2gHfA-LYe8P01MWv7-FjKqA-Oa6tNQro3jvg8A0blYZK0G6zY6Rcp5K0__A13nNXMcDT7GnTzPGLqWD3hPZLtXdusWQqdjYYz9ciGyPjfd6tS--l2vncEuoUq4c_F_rtMRyHwB1HSp8-uz2se8a3CfOJ4A4PM6BxV4BkCRhrZ_he2Aa0hUbL089CCocEUQ')
HEADERS = {'Authorization': f'Bearer {FIVESIM_API_KEY}'}

def start(update: Update, ctx):
    update.message.reply_text(
        "👋 Welcome to the OTP Bot!\n"
        "Use /buy [service] to get a number for supported platform.\n"
        "Example: /buy telegram"
    )

def buy(update: Update, ctx):
    if not ctx.args:
        return update.message.reply_text("⚠️ Please use: /Start Alpha Code")
    service = ctx.args[0].lower()
    try:
        res = requests.get(f"https://5sim.net/v1/user/buy/activation/any/any/{service}", headers=HEADERS)
        res.raise_for_status()
        data = res.json()
        num, oid = data['phone'], data['id']
        update.message.reply_text(f"📞 Number: {num}\n⏳ Waiting for OTP…", parse_mode='Markdown')
        for _ in range(30):
            time.sleep(3)
            chk = requests.get(f"https://5sim.net/v1/user/check/{oid}", headers=HEADERS).json()
            if chk.get('sms'):
                code = chk['sms'][0]['code']
                return update.message.reply_text(f"✅ OTP: `{code}`", parse_mode='Markdown')
        update.message.reply_text("⌛ Timeout: No OTP in 90 seconds.")
    except Exception as e:
        update.message.reply_text(f"❌ Error: {e}")

if __name__ == "__main__":
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("buy", buy))
    updater.start_polling()
    updater.idle()
