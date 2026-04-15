import os
import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

keyboard = [
    ["📊 Prices", "📈 Signals"],
    ["💼 Services", "🌐 Website"],
    ["📞 Support"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to COIN NODE\n\nPowering Smart Crypto Decisions.",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📊 Prices":
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd"
    
        data = requests.get(url).json()

        btc = data["bitcoin"]["usd"]
        eth = data["ethereum"]["usd"]
        usdt = data["tether"]["usd"]

    message = (
        f"📊 COIN NODE Live Prices\n\n"
        f"BTC: ${btc}\n"
        f"ETH: ${eth}\n"
        f"USDT: ${usdt}"
    )

    await update.message.reply_text(message)

    elif text == "📈 Signals":
        await update.message.reply_text("📈 BTC/USDT BUY\nTP: 67,500\nSL: 63,500")

    elif text == "💼 Services":
        await update.message.reply_text("💼 Trading • Investment • Account Management")

    elif text == "🌐 Website":
        await update.message.reply_text("https://horizonmarkets.co")

    elif text == "📞 Support":
        await update.message.reply_text("Contact support on Telegram")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
