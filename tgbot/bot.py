import configure
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_command(message): # обработчик стартовой комманды
    bot.send_message(message.chat.id, 'Привет, я бот для управления твоими устройствами. \nС помощью команды /add можно добавить ip-aдрес устройства. \nКоманда /help поможет узнать, что умеет этот бот.')

@bot.message_handler(commands=["add"])
def add_device(message): # обработчик команды добавления устройства
    # парсинг ip
    # запрос у устройства доступных комманд
    # занесение устройства в бд 
    # отправка доступных комманд пользователю

@bot.message_handler(commands=["choose"])
def choose_device(message): # обработчик команды добавления устройства
    # парсинг имени
    # занесение выбора в бд 
    # отправка доступных комманд пользователю

@bot.message_handler(commands=["list"])
def list_devices(message): # обработчик команды вывода списка добавленных устройств
	# запрос к бд всех устройств данного пользователя
	# вывод всех устройств

@bot.message_handler(commands=["rename"])
def rename_device(message): # обработчик команды переименования устройства
	# парсинг старого и нового имени
	# запрос к базе по изменению имени устройства
	# вывод статуса операции

@bot.message_handler(commands=["commands"])
def list_commands_device(message): # обработчик команды вывода списка команд устройства
	# Запрос к бд текущего устройства
	# Запрос к бд списка комманд
	# Вывод комманд
