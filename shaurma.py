from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# todo патерн билдер

heart_symbol = u"\u2764"
cheese_symbol = u"\U0001F9C0"
fitness_symbol = u"\U0001F3C3\u200D\u2642\uFE0F"
chicken_symbol = u"\U0001F357"
pekin_symbol = u"\U0001F96C"
burger_symbol = u"\U0001F354"


class shaurma:
    def __init__(self, name, additives, bot, message):
        self.name = name
        self.additives = additives

        markup = ReplyKeyboardMarkup(resize_keyboard=True)

        # markup.add(KeyboardButton(f"{pekin_symbol} шаурма Цезарь"))
        # markup.add(KeyboardButton(f"{chicken_symbol} шаурма Классическая"))
        # markup.add(KeyboardButton(f"{cheese_symbol} шаурма Сырная"))
        # markup.add(KeyboardButton(f"{fitness_symbol} шаурма Фитнес"))
        # markup.add(KeyboardButton(f"{burger_symbol} шаурма В булке"))

        markup.add(KeyboardButton(f"шаурма Цезарь {pekin_symbol}"))
        markup.add(KeyboardButton(f"шаурма Классическая {chicken_symbol}"))
        markup.add(KeyboardButton(f"шаурма Сырная {cheese_symbol}"))
        markup.add(KeyboardButton(f"шаурма Фитнес {fitness_symbol}"))
        markup.add(KeyboardButton(f"шаурма В булке {burger_symbol}"))

        bot.send_message(message.chat.id,
                         'Привет! Мы открыты каждый день с 9:00 до 1:00 по адресу Жемчужная, 34 к2 киоск.\n'
                         'Также у нас работает доставка с 9:00 до 1:00 в Яндекс Еде!')

        bot.send_message(message.chat.id, 'Перед Вами наше меню:')

        bot.send_message(message.chat.id, f'{pekin_symbol} шаурма Цезарь:\n'
                                          'лаваш, мясо, помидоры .... *ингредиенты*\n'
                                          'маленькая (150 рубллей/500 гр),\n'
                                          'средняя (175 рубллей/600 гр),\n'
                                          'большая (200 рубллей/700 гр)\n')

        bot.send_message(message.chat.id, f'{chicken_symbol} шаурма Классическая:\n'
                                          'лаваш, мясо, помидоры .... *ингредиенты*\n'
                                          'маленькая (150 рубллей/500 гр),\n'
                                          'средняя (175 рубллей/600 гр),\n'
                                          'большая (200 рубллей/700 гр)\n')

        bot.send_message(message.chat.id, f'{cheese_symbol} шаурма Сырная:\n'
                                          'лаваш, мясо, помидоры .... *ингредиенты*\n'
                                          'маленькая (150 рубллей/500 гр),\n'
                                          'средняя (175 рубллей/600 гр),\n'
                                          'большая (200 рубллей/700 гр)\n')

        bot.send_message(message.chat.id, f'{fitness_symbol} шаурма Фитнес:\n'
                                          'лаваш, мясо, помидоры .... *ингредиенты*\n'
                                          'маленькая (150 рубллей/500 гр),\n'
                                          'средняя (175 рубллей/600 гр),\n'
                                          'большая (200 рубллей/700 гр)\n')

        bot.send_message(message.chat.id, f'{burger_symbol} шаурма В булке:\n'
                                          'лаваш, мясо, помидоры .... *ингредиенты*\n'
                                          'маленькая (150 рубллей/500 гр),\n'
                                          'средняя (175 рубллей/600 гр),\n'
                                          'большая (200 рубллей/700 гр)\n')

        bot.send_message(message.chat.id, 'Выберите что хотите', reply_markup=markup)

    def __str__(self):
        sting = f"Шаурма: {self.name}\n" \
                f"Добавки: {self.additives}\n"
        return sting
