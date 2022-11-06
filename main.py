import os
from aiogram import Bot,Dispatcher,executor,types
from config import bot_token
import basemoduls as bs

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

tek_command = ""

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    global tek_command

    user_dates = bs.check_users(message.from_user.id)
    tx_user = message.from_user.last_name + " " + message.from_user.first_name
    if len(user_dates) == 0:
        tek_command = "start"
        await bot.send_message(message.from_user.id, "Здравствуйте, " + tx_user+". Введите пароль класса: ")
    else:
        tek_command = ""
        await bot.send_message(message.from_user.id, "Здравствуйте, " + tx_user+". Ваш класс: "+str(user_dates[0][0])+"\n Нажмите (<Меню>) для выборка действий")

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
    global tek_command
    tx_user = message.from_user.last_name + " " + message.from_user.first_name
    tek_command = "klass"
    await bot.send_message(message.from_user.id, tx_user+". Введите пароль класса: ")



@dp.message_handler()
async def bot_message(message: types.Message):
    #await bot.send_message(message.from_user.id, message.text)
    tx_user = message.from_user.last_name + " " + message.from_user.first_name
    tx_username = message.from_user.username
    mes = message.text
    print(mes)

    if mes[:3] == "ps#" and (tek_command == "start" or tek_command == "klass"):
        print("Смена класса: "+mes)
        datacheck = bs.check_psw_klass(mes[3:])
        #print(datacheck)
        if len(datacheck) == 1:
            #print(message.from_user.id, datacheck[0][1], tx_user, tx_username)
            user_dates = bs.registr_uses(message.from_user.id, datacheck[0][1], tx_user, tx_username)

            if len(user_dates) == 0:
                await bot.send_message(message.from_user.id, "Ошибка регистрации. Введите пароль класса: ")
            else:
                await bot.send_message(message.from_user.id, tx_user + ". Ваш класс: " + str(
                    user_dates[0][0]) + "\n Нажмите (<Меню>) для выборка действий")
        else:
            await bot.send_message(message.from_user.id, "Не правильный пароль класса")


"""@dp.callback_query_handler(text="choice_urok")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer("123123123")"""


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates= True)