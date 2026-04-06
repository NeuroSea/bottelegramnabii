from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# ============================
# EDIT THESE DETAILS
# ============================
TOKEN = "8166122791:AAETIndnmyr5RohcdXrHWWxxPu92pJ5b8qY"
YOUR_USERNAME = "nabimaker"

CHANNEL_INFO = """
📊 *Trading Channel — Overview*

Welcome! Thank you for your interest in my trading channel. 🚀

━━━━━━━━━━━━━━━━━━━━
💼 *How does it work?*
━━━━━━━━━━━━━━━━━━━━
• Clear and precise trading signals
• Detailed technical analysis
• Full explanation for every signal
• Direct communication with the trader

━━━━━━━━━━━━━━━━━━━━
💰 *Payment Model*
━━━━━━━━━━━━━━━━━━━━
• *20% of generated profit* — you only pay when you win
• No fixed monthly subscription
• Transparent and fair

━━━━━━━━━━━━━━━━━━━━
📈 *Why join this channel?*
━━━━━━━━━━━━━━━━━━━━
• Minimal risk for you
• Shared interest — we win together
• Proven results

Tap the button below to speak with me directly! 👇
"""

FAQ = {
    "What markets do you trade?": "We trade *Forex, Crypto and Indices*. Every signal includes Entry, TP and SL.",
    "How is the 20% calculated?": "At the end of each month, we calculate the net profit generated from my signals. You pay 20% of that profit.",
    "What if I don't make a profit?": "No profit = no commission. Simple and fair. 🤝",
    "How do I receive the signals?": "Directly on Telegram, in real time, with full details: pair, direction, Entry, TP1, TP2, SL.",
}
# ============================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📋 Channel Info", callback_data="info")],
        [InlineKeyboardButton("❓ FAQ", callback_data="faq")],
        [InlineKeyboardButton("💬 Talk to the Trader", url=f"https://t.me/{YOUR_USERNAME}")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 *Welcome!*\n\nI'm the trading channel bot.\nChoose one of the options below:",
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        keyboard = [
            [InlineKeyboardButton("💬 Talk to the Trader", url=f"https://t.me/{YOUR_USERNAME}")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")],
        ]
        await query.edit_message_text(
            CHANNEL_INFO,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "faq":
        faq_text = "❓ *Frequently Asked Questions*\n\n"
        for question, answer in FAQ.items():
            faq_text += f"*• {question}*\n{answer}\n\n"

        keyboard = [
            [InlineKeyboardButton("💬 Talk to the Trader", url=f"https://t.me/{YOUR_USERNAME}")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")],
        ]
        await query.edit_message_text(
            faq_text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("📋 Channel Info", callback_data="info")],
            [InlineKeyboardButton("❓ FAQ", callback_data="faq")],
            [InlineKeyboardButton("💬 Talk to the Trader", url=f"https://t.me/{YOUR_USERNAME}")],
        ]
        await query.edit_message_text(
            "👋 *Welcome!*\n\nI'm the trading channel bot.\nChoose one of the options below:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💬 Talk to the Trader", url=f"https://t.me/{YOUR_USERNAME}")],
    ]
    await update.message.reply_text(
        "For any additional questions, speak directly with the trader! 👇",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))

print("✅ Bot is running...")
app.run_polling()
