import telebot
from telebot import types

# Указываем токен (не забудьте заменить на ваш токен)
bot = telebot.TeleBot('токен')  # Замените на ваш токен

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, сейчас я покажу тебе мой каталог.")
        keyboard = types.InlineKeyboardMarkup()

        key_Tri = types.InlineKeyboardButton(text='ТРЕУГОЛЬНИК', callback_data='triangle')
        keyboard.add(key_Tri)
        key_PrKv = types.InlineKeyboardButton(text='ПРЯМОУГОЛЬНИК И КВАДРАТ', callback_data='geometry')
        keyboard.add(key_PrKv)
        key_Ok = types.InlineKeyboardButton(text='ОКРУЖНОСТЬ И КРУГ', callback_data='Circle')
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
        msg = "Сейчас я покажу, что я знаю о прямоугольнике и квадрате."

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
        msg = "Сейчас я покажу, что я знаю о треугольниках."

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

    elif call.data == 'Circle':
        msg = "Сейчас я покажу, что я знаю о окружностях и кругах."
        keyboard = types.InlineKeyboardMarkup()

        key_Ok_Kr = types.InlineKeyboardButton(text='ОКРУЖНОСТЬ', callback_data='Circle Kr')
        keyboard.add(key_Ok_Kr)
        key_Ok_Ok = types.InlineKeyboardButton(text='КРУГ', callback_data='Circle OK')
        keyboard.add(key_Ok_Ok)
        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери окружность или круг:", reply_markup=keyboard)
    elif call.data == "Circle Kr":
        bot.send_message(call.message.chat.id, "Это информация о круге...")
    elif call.data == "Circle OK":
        bot.send_message(call.message.chat.id, "Это информация о окружности...")

    elif call.data == "Straight":
        msg = "Сейчас я покажу, что я знаю о прямых."

        keyboard = types.InlineKeyboardMarkup()
        key_Pr_Pa = types.InlineKeyboardButton(text='ПАРАЛЕЛЬНЫЕ', callback_data='Straight Pa')
        keyboard.add(key_Pr_Pa)
        key_Pr_Pe = types.InlineKeyboardButton(text='ПЕРЕПЕНДЕКУЛЯРНЫЕ', callback_data='Straight Pe')
        keyboard.add(key_Pr_Pe)
        key_Pr_PP = types.InlineKeyboardButton(text='ПАРАЛЕЛЬНЫЕ И ПЕРПЕНДЕКУЛЯРНЫЕ', callback_data='Straight PP')
        keyboard.add(key_Pr_PP)

        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери тип прямой:", reply_markup=keyboard)

    elif call.data == "Straight Pa":
        bot.send_message(call.message.chat.id, "Это информация о паралельных прямых...")
    elif call.data == "Straight Pe":
        bot.send_message(call.message.chat.id, "Это информация о перпендекулярных прямых...")
    elif call.data == "Straight PP":
        bot.send_message(call.message.chat.id, "Это информация о парадельных и перпендекулярных прямых...")

    elif call.data == "Corner":
        msg = "Сейчас я покажу, что я знаю о углах."

        keyboard = types.InlineKeyboardMarkup()
        key_Yg_Ve = types.InlineKeyboardButton(text='ВЕРТЕКАЛЬНЫЕ УГЛЫ', callback_data='Corner Ve')
        keyboard.add(key_Yg_Ve)
        key_Yg_Sm = types.InlineKeyboardButton(text='СМЕЖНЫЕ УГЛЫ', callback_data='Corner Sm')
        keyboard.add(key_Yg_Sm)
        key_Yg_Pe = types.InlineKeyboardButton(text='ДВЕ ПРЯМЫЕ И СЕКУЩАЯ', callback_data='Corner Pe')
        keyboard.add(key_Yg_Pe)

        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери тип угла:", reply_markup=keyboard)

    elif call.data == "Corner Ve":
        bot.send_message(call.message.chat.id, "Это информация о вертикальных углах...")
    elif call.data == "Corner Sm":
        bot.send_message(call.message.chat.id, "Это информация о смежных углах...")
    elif call.data == "Corner Pe":
        bot.send_message(call.message.chat.id, "Это информация о пересечения двух прямых секущей...")

    elif call.data == "Corner Pe":
        msg = "Сейчас я покажу, что я знаю о пересечение двух прямых секущей."

        keyboard = types.InlineKeyboardMarkup()
        key_Yg_Pe_So = types.InlineKeyboardButton(text='соответственные углы', callback_data='Corner So')
        keyboard.add(key_Yg_Pe_So)
        key_Yg_Pe_Na = types.InlineKeyboardButton(text='накрест лежащие углы', callback_data='Corner Na')
        keyboard.add(key_Yg_Pe_Na)
        key_Yg_Pe_Od = types.InlineKeyboardButton(text='Односторонние углы', callback_data='Corner Od')
        keyboard.add(key_Yg_Pe_Od)

        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери тип угла:", reply_markup=keyboard)

    elif call.data == "Corner So":
        bot.send_message(call.message.chat.id, "Это информация о соответственных  углах...")
    elif call.data == "Corner Na":
        bot.send_message(call.message.chat.id, "Это информация о накрест лежащих углах...")
    elif call.data == "Corner Od":
        bot.send_message(call.message.chat.id, "Это информация о односторонних углах...")

        # Запускаем бота
bot.polling(none_stop=True)
