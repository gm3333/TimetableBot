import telebot
from config import bot

# /mtuci command processing
@bot.message_handler(commands=['mtuci'])
def mtuci_message(message):
    bot.send_message(message.chat.id, 'Info about mtuci here - its link')