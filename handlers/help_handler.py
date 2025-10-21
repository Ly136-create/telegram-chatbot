from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/start - Start the bot\n/help - Show help")

help_handler = CommandHandler("help", help)