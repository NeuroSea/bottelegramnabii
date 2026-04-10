from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# ============================
# DETALII BOT
# ============================
TOKEN = "8166122791:AAETIndnmyr5RohcdXrHWWxxPu92pJ5b8qY"
YOUR_USERNAME = "neb1trades"

CHANNEL_INFO = """
📊 *Canal de Trading — Prezentare*

Bun venit! Îți mulțumesc că ești interesat de canalul meu de trading. 🚀

━━━━━━━━━━━━━━━━━━━━
💼 *Cum funcționează?*
━━━━━━━━━━━━━━━━━━━━
• Semnale de trading clare și precise
• Analize tehnice detaliate
• Explicație completă pentru fiecare semnal
• Comunicare directă cu traderul

━━━━━━━━━━━━━━━━━━━━
💰 *Model de plată*
━━━━━━━━━━━━━━━━━━━━
• *20% din profitul generat* — plătești doar când câștigi
• Fără abonament fix lunar
• Transparent și corect

━━━━━━━━━━━━━━━━━━━━
📈 *De ce să te alături?*
━━━━━━━━━━━━━━━━━━━━
• Risc minim pentru tine
• Interes comun — câștigăm împreună
• Rezultate dovedite

Apasă butonul de mai jos pentru a vorbi direct cu mine! 👇
"""

FAQ = {
    "Ce piețe tranzacționați?": "Tranzacționăm *Forex, Crypto și Indici*. Fiecare semnal include Entry, TP și SL.",
    "Cum se calculează cei 20%?": "La sfârșitul fiecărei luni calculăm profitul net generat din semnalele mele. Plătești 20% din acel profit.",
    "Dacă nu fac profit, plătesc ceva?": "Fără profit = fără comision. Simplu și corect. 🤝",
    "Cum primesc semnalele?": "Direct pe Telegram, în timp real, cu toate detaliile: pereche, direcție, Entry, TP1, TP2, SL.",
}
# ============================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📋 Informații canal", callback_data="info")],
        [InlineKeyboardButton("❓ Întrebări frecvente", callback_data="faq")],
        [InlineKeyboardButton("🚀 Intră în grup", url="https://t.me/+6P7Pj3dKKrJkNTZk")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 *Bun venit!*\n\nSunt botul canalului de trading.\nAlege una din opțiunile de mai jos:",
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        keyboard = [
            [InlineKeyboardButton("🚀 Intră în grup", url="https://t.me/+6P7Pj3dKKrJkNTZk")],
            [InlineKeyboardButton("🔙 Înapoi", callback_data="back")],
        ]
        await query.edit_message_text(
            CHANNEL_INFO,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "faq":
        faq_text = "❓ *Întrebări frecvente*\n\n"
        for question, answer in FAQ.items():
            faq_text += f"*• {question}*\n{answer}\n\n"

        keyboard = [
            [InlineKeyboardButton("🚀 Intră în grup", url="https://t.me/+6P7Pj3dKKrJkNTZk")],
            [InlineKeyboardButton("🔙 Înapoi", callback_data="back")],
        ]
        await query.edit_message_text(
            faq_text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("📋 Informații canal", callback_data="info")],
            [InlineKeyboardButton("❓ Întrebări frecvente", callback_data="faq")],
            [InlineKeyboardButton("🚀 Intră în grup", url="https://t.me/+6P7Pj3dKKrJkNTZk")],
        ]
        await query.edit_message_text(
            "👋 *Bun venit!*\n\nSunt botul canalului de trading.\nAlege una din opțiunile de mai jos:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Intră în grup", url="https://t.me/+6P7Pj3dKKrJkNTZk")],
    ]
    await update.message.reply_text(
        "Pentru orice întrebare suplimentară, vorbește direct cu traderul! 👇",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))

print("✅ Botul rulează...")
app.run_polling()
