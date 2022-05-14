from PyQt5 import QtWidgets, uic
import sys

from email import message
from threading import Thread

from telebot.types import ReplyKeyboardMarkup, KeyboardButton


import telebot
import shaurma
import  time

# todo init
token = '2097318317:AAE-6SFnxE8TOzRP6kG6iPKssa-UV_fIDQg'
bot = telebot.TeleBot(token)
cur = 0
finished = False
order_list = []
to_do = []
vidacha = []

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.show()
        self.ol.clicked.connect(self.from_ol_in_vl)
        self.vl.clicked.connect(self.from_vl)

    def from_ol_in_vl(self):
        num_sh = int(self.editTodo.text())
        vidacha.append(to_do[num_sh - 1])
        del to_do[num_sh - 1]


    def from_vl(self):
        num_sh = int(self.editV.text())
        del vidacha[num_sh - 1]

    def update(self):
        while True:
            self.listOrder.clear()
            for order in to_do:
                self.listOrder.addItem(str(order))
            self.listV.clear()
            for order in vidacha:
                self.listV.addItem(str(order))
            time.sleep(1)



# todo перенести все методы
@bot.message_handler(commands=['start'])
def button_message(message):
    if len(order_list) == 0:
        order_list.append(shaurma.shaurma(1, [], bot, message))

def choice_additives(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = KeyboardButton("добавка сыр")
    item2 = KeyboardButton("добавка мясо")
    item3 = KeyboardButton("добавка огурцы")
    item5 = KeyboardButton("добавка халапеньо")
    item6 = KeyboardButton("добавка сухарики")
    item7 = KeyboardButton("добавка помидоры")
    item8 = KeyboardButton("добавка картофель фри")
    item9 = KeyboardButton("добавка кукурза")
    item10 = KeyboardButton("добавка ананас")
    item11 = KeyboardButton("добавка соус острый")
    item12 = KeyboardButton("/finish")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item5)
    markup.add(item6)
    markup.add(item7)
    markup.add(item8)
    markup.add(item9)
    markup.add(item10)
    markup.add(item11)
    markup.add(item12)
    bot.send_message(message.chat.id, 'Выберите что добавить', reply_markup=markup)

def scanorder():
    while True:
        w = input()
        if w == "do":
            num_sh = int(input())
            vidacha.append(to_do[num_sh - 1])
            del to_do[num_sh - 1]
        if w == "done":
            num_sh = int(input())
            del vidacha[num_sh - 1]
        elif w == "ol":
            for i in range(len(to_do)):
                additive1 = "Добавки: "
                print("Номер заказа: ", i + 1)
                print("Название шаурмы: ", to_do[i].name)
                for additive in to_do[i].additives:
                    additive1 += additive + "; "
                print(additive1)
        elif w == "vl":
            for i in range(len(vidacha)):
                additive1 = "Добавки: "
                print("Номер заказа: ", i + 1)
                print("Название шаурмы: ", vidacha[i].name)
                for additive in vidacha[i].additives:
                    additive1 += additive + "; "
                print(additive1)


@bot.message_handler(commands=['finish'])
def final(message):
    if len(order_list) == 0:
        order_list.append(shaurma.shaurma(1, [], bot,message))
    print(order_list[0].name, "Добавки:")
    for additive in order_list[0].additives:
        print(additive, end=" ")
    print()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    item9 = KeyboardButton("да")
    item10 = KeyboardButton("нет")
    markup.add(item9)
    markup.add(item10)
    bot.send_message(message.chat.id,f"Ваша шаурма: {order_list[0].name}")
    bot.send_message(message.chat.id, f"Ваши добавки: {order_list[0].additives}")
    bot.send_message(message.chat.id, 'Подтвердить заказ?', reply_markup=markup)


@bot.message_handler(content_types='text')
def choice_shaurma(message):
    if len(order_list) == 0:
        order_list.append(shaurma.shaurma(1, [], bot,message))
    global cur
    #todo Устойчивость к поломке(преждевременного завершения)(можно ещё задание на предотвращение левых добавок) - Тимур, Алексей
    if message.text == "да":
        print("Заказ принят")
        to_do.append(order_list[0])
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        item10 = KeyboardButton("/start")
        markup.add(item10)
        bot.send_message(message.chat.id, 'Сделать ешё 1 заказ?', reply_markup=markup)
        del order_list[0]
    elif message.text == "нет":
        print("Заказ отменён")
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        item10 = KeyboardButton("/start")
        markup.add(item10)
        bot.send_message(message.chat.id, 'Сделать заказ?', reply_markup=markup)
        del order_list[0]
    else:
        if message.text[0:6] == "шаурма":
            type, name = message.text.split()
            order_list[0].name = name
            choice_additives(message)
        if message.text[0:7] == "добавка":
            type, name = message.text.split()
            order_list[0].additives.append(name)
thread = Thread(target=scanorder, daemon=True)
thread.start()


thread_bot = Thread(target=bot.infinity_polling, daemon=True)
thread_bot.start()
app = QtWidgets.QApplication(sys.argv)
window = Ui()
thread_update = Thread(target=window.update, daemon=True)
thread_update.start()
app.exec_()