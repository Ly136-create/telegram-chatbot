from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from handlers.start_handler import start_handler
from handlers.help_handler import help_handler
from handlers.message_handler import message_handler

app = ApplicationBuilder().token(BOT_TOKEN).build()

#Add all handlers
app.add_handlers(start_handler)
app.add_handlers(help_handler)
app.add_handlers(message_handler)

print("🤖 SmartBot is running...")
app.run_polling()