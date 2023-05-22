import telebot
import random

bot = telebot.TeleBot('BotToken')
import datetime
file = open('list.txt', encoding='utf-8', mode='r')
data = file.read()
data = data.replace('\n', '')
data = data.split('***')
data.pop(0)
data.pop(33)
data.pop(132)
lst = data

def autopost():
    message = random.choice(lst)
    chat_id = "@Channel"
    bot.send_message(chat_id, message)

import schedule
import time

schedule.every(20).minutes.do(autopost) # Запускаем функцию автопостинга каждый день в 12:00.

while True:
    schedule.run_pending()
    time.sleep(1)

