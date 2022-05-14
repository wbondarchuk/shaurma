from telebot import types
#todo патерн билдер
class shaurma:
    def __init__(self, name, additives,bot,message):
        self.name = name
        self.additives = additives
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("шаурма Цезарь")
        item2 = types.KeyboardButton("шаурма Классическая")
        item3 = types.KeyboardButton("шаурма Сырная")
        item4 = types.KeyboardButton("шаурма Фитнес")
        item5 = types.KeyboardButton("шаурма В булке")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(message.chat.id, 'Выберите что хотите', reply_markup=markup)
        # choice_shaurma(message)

    def __str__(self):
        sting = f"Ваша шаурма: {self.name} " + f"Ваши добавки: {self.additives}"
        return sting

