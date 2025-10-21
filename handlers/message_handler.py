from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.messange.reply_text(f"You said: {user_text}")


message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message)