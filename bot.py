import telebot
import telegram

bot = telebot.TeleBot('1113866643:AAFOKzYmOPdXZGVqlLS_qJFGZfF3s-_Xago')
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
cross = u'\U0000274C'
keyboard.row('Сайт', 'Контакты', cross + ' Закрыть')
@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал старт! Чтобы открыть меню напиши /menu или открой панель')
@bot.message_handler(commands = ['menu'])
def menu_message(message):
    bot.send_message(message.chat.id, 'Меню:', reply_markup=keyboard)
@bot.message_handler(content_types = ['text'])
def send_text(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'ку' or message.text.lower() == 'даров':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() == 'сайт':
        bot.send_message(message.chat.id,
                         text='<i>Вот наш сайт</i> <a href="http://yandex.ru">Ссылка на сайт</a>.',
                         parse_mode=telegram.ParseMode.HTML)
    elif message.text.lower() == 'контакты':
        bot.send_message(message.chat.id, 'Наш телефон 89299292929292')
    elif message.text.lower() == '\U0000274C закрыть':
        bot.send_message(message.chat.id, 'Чтобы вызвать мнею снова напишите /menu или откройте панель')
    elif message.text.lower() == 'как дела' or message.text.lower() == 'че как' or message.text.lower() == 'ты как'or message.text.lower() == 'как дела?' or message.text.lower() == 'че как?' or message.text.lower() == 'ты как?' or message.text.lower() == 'как ты?':
        bot.send_message(message.chat.id, 'норм, я крут, напиши мне это :)')
    elif message.text.lower() == 'ты крут':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJE6V6TIazgzEN90SCF_mTz4-6vA8LTAAKfAAP3AsgPy97xlgABDNP-GAQ')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()