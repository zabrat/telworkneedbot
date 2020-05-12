# -*- coding: utf-8 -*-
import telebot
from telebot import types

bot = telebot.TeleBot("1091648816:AAE5Pw1kF6GPY46rKKukLU8r7TUN_ffOa_M")

@bot.message_handler(commands=["start"])
def who(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    button_worker = types.KeyboardButton(text="Нужна работа")
    button_boss= types.KeyboardButton(text="Есть работа")
    keyboard.add(button_worker, button_boss)
    bot.send_message(message.chat.id, "Что хотели?", reply_markup=keyboard)
bot.polling(none_stop=True)
