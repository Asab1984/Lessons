import telebot

import datetime

bot = telebot.TeleBot('5633107326:AAFalX819ICLzQ62-jkLsqhDc71q6ovgT-c')

@bot.message_handler(commands=['start'])  # функция называется как команда
def start(message):
    bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(commands=['hello'])
def hello(message):
    text = 'Привет! Как твои дела?'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['python'])
def python(message):
    text = 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes ' \
           'code readability with the use of significant indentation via the off-side rule.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['print'])
def hello(message):
    text = 'Используется для вывода текста или значений переменных на консоль.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['input'])
def hello(message):
    text = 'Позволяет пользователю вводить данные с клавиатуры, возвращает введенное значение в виде строки.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['len'])
def hello(message):
    text = 'Возвращает длину или размер объекта (например, строки, списка, кортежа и т.д.).'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['range'])
def hello(message):
    text = 'Создает последовательность чисел в заданном диапазоне.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['str'])
def hello(message):
    text = 'Преобразует объект в строку.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['int'])
def hello(message):
    text = 'Преобразует объект в целое число.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['float'])
def hello(message):
    text = 'Преобразует объект в число с плавающей запятой.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['max'])
def hello(message):
    text = 'Возвращает наибольшее значение из последовательности или аргументов.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['min'])
def hello(message):
    text = 'Возвращает наименьшее значение из последовательности или аргументов.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['sum'])
def hello(message):
    text = 'Возвращает сумму чисел в последовательности или списке.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'math':
        doc = open('math.html', 'r')
        bot.send_document(message.chat.id, doc)
    elif message.text == 'os':
        doc = open('os.html', 'r')
        bot.send_document(message.chat.id, doc)
    elif message.text == 'random':
        doc = open('random.html', 'r')
        bot.send_document(message.chat.id, doc)
    elif message.text == 're':
        doc = open('re.html', 'r')
        bot.send_document(message.chat.id, doc)
    elif message.text == 'sys':
        doc = open('sys.html', 'r')
        bot.send_document(message.chat.id, doc)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю...')

@bot.message_handler(commands=['datetime'])
def get_datetime_info(message):
    now = datetime.now()
    date = now.date()
    time = now.time()
    weekday = now.strftime('%A')
    week_number = now.strftime('%W')

    text = f'Текущая дата: {date}\n' \
           f'День недели: {weekday}\n' \
           f'Текущее время: {time}\n' \
           f'Номер недели: {week_number}'

    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

# Есть проблема- это все не работает... У меня выдает кучу ошибок в пайчарме,
# а в самом телеграм боте ничего не происходит.