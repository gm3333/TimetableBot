import telebot # import telebot lib
import psycopg2 # import postgresql lib
import datetime
from datetime import date
from telebot import types # import types from telebot lib
from mtuci import mtuci_message # import main function mtuci_message from mtuci.py for correctly working
from markup import start_msg # import main function start_msg from markup.py for correctly working
from help import help_message # import main function help_message from help.py for correctly working
from config import bot # import bot with setted token from config.py
from config import connection
from database_update import database_update
from config import current_weeek


connection.autocommit = True

curr_weak = current_weeek




def get_timetable(day, chat_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM days.{day} ORDER BY id;""")
            res = cursor.fetchall()
            s_res = ''
            for i in res:
                id, room, teacher, subject, time = list(i)
                s = f'Пара №{id} - {room} - {teacher} - {subject} - {time}'
                s_res += s + '\n'
            bot.send_message(chat_id, s_res)
    except Exception as _ex:
        print('Wrong', _ex)

# callback keyboard processing
@bot.callback_query_handler(func=lambda message: True)
def logic_inline(message):
    global current_weeek

    database_update(curr_weak)

    if message.data == 'one':
        day = 'monday'
        chat_id = message.message.chat.id
        get_timetable(day, chat_id)
    elif message.data == 'two':
          day = 'tuesday'
          chat_id = message.message.chat.id
          get_timetable(day, chat_id)
    elif message.data == 'three':
          day = 'wednesday'
          chat_id = message.message.chat.id
          get_timetable(day, chat_id)
    elif message.data == 'four':
          day = 'thursday'
          chat_id = message.message.chat.id
          get_timetable(day, chat_id)
    elif message.data == 'five':
          day = 'friday'
          chat_id = message.message.chat.id
          get_timetable(day, chat_id)
    elif message.data == 'six':
          day = 'saturday'
          chat_id = message.message.chat.id
          get_timetable(day, chat_id)
    elif message.data == 'now':
        chat_id = message.message.chat.id
        bot.send_message(chat_id, '////////////////////////////////')
        get_timetable('monday', chat_id)
        get_timetable('tuesday', chat_id)
        get_timetable('wednesday', chat_id)
        get_timetable('thursday', chat_id)
        get_timetable('friday', chat_id)
        get_timetable('saturday', chat_id)

    elif message.data == 'next_week':
        curr = current_weeek + 1
        database_update(curr)
        chat_id = message.message.chat.id
        bot.send_message(chat_id, '////////////////////////////////')
        get_timetable('monday', chat_id)
        get_timetable('tuesday', chat_id)
        get_timetable('wednesday', chat_id)
        get_timetable('thursday', chat_id)
        get_timetable('friday', chat_id)
        get_timetable('saturday', chat_id)
        curr -= 1



bot.polling()