from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.keyboards import main_menu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to SmartBot 🤖!", reply_markup=main_menu())

start_handler = CommandHandler("start", start)   