import telebot;
from telebot import types
bot = telebot.TeleBot('');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "/start":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь? Чтобы посмотреть что я умею введи /help")
  elif message.text == "/help":
    bot.send_message(message.from_user.id, "Для того, чтобы произвести умножение введите /multiple")
    bot.send_message(message.from_user.id, "Для того, чтобы произвести деление введите /division")
    bot.send_message(message.from_user.id, "Для того, чтобы произвести сложение введите /addition")
    bot.send_message(message.from_user.id, "Для того, чтобы произвести вычитание введите /subtraction")
  elif message.text == '/multiple':
    bot.send_message(message.from_user.id, "Введите два числа через пробел (для двоичных чисел используйте .)");
    bot.register_next_step_handler(message, get_multiple);
  elif message.text == '/division':
    bot.send_message(message.from_user.id, "Введите два числа через пробел (для двоичных чисел используйте .)");
    bot.register_next_step_handler(message, get_division);
  elif message.text == '/addition':
    bot.send_message(message.from_user.id, "Введите два числа через пробел (для двоичных чисел используйте .)");
    bot.register_next_step_handler(message, get_addition);
  elif message.text == '/subtraction':
    bot.send_message(message.from_user.id, "Введите два числа через пробел (для двоичных чисел используйте .)");
    bot.register_next_step_handler(message, get_subtraction);
  else:
    bot.send_message(message.from_user.id, "Я такого еще не умею. Напиши /help.")

def get_multiple(message):
  a = 0;
  b = 0;
  answer = "";
  mestext = message.text;
  if (mestext.find(' ') != -1):
    text = mestext.split(' ');
    try:
        a = float(text[0]);
        b = float(text[1]);
        answer = 'Результат '+str(a*b);
        bot.send_message(message.from_user.id, text=answer)
    except:
        bot.send_message(message.from_user.id, "ERROR: Введите числа")
  else:
    bot.send_message(message.from_user.id, "ERROR: Введите два числа через пробел")

def get_division(message):
  a = 0;
  b = 0;
  answer = "";
  mestext = message.text;
  if (mestext.find(' ') != -1):
    text = mestext.split(' ');
    try:
        a = float(text[0]);
        b = float(text[1]);
        answer = 'Результат '+str(a/b);
        bot.send_message(message.from_user.id, text=answer)
    except:
        bot.send_message(message.from_user.id, "ERROR: Введите числа")
  else:
    bot.send_message(message.from_user.id, "ERROR: Введите два числа через пробел")

def get_addition(message):
  a = 0;
  b = 0;
  answer = "";
  mestext = message.text;
  if (mestext.find(' ') != -1):
    try:
        a = float(text[0]);
        b = float(text[1]);
        answer = 'Результат '+str(a+b);
        bot.send_message(message.from_user.id, text=answer)
    except:
        bot.send_message(message.from_user.id, "ERROR: Введите числа")
  else:
    bot.send_message(message.from_user.id, "ERROR: Введите два числа через пробел")

def get_subtraction(message):
  a = 0;
  b = 0;
  answer = "";
  mestext = message.text;
  if (mestext.find(' ') != -1):
    try:
        a = float(text[0]);
        b = float(text[1]);
        answer = 'Результат '+str(a-b);
        bot.send_message(message.from_user.id, text=answer)
    except:
        bot.send_message(message.from_user.id, "ERROR: Введите числа")
  else:
    bot.send_message(message.from_user.id, "ERROR: Введите два числа через пробел")

bot.polling(none_stop=True, interval=0)
