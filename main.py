import telebot
from telebot import types

# Указываем токен (не забудьте заменить на ваш токен)
bot = telebot.TeleBot('токен')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, сейчас я покажу тебе мой каталог.")
        keyboard = types.InlineKeyboardMarkup()

        key_Tri = types.InlineKeyboardButton(text='ТРЕУГОЛЬНИК', callback_data='triangle')
        keyboard.add(key_Tri)
        key_PrKv = types.InlineKeyboardButton(text='ПРЯМОУГОЛЬНИК И КВАДРАТ', callback_data='geometry')
        keyboard.add(key_PrKv)
        key_Ok = types.InlineKeyboardButton(text='ОКРУЖНОСТЬ', callback_data='Circle')
        keyboard.add(key_Ok)
        key_Pr = types.InlineKeyboardButton(text='ПРЯМАЯ', callback_data='Straight')
        keyboard.add(key_Pr)
        key_Yg = types.InlineKeyboardButton(text='УГОЛ', callback_data='Corner')
        keyboard.add(key_Yg)

        bot.send_message(message.from_user.id, text='Выбери нужную фигуру', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "geometry":
        msg = "Сейчас я ОЛЕГ покажу, что я знаю о прямоугольнике и квадрате."

        keyboard = types.InlineKeyboardMarkup()
        key_PrKv_Pr = types.InlineKeyboardButton(text='ПРЯМОУГОЛЬНИК', callback_data='Rectangle')
        keyboard.add(key_PrKv_Pr)
        key_PrKv_Kv = types.InlineKeyboardButton(text='КВАДРАТ', callback_data='Square')
        keyboard.add(key_PrKv_Kv)

        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери нужную фигуру:", reply_markup=keyboard)

    elif call.data == "Rectangle":
        bot.send_message(call.message.chat.id, "Это информация о прямоугольнике...")
    elif call.data == "Square":
        bot.send_message(call.message.chat.id, "Это информация о квадрате...")

    elif call.data == "triangle":
        msg = "Сейчас я ОЛЕГ покажу, что я знаю о треугольниках."

        keyboard = types.InlineKeyboardMarkup()
        key_Tri_Pr = types.InlineKeyboardButton(text='ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК', callback_data='triangle PR')
        keyboard.add(key_Tri_Pr)
        key_Tri_Or = types.InlineKeyboardButton(text='ОСТРОУГОЛЬНЫЙ ТРЕУГОЛЬНИК', callback_data='triangle OS')
        keyboard.add(key_Tri_Or)
        key_Tri_Ty = types.InlineKeyboardButton(text='ТУПОУГОЛЬНЫЙ ТРЕУГОЛЬНИК', callback_data='triangle TY')
        keyboard.add(key_Tri_Ty)

        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери тип треугольника:", reply_markup=keyboard)

    elif call.data == "triangle PR":
        bot.send_message(call.message.chat.id, "Это информация о прямоугольном треугольнике...")
    elif call.data == "triangle OS":
        bot.send_message(call.message.chat.id, "Это информация об остроугольном треугольнике...")
    elif call.data == "triangle TY":
        bot.send_message(call.message.chat.id, "Это информация о тупоугольном треугольнике...")


# Запускаем бота
bot.polling(none_stop=True)
