import telebot
from telebot import types
from parser import parser
from bot import config


api_key = config.token


joke_bot = telebot.TeleBot(api_key)

@joke_bot.message_handler(commands=["Joke"])
@joke_bot.message_handler(commands=["joke"])




def hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Анекдот")
    markup.add(btn1)
    joke_bot.send_message(message.chat.id, "Joke готов к работе,нажми кнопку : ", reply_markup=markup)




@joke_bot.message_handler(content_types=["text"])

def jokes(message):
    if message.text == "Анекдот":
        joke_bot.send_message(message.chat.id, parser.clear_list_joke[0])
        del parser.clear_list_joke[0]
    else:
        joke_bot.send_message(message.chat.id, "Вы ошиблись с цифрой?")


