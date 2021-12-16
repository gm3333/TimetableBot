import telebot
from telebot import types
from config import bot


# button settings and them adding to keyboard
@bot.message_handler(commands=['start'])
def start_msg(message):

    # settings
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    one = types.InlineKeyboardButton('Понедельник', callback_data='one')
    two = types.InlineKeyboardButton('Вторник', callback_data='two')
    three = types.InlineKeyboardButton('Среда', callback_data='three')
    four = types.InlineKeyboardButton('Четверг', callback_data='four')
    five = types.InlineKeyboardButton('Пятница', callback_data='five')
    six = types.InlineKeyboardButton('Суббота', callback_data='six')

    now = types.InlineKeyboardButton('Расписание на текущую неделю', callback_data='now')
    next_week = types.InlineKeyboardButton('Расписание на следующую неделю', callback_data='next_week')

    # adding
    keyboard.add(one, two, three, four, five, six, now, next_week)

    bot.send_message(message.chat.id, 'Здравствуйте! С помощью этого бота можно узнать расписание занятий на любой день недели, следующую неделю или текущую.', reply_markup=keyboard)

    # help message
    bot.send_message(message.chat.id, 'Чтобы вывести список доступных команд, напишите /help')