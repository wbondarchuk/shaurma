from PyQt5 import QtWidgets, uic
import sys

from threading import Thread

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

import telebot
import shaurma
import time

# todo init
token = '5278878177:AAFD_eYJ39E3mBH-8Nv6lCF5v4KTbakBF0o'
bot = telebot.TeleBot(token)
cur = 0
finished = False
order_list = []
to_do = []
vidacha = []

heart_symbol = u"\u2764"
cheese_symbol = u"\U0001F9C0"
fitness_symbol = u"\U0001F3C3\u200D\u2642\uFE0F"
chicken_symbol = u"\U0001F357"
pekin_symbol = u"\U0001F96C"
burger_symbol = u"\U0001F354"
cucumber_symbol = u"\U0001F952"
peper_symbol = u"\U0001F336"
bread_symbol = u"\U0001F35E"
fries_symbol = u"\U0001F35F"
tomato_symbol = u"\U0001F345"
fire_symbol = u"\U0001F525"
pineapple_symbol = u"\U0001F34D"
corn_symbol = u"\U0001F33D"


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

    markup.add(KeyboardButton(f"добавка сыр {cheese_symbol}"))
    markup.add(KeyboardButton(f"добавка мясо {chicken_symbol}"))
    markup.add(KeyboardButton(f"добавка огурцы {cucumber_symbol}"))
    markup.add(KeyboardButton(f"добавка халапеньо {peper_symbol}"))
    markup.add(KeyboardButton(f"добавка сухарики {bread_symbol}"))
    markup.add(KeyboardButton(f"добавка помидоры {tomato_symbol}"))
    markup.add(KeyboardButton(f"добавка картофель фри {fries_symbol}"))
    markup.add(KeyboardButton(f"добавка кукурза {corn_symbol}"))
    markup.add(KeyboardButton(f"добавка ананас {pineapple_symbol}"))
    markup.add(KeyboardButton(f"добавка соус острый {fire_symbol}"))
    markup.add(KeyboardButton("/finish"))

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
        order_list.append(shaurma.shaurma(1, [], bot, message))
    print(order_list[0].name, "Добавки:")
    for additive in order_list[0].additives:
        print(additive, end=" ")
    print()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton("да"))
    markup.add(KeyboardButton("нет"))

    bot.send_message(message.chat.id, f"Ваша шаурма: {order_list[0].name}\n"
                                      f"Ваши добавки: {order_list[0].additives}\n"
                                      f"Ждём Вас по адресу Жемчужная, 34 к2 киоск!\n" \
                                      f"Приятного аппетита! Приходите ещё!")

    bot.send_message(message.chat.id, 'Подтвердить заказ?', reply_markup=markup)


@bot.message_handler(content_types='text')
def choice_shaurma(message):
    if len(order_list) == 0:
        order_list.append(shaurma.shaurma(1, [], bot, message))
    global cur
    # todo Устойчивость к поломке(преждевременного завершения)(можно ещё задание на предотвращение левых добавок) - Тимур, Алексей
    if len(message.text) != 0:
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

            item, name = message.text.split()[:-1]
            if item == "шаурма":
                order_list[0].name = name
                choice_additives(message)
            if item == "добавка":
                order_list[0].additives.append(name)

    else:
        bot.send_message(message.chat.id, 'Жду ответ!')


thread = Thread(target=scanorder, daemon=True)
thread.start()

thread_bot = Thread(target=bot.infinity_polling, daemon=True)
thread_bot.start()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
thread_update = Thread(target=window.update, daemon=True)
thread_update.start()
app.exec_()
