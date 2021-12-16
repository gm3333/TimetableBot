import telebot
import psycopg2 # import postgresql lib
import datetime
from datetime import date

# bot initialization
now = date.today()
splitted_now = list(map(int,str(now).split('-')))
current_weeek = datetime.date(*splitted_now).isocalendar()[1]+1

TOKEN = '5096681875:AAGTSfB8ArrDshpAl4SzhXvXOcuQa09qTKE'
bot = telebot.TeleBot(TOKEN)

# Database settings

host = '127.0.0.1'
user = 'postgres'
password = 'qwerty'
db_name = 'timetablebot_db'
port = 5432

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)