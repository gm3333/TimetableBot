import telebot
from config import bot

# /help command processing
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'its a help message! \n'
                                      'About MTUCI click here - /mtuci')