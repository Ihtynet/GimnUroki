import os
from aiogram import Bot,Dispatcher,executor,types
from config import bot_token
import basemoduls as bs

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

tek_commands = {}

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    global tek_commands

    tx_user     = message.from_user.last_name + " " + message.from_user.first_name
    id_user     = message.from_user.id
    user_dates  = bs.check_users(id_user)

    if len(user_dates) == 0:
        tek_commands[id_user] = "start"
        await bot.send_message(id_user, "Здравствуйте, " + tx_user+". Введите пароль класса: ")
    else:
        tek_commands[id_user] = ""
        await bot.send_message(id_user, "Здравствуйте, " + tx_user+". Ваш класс: "+str(user_dates[0][0])+"\n Нажмите (<Меню>) для выборка действий")

"""        buttons = [
            types.InlineKeyboardButton(text="Выбрать ", callback_data="choice_urok"),
            types.InlineKeyboardButton(text="Выбрать видео", callback_data="film"),
            types.KeyboardButton('Сменить класс')
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(buttons)
        await bot.send_message(message.from_user.id, "Здравствуйте, " + tx_user, reply_markup=keyboard)
"""
@dp.message_handler(commands=['klass'])
async def command_klass(message: types.Message):
    global tek_commands
    tx_user = message.from_user.last_name + " " + message.from_user.first_name
    id_user = message.from_user.id
    tek_commands[id_user] = "klass"
    await bot.send_message(id_user, tx_user+". Введите пароль класса: ")



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
                await bot.send_message(id_user, tx_user + ". Ваш класс: " + str(user_dates[0][0]) + "\n Нажмите (<Меню>) для выборка действий")
                tek_commands[id_user] = ""
        else:
            await bot.send_message(id_user, "Не правильный пароль класса")


"""@dp.callback_query_handler(text="choice_urok")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer("123123123")"""


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates= True)