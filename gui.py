from PyQt5 import QtWidgets, uic
import sys
from threading import Thread
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

import telebot
import shaurma
token = '2097318317:AAE-6SFnxE8TOzRP6kG6iPKssa-UV_fIDQg'
bot = telebot.TeleBot(token)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.show()

class TelegramBot:
    def __init__(self):
        self.cur = 0
        self.finished = False
        self.order_list = []
        self.to_do = []
        self.vidacha = []

    @bot.message_handler(commands=['start'])
    def button_message(self,message):
        if len(self.order_list) == 0:
            self.order_list.append(shaurma.shaurma(1, [], bot, message))

    def choice_additives(self, message):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = KeyboardButton("добавка сыр")
        item2 = KeyboardButton("добавка мясо")
        item3 = KeyboardButton("добавка огурцы")
        item4 = KeyboardButton("добавка морковь")
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
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)
        markup.add(item8)
        markup.add(item9)
        markup.add(item10)
        markup.add(item11)
        markup.add(item12)
        bot.send_message(message.chat.id, 'Выберите что добавить', reply_markup=markup)

    def scanorder(self):
        while True:
            w = input()
            if w == "done":
                num_sh = int(input())
                self.vidacha.append(self.to_do[num_sh - 1])
                del self.to_do[num_sh - 1]
            if w == "del":
                num_sh = int(input())
                del self.vidacha[num_sh - 1]
            elif w == "ol":
                for i in range(len(self.to_do)):
                    additive1 = "Добавки: "
                    print("Номер заказа: ", i + 1)
                    print("Название шаурмы: ", self.to_do[i].name)
                    for additive in self.to_do[i].additives:
                        additive1 += additive + "; "
                    print(additive1)
            elif w == "tl":
                for i in range(len(self.vidacha)):
                    additive1 = "Добавки: "
                    print("Номер заказа: ", i + 1)
                    print("Название шаурмы: ", self.vidacha[i].name)
                    for additive in self.vidacha[i].additives:
                        additive1 += additive + "; "
                    print(additive1)
            else:
                print("Комнда не найдена")

    @bot.message_handler(commands=['finish'])
    def final(self, message):
        if len(self.order_list) == 0:
            self.order_list.append(shaurma.shaurma(1, [], bot, message))
        print(self.order_list[0].name, "Добавки:")
        for additive in self.order_list[0].additives:
            print(additive, end=" ")
        print()
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        item9 = KeyboardButton("да")
        item10 = KeyboardButton("нет")
        markup.add(item9)
        markup.add(item10)
        bot.send_message(message.chat.id, f"Ваша шаурма: {self.order_list[0].name}")
        bot.send_message(message.chat.id, f"Ваши добавки: {self.order_list[0].additives}")
        bot.send_message(message.chat.id, 'Подтвердить заказ?', reply_markup=markup)

    @bot.message_handler(content_types='text')
    def choice_shaurma(self,message):
        if len(self.order_list) == 0:
            self.order_list.append(shaurma.shaurma(1, [], bot,message))
        global cur
        #todo Устойчивость к поломке(преждевременного завершения)(можно ещё задание на предотвращение левых добавок) - Тимур, Алексей
        if message.text == "да":
            print("Заказ принят")
            self.to_do.append(self.order_list[0])
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            item10 = KeyboardButton("/start")
            markup.add(item10)
            bot.send_message(message.chat.id, 'Сделать ешё 1 заказ?', reply_markup=markup)
            del self.order_list[0]
        elif message.text == "нет":
            print("Заказ отменён")
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            item10 = KeyboardButton("/start")
            markup.add(item10)
            bot.send_message(message.chat.id, 'Сделать заказ?', reply_markup=markup)
            del self.order_list[0]
        else:
            if message.text[0:6] == "шаурма":
                type, name = message.text.split()
                self.order_list[0].name = name
                self.choice_additives(message)
            if message.text[0:7] == "добавка":
                type, name = message.text.split()
                self.order_list[0].additives.append(name)


t = TelegramBot()
thread = Thread(target=t.scanorder, daemon=True)
thread.start()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
