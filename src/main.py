import telebot
import os
import FileManager

from telebot import types
token = '5148266752:AAF8-LNG_vYLxEK83N0cNfGZ4bi36amFsF0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, 'Здарова! Я pdf бот, могу разделить или объединить pdf файлы. А еще конвертировать docx в pdf!\nПришли мне файлики!\nзатем пиши \do')

@bot.message_handler(content_types=['document'])
def doc_handler(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = '/Users/pita2/PycharmProjects/telebot_test/files/' + message.document.file_name;
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

@bot.message_handler(commands=['do'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    split = types.KeyboardButton("разделить файлик")
    merge = types.KeyboardButton("объединить файлики")
    convert = types.KeyboardButton("docx -> pdf")
    markup.add(split, merge, convert)
    bot.send_message(message.chat.id, 'Выбери что тебе нужно', reply_markup=markup)

@bot.message_handler(content_types=['text'], func=lambda message: message.text.lower() == "разделить файлик")
def SplitFile(message):
    try:
        pdf = FileManager.PdfFile()
        pdf.split()
        bot.send_message(message.chat.id, 'Разделено!')
        for filename in os.listdir("files"):
            bot.send_document(message.chat.id, open(os.path.join("files", filename), 'rb'))
            os.remove(os.path.join("files", filename))
    except Exception as e:
        bot.reply_to(message, e)

@bot.message_handler(content_types=['text'], func=lambda message: message.text.lower() == "объединить файлики")
def MergeFiles(message):
    try:
        pdf = FileManager.PdfFile()
        pdf.merge()
        bot.send_message(message.chat.id, 'Объединил!')
        for filename in os.listdir("files"):
            bot.send_document(message.chat.id, open(os.path.join("files", filename), 'rb'))
            os.remove(os.path.join("files", filename))
    except Exception as e:
        bot.reply_to(message, e)

@bot.message_handler(content_types=['text'], func=lambda message: message.text.lower() == "docx -> pdf")
def ConvertFiles(message):
    try:
        pdf = FileManager.PdfFile()
        pdf.convert()
        bot.send_message(message.chat.id, 'Конвертировал!!')
        for filename in os.listdir("files"):
            bot.send_document(message.chat.id, open(os.path.join("files", filename), 'rb'))
            os.remove(os.path.join("files", filename))
    except Exception as e:
        bot.reply_to(message, e)

bot.polling(none_stop=True)