from os import name

import telebot

bot = telebot.TeleBot("6002683883:AAEqKXMPxfe7Joa2UxwPs0uQceB1WycTQFw")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()