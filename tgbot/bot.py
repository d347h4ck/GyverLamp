import configure
import telebot
from database import SQLighter

bot = telebot.TeleBot(configure.token)


@bot.message_handler(commands=["start"])
def start_command(message): # обработчик стартовой комманды
    db_worker = SQLighter(configure.database)
    db_worker.add_user(message.chat.id)
    bot.send_message(message.chat.id, 'Привет, я бот для управления твоими устройствами. \nС помощью команды /add можно добавить ip-aдрес устройства. \nКоманда /help поможет узнать, что умеет этот бот.')

@bot.message_handler(commands=["add"])
def add_device(message): # обработчик команды добавления устройства
    pass
    # парсинг ip
    # запрос у устройства доступных комманд
    # занесение устройства в бд 
    # отправка доступных комманд пользователю

@bot.message_handler(commands=["choose"])
def choose_device(message): # обработчик команды добавления устройства
    pass
    # парсинг имени
    # занесение выбора в бд 
    # отправка доступных комманд пользователю

@bot.message_handler(commands=["list"])
def list_devices(message): # обработчик команды вывода списка добавленных устройств
    pass
    # запрос к бд всех устройств данного пользователя
    # вывод всех устройств

@bot.message_handler(commands=["rename"])
def rename_device(message): # обработчик команды переименования устройства
    pass
    # парсинг старого и нового имени
    # запрос к базе по изменению имени устройства
    # вывод статуса операции

@bot.message_handler(commands=["commands"])
def list_commands_device(message): # обработчик команды вывода списка команд устройства
    pass
    # Запрос к бд текущего устройства
    # Запрос к бд списка комманд
    # Вывод комманд

@bot.message_handler(commands=["run"])
def run_command(message): # обработчик команды вывода списка команд устройства
    pass
    # парсинг команды и аргументов
    # Запрос к бд текущего устройства
    # Запрос к бд списка комманд
    # проверка существования комманды
    # запуск комманды
    # вывод статуса

if __name__ == '__main__':
    bot.polling(none_stop=True)