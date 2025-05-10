import telebot
from telebot import types

# Указываем токен (не забудьте заменить на ваш токен)
bot = telebot.TeleBot('7581318358:AAGk09DLgZrhh2VJkk6wweip7lBangSiyIc')  # Замените на ваш токен

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
        bot.send_message(call.message.chat.id, "Признаки прямоугольника:
1. Если у выпуклого четырехугольника все углы прямые, то он является прямоугольником.
2. Если у параллелограмма диагонали равны, то он является прямоугольником.
Свойство прямоугольника:
Диагонали прямоугольника равны.
")
    elif call.data == "Square":
        bot.send_message(call.message.chat.id, "Свойства квадрата:
1. Все стороны равны.
2. Все углы прямые.
3. Диагонали точкой пересечения делятся пополам.
4. Диагонали равны.
5. Диагонали взаимно перпендикулярны.
6. Диагонали делят углы квадрата пополам.
7. Диагональ квадрата со стороной a равна a√2.
")

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
        bot.send_message(call.message.chat.id, "1.Круг — это фигура с наибольшей площадью при заданной длине периметра
2. Окружность и радиус круга пропорциональны.
3.Заключенная в нем площадь и квадрат его радиуса пропорциональны.
4.Константы пропорциональности равны 2π и π соответственно.
")
    elif call.data == "Circle OK":
        bot.send_message(call.message.chat.id, "1.Теорема о пересечении хорд гласит, что если два хорда CD и EB пересекаются в точке A, то AC × AD = AB × AE.
        2.Если две секущие AE и AD также пересекают окружность в точках B и C соответственно, то AC × AD = AB × AE (следствие из теоремы о длине хорды).
        3.Угол между хордой и касательной в одной из её конечных точек равен половине угла, образованного в центре окружности, на противоположной стороне хорды (угол между касательной и хордой).
        ")

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
        bot.send_message(call.message.chat.id, "1.Через любую точку, не лежащую на прямой, можно провести прямую, параллельную данной, и притом только одну.
        2.Если прямая пересекает одну из параллельных прямых, то она пересекает и другую")
    elif call.data == "Straight Pe":
        bot.send_message(call.message.chat.id, "1.Две прямые на плоскости называются перпендикулярными, если при пересечении они образуют 4 прямых угла.
        2.Две прямые в пространстве перпендикулярны друг другу, если они соответственно параллельны некоторым двум другим взаимно перпендикулярным прямым, лежащим в одной плоскости.")
   

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
        bot.send_message(call.message.chat.id, "1. Вертикальные углы всегда равны друг другу.")
    elif call.data == "Corner Sm":
        bot.send_message(call.message.chat.id, "1.сумма смежных углов равна 180 градусов")
    elif call.data == "Corner Pe":
        bot.send_message(call.message.chat.id, "Это информация о пересечения двух прямых секущей...")

    if call.data == "Corner Pe":
        msg = "Сейчас я покажу, что я знаю о пересечении двух прямых секущей."

        # Create an inline keyboard for angle types
        keyboard = types.InlineKeyboardMarkup()
        key_Yg_Pe_So = types.InlineKeyboardButton(text='соответственные углы', callback_data='Corner So')
        keyboard.add(key_Yg_Pe_So)
        key_Yg_Pe_Na = types.InlineKeyboardButton(text='накрест лежащие углы', callback_data='Corner Na')
        keyboard.add(key_Yg_Pe_Na)
        key_Yg_Pe_Od = types.InlineKeyboardButton(text='Односторонние углы', callback_data='Corner Od')
        keyboard.add(key_Yg_Pe_Od)

        # Send the initial message and the keyboard
        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери тип угла:", reply_markup=keyboard)


    elif call.data == "Corner So":
        bot.send_message(call.message.chat.id, "Если две параллельные прямые пересечены секущей, то соответственные углы равны.")
    elif call.data == "Corner Na":
        bot.send_message(call.message.chat.id, "Если две параллельные прямые пересечены секущей, то накрест лежащие углы равны.")
    elif call.data == "Corner Od":
        bot.send_message(call.message.chat.id, "Если две параллельные прямые пересечены секущей, то сумма односторонних углов равна 180 градусов.")



    elif call.data == "triangle PR":
        msg = "Сейчас я покажу, что я знаю о прямоугольных треугольных."

        keyboard = types.InlineKeyboardMarkup()
        key_Tri_Pr_B = types.InlineKeyboardButton(text='БИССИКТРИСА', callback_data='triangle PrB')
        keyboard.add(key_Tri_Pr_B)
        key_Tri_Pr_M = types.InlineKeyboardButton(text='МЕДИАНА', callback_data='triangle PrM')
        keyboard.add(key_Tri_Pr_M)
        key_Tri_Pr_V = types.InlineKeyboardButton(text='ВЫСОТА', callback_data='triangle PrV')
        keyboard.add(key_Tri_Pr_V)
        key_Tri_Pr_R = types.InlineKeyboardButton(text='ПРИЗНАКИ РАВЕНСТВА', callback_data='triangle PrR')
        keyboard.add(key_Tri_Pr_R)
        key_Tri_Pr_RB = types.InlineKeyboardButton(text='РАВНОБЕДРЕННОСТЬ', callback_data='triangle PrRB')
        keyboard.add(key_Tri_Pr_RB)

        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери что ты хочешь узнать о прямоугольном треугольнике:", reply_markup=keyboard)

    elif call.data == "triangle PrB":
        bot.send_message(call.message.chat.id, "биссиктриса в прямоугольном треугольнике делит угол на два равных")
    elif call.data == "triangle PrM":
        bot.send_message(call.message.chat.id, "медиана проведенная к гипотенузе равна ее половине")
    elif call.data == "triangle PrV":
        bot.send_message(call.message.chat.id, "1.Высота, опущенная на гипотенузу, является средним геометрическим (средним пропорциональным) двух отрезков гипотенузы.
        2.Каждая сторона треугольника является средним пропорциональным между гипотенузой и отрезком гипотенузы, примыкающим к стороне.")
    elif call.data == "triangle PrR":
        bot.send_message(call.message.chat.id, "1.если два катета одного прямоугольного треугольника соответственно равны двум катетам другого прямоугольного треугольника, то такие треугольники равны.
        2. Если катет и прилежащий к нему острый угол одного прямоугольного треугольника соответственно равны катету и прилежащему острому углу другого прямоугольного треугольника, то такие треугольники равны.
        3.если гипотенуза и прилежащий к ней угол одного прямоугольного треугольника соответственно равны гипотенузе и прилежащему углу другого треугольника, то такие треугольники равны.
        4.Если катет и гипотенуза одного треугольника соответственно равны катету и гипотенузе другого треугольника, такие прямоугольные треугольники равны.
        ")
    elif call.data == "triangle PrRB":
        bot.send_message(call.message.chat.id, "Биссектриса, медиана, высота и серединный перпендикуляр, проведённые к основанию, совпадают между собой. ")


    elif call.data == "triangle OS":
        msg = "Сейчас я покажу, что я знаю о прямоугольных треугольных."

        keyboard = types.InlineKeyboardMarkup()
        key_Tri_OS_B = types.InlineKeyboardButton(text='БИССИКТРИСА', callback_data='triangle OSB')
        keyboard.add(key_Tri_OS_B)
        key_Tri_OS_M = types.InlineKeyboardButton(text='МЕДИАНА', callback_data='triangle OSM')
        keyboard.add(key_Tri_OS_M)
        key_Tri_OS_V = types.InlineKeyboardButton(text='ВЫСОТА', callback_data='triangle OSV')
        keyboard.add(key_Tri_OS_V)
        key_Tri_OS_R = types.InlineKeyboardButton(text='ПРИЗНАКИ РАВЕНСТВА', callback_data='triangle OSR')
        keyboard.add(key_Tri_OS_R)
        key_Tri_OS_RB = types.InlineKeyboardButton(text='РАВНОБЕДРЕННОСТЬ', callback_data='triangle OSRB')
        keyboard.add(key_Tri_OS_RB)
        key_Tri_OS_RS = types.InlineKeyboardButton(text='РАВНОСТОРОННОСТЬ', callback_data='triangle OSRS')
        keyboard.add(key_Tri_OS_RS)

        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери что ты хочешь узнать о остроугоьном  треугольнике:", reply_markup=keyboard)

    elif call.data == "triangle OSB":
        bot.send_message(call.message.chat.id, "биссиктрисса делит угол на два равных")
    elif call.data == "triangle OSM":
        bot.send_message(call.message.chat.id, "медиана делит сторону пполам")
    elif call.data == "triangle OSV":
        bot.send_message(call.message.chat.id, "высота образует прямой угол")
    elif call.data == "triangle OSR":
        bot.send_message(call.message.chat.id, "1.Если две стороны и угол между ними одного треугольника равны соответственно двум сторонам и углу между ними другого треугольника, то такие треугольники равны.
2.Если сторона и прилежащие к ней углы одного треугольника равны соответственно стороне и прилежащим к ней углам другого треугольника, то такие треугольники равны.
3.Если три стороны одного треугольника равны трём сторонам другого треугольника, то такие треугольники равны.")
    elif call.data == "triangle OSRB":
        bot.send_message(call.message.chat.id, "Биссектриса, медиана, высота и серединный перпендикуляр, проведённые к основанию, совпадают между собой. ")
    elif call.data == "triangle OSRS":
        bot.send_message(call.message.chat.id, "1.в равностороннем треугольнике все стороны равны
2.в равносторонем треугольнике все углы равны 60 градусов")



    elif call.data == "triangle TY":
        msg = "Сейчас я покажу, что я знаю о тупогольных треугольных."

        keyboard = types.InlineKeyboardMarkup()
        key_Tri_TY_B = types.InlineKeyboardButton(text='БИССИКТРИСА', callback_data='triangle TYB')
        keyboard.add(key_Tri_TY_B)
        key_Tri_TY_M = types.InlineKeyboardButton(text='МЕДИАНА', callback_data='triangle TYM')
        keyboard.add(key_Tri_TY_M)
        key_Tri_TY_V = types.InlineKeyboardButton(text='ВЫСОТА', callback_data='triangle TYV')
        keyboard.add(key_Tri_TY_V)
        key_Tri_TY_R = types.InlineKeyboardButton(text='ПРИЗНАКИ РАВЕНСТВА', callback_data='triangle TYR')
        keyboard.add(key_Tri_TY_R)
        key_Tri_TY_RB = types.InlineKeyboardButton(text='РАВНОБЕДРЕННОСТЬ', callback_data='triangle TYRB')
        keyboard.add(key_Tri_TY_RB)

        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери что ты хочешь узнать о тупоугоьном  треугольнике:", reply_markup=keyboard)

    elif call.data == "triangle TYB":
        bot.send_message(call.message.chat.id, "биссиктрисса делит угол на два равных")
    elif call.data == "triangle TYM":
        bot.send_message(call.message.chat.id, "медиана делит сторону пполам")
    elif call.data == "triangle TYV":
        bot.send_message(call.message.chat.id, "высота в прямоугольном треугольнике проводится на продолжение стороны")
    elif call.data == "triangle TYR":
        bot.send_message(call.message.chat.id, "1.Если две стороны и угол между ними одного треугольника равны соответственно двум сторонам и углу между ними другого треугольника, то такие треугольники равны.
2.Если сторона и прилежащие к ней углы одного треугольника равны соответственно стороне и прилежащим к ней углам другого треугольника, то такие треугольники равны.
3.Если три стороны одного треугольника равны трём сторонам другого треугольника, то такие треугольники равны.")
    elif call.data == "triangle TYRB":
        bot.send_message(call.message.chat.id, "Биссектриса, медиана, высота и серединный перпендикуляр, проведённые к основанию, совпадают между собой.")



# Запускаем бота

bot.polling(none_stop=True)
