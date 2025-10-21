from telegram import ReplyKeyboardMarkup
def main_menu():
    keyboard = [["📅 Schedule", "📞 Contact"], ["❓ Help"]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
