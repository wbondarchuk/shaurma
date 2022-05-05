from PyQt5 import QtWidgets, uic
import sys

from email import message
from threading import Thread
import order
import telebot
import shaurma
from telebot import types

order_list = []
token = '2097318317:AAE-6SFnxE8TOzRP6kG6iPKssa-UV_fIDQg'
bot = telebot.TeleBot(token)
cur = order.order("1", [])


@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("шаурма 1")
    item2 = types.KeyboardButton("шаурма 2")
    item3 = types.KeyboardButton("шаурма 3")
    item4 = types.KeyboardButton("шаурма 4")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    bot.send_message(message.chat.id, 'Выберите что хотите', reply_markup=markup)
    # choice_shaurma(message)


@bot.message_handler(content_types='text')
def choice_shaurma(message):
    global cur
    if message.text == "/finish":
        name = 0
        print("шаурма заказана")
        order_list.append(cur)
        print(f"ret code {name}")
    else:
        type, name = message.text.split()
        if type == "шаурма":
            cur = order.order(name,[])
            choice_additives(message)
        if type == "добавка":
            cur.add.append(name)




def choice_additives(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item5 = types.KeyboardButton("добавка 1")
    item6 = types.KeyboardButton("добавка 2")
    item7 = types.KeyboardButton("добавка 3")
    item8 = types.KeyboardButton("добавка 4")
    markup.add(item5)
    markup.add(item6)
    markup.add(item7)
    markup.add(item8)
    bot.send_message(message.chat.id, 'Выберите что добавить', reply_markup=markup)


def preservation(message):
    if message.text == "добавка 1":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("добавка 1")
        markup.add(item1)
        choice_additives(message)
        order.append("добавка 1")
        final(message)
    elif message.text == "добавка 2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("добавка 2")
        markup.add(item2)
        choice_additives(message)
        order.append(" добавка 2")
        final(message)
    elif message.text == "добавка 3":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("добавка 3")
        markup.add(item2)
        choice_additives(message)
        order.append(" добавка 3")
        final(message)
    elif message.text == "добавка 4":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("добавка 4")
        markup.add(item2)
        choice_additives(message)
        order.append(" добавка 4")
        final(message)


def scanorder():
    while True:
        w = input('Введите команду')
        if w == "list":
            for i in range(len(order_list)):
                print(i + 1, ":",order_list[i].text,"Добавки:")
                for add in order_list[i].add:
                    print(add,end=" ")
                print("")
        if w == "del":
            num_sh = int(input())
            del order_list[num_sh - 1]


def final(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, 'Подтвердить заказ?')
    item9 = types.KeyboardButton("да")
    item10 = types.KeyboardButton("нет")
    markup.add(item9)
    markup.add(item10)
    bot.send_message(message.chat.id, 'Выберите что хотите', reply_markup=markup)


thread = Thread(target=scanorder, daemon=True)
thread.start()

bot.infinity_polling()
