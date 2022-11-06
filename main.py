import os
from aiogram import Bot,Dispatcher,executor,types
from config import bot_token
import basemoduls as bs

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

tek_commands    = {}
tek_urok        = {}
tek_klass       = {}

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    global tek_commands

    tx_user     = message.from_user.last_name + " " + message.from_user.first_name
    id_user     = message.from_user.id
    user_dates  = bs.check_users(id_user)
    tek_urok[id_user] = ""
    tek_klass[id_user] = ""
    if len(user_dates) == 0:
        tek_commands[id_user] = "start"
        await bot.send_message(id_user, "Здравствуйте, " + tx_user+". Введите пароль класса: ")
    else:
        tek_commands[id_user]   = ""
        tek_klass[id_user]      = user_dates[0][0]
        await bot.send_message(id_user, "Здравствуйте, " + tx_user+". Ваш класс: "+str(tek_klass[id_user])+"\n Нажмите (<Меню>) для выборка действий")


@dp.message_handler(commands=['klass'])
async def command_klass(message: types.Message):
    global tek_commands
    tx_user = message.from_user.last_name + " " + message.from_user.first_name
    id_user = message.from_user.id
    tek_commands[id_user] = "klass"
    tek_urok[id_user] = ""
    tek_klass[id_user] = ""
    await bot.send_message(id_user, ">>Введите пароль класса: ")


@dp.message_handler(commands=['urok'])
async def command_klass(message: types.Message):
    global tek_commands
    tx_user = message.from_user.last_name + " " + message.from_user.first_name
    id_user = message.from_user.id
    tek_commands[id_user] = "urok"
    tek_urok[id_user] = ""
    tek_klass[id_user] = ""
    ## нАДО СОЗДАТЬ СПИСОК КНОПОК С ПРЕДМЕТАМИ КЛАССА
    await bot.send_message(id_user, ">>Выберите предмет: ")

@dp.message_handler(commands=['movies'])
async def command_klass(message: types.Message):
    global tek_commands
    tx_user = message.from_user.last_name + " " + message.from_user.first_name
    id_user = message.from_user.id
    tek_commands[id_user] = "urok"
    tek_urok[id_user] = ""
    tek_klass[id_user] = ""
    ## нАДО СОЗДАТЬ СПИСОК КНОПОК С видео КЛАССА
    await bot.send_message(id_user, ">>Выберите видео запись: ")

@dp.message_handler()
async def bot_message(message: types.Message):
    global tek_commands
    #await bot.send_message(message.from_user.id, message.text)
    tx_user     = message.from_user.last_name + " " + message.from_user.first_name
    id_user      = message.from_user.id
    tx_username = message.from_user.username

    mes = message.text
    print(mes)

    if mes[:3] == "ps#" and (tek_commands[id_user] == "start" or tek_commands[id_user] == "klass"):
        print("Задание класса: "+ mes)
        datacheck = bs.check_psw_klass(mes[3:])
        #print(datacheck)
        if len(datacheck) == 1:
            #print(message.from_user.id, datacheck[0][1], tx_user, tx_username)
            user_dates = bs.registr_uses(id_user, datacheck[0][1], tx_user, tx_username)

            if len(user_dates) == 0:
                await bot.send_message(id_user, "Ошибка регистрации. Введите пароль класса: ")
            else:
                tek_klass[id_user] = user_dates[0][0]
                await bot.send_message(id_user, tx_user + ". Ваш класс: " + str(tek_klass[id_user]) + "\n Нажмите (<Меню>) для выборка действий")
                tek_commands[id_user]   = ""
                tek_klass[id_user]      = ""

        else:
            await bot.send_message(id_user, "Не правильный пароль класса")





if __name__ == "__main__":
    executor.start_polling(dp,skip_updates= True)