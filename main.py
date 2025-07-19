from flask import Flask, request
import telebot

API_TOKEN = "7939932839:AAEx7y3C7bnaojrjg57DTrO5NHQ-r6nWVIk"
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# وقتی پیام متنی میاد


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام سجاد! ربات فعاله ✌️")

# روت برای وب‌هوک


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    else:
        return 'Unsupported Media Type', 415

# برای تست


@app.route('/', methods=['GET'])
def index():
    return "ربات تلگرام Flask فعاله 🎯"


# فقط برای تست لوکال
if __name__ == '__main__':
    app.run(debug=True)
