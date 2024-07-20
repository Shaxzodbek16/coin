import json
import telebot
import requests


TOKEN = '7474243462:AAF768BqbIl9X8TKkGAkHjdOOt2hw3aoy48'

API_URL = 'https://tmshaxzodbek.jprq.app/api/user/'
WEBSITE_URL = 'https://tmshaxzodbek.jprq.app/api/user'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    data = {
        'telegram_id': str(user.id),
        'name': user.first_name,


    }
    data = json.dumps(data)
    response = requests.post(API_URL, data=data)
    if response.status_code == 201:
        markup = telebot.types.InlineKeyboardMarkup()
        btn_website = telebot.types.InlineKeyboardButton(text='Play', url=WEBSITE_URL)
        markup.add(btn_website)
        bot.send_message(message.chat.id, "Ma'lumotlaringiz qabul qilindi!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")


bot.polling()
