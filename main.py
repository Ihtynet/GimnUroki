import os
from aiogram import Bot,Dispatcher,executor,types
from config import bot_token, admin
import markup as nav
import basemoduls as bs

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    user_dates = bs.check_users(message.from_user.id)
    tx_user = message.from_user.last_name + " " + message.from_user.first_name
    if len(user_dates) == 0:
        await bot.send_message(message.from_user.id, "Здравствуйте, " + tx_user+". Введите пароль класса: ")
    else:
        buttons = [
            types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
            types.InlineKeyboardButton(text="Выбрать урок", callback_data="random_value")
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        await bot.send_message(message.from_user.id, "Здравствуйте, " + tx_user, reply_markup=keyboard)

@dp.message_handler()
async def bot_message(message: types.Message):

    tx_user = message.from_user.last_name + " " + message.from_user.first_name
    tx_username = message.from_user.username;
    mes = message.text
    print(mes)

    if mes[:3] == "ps#":
        print(mes)
        datacheck = bs.check_psw_klass(mes[3:])
        print(datacheck)
        if len(datacheck) == 1:
            print(message.from_user.id, datacheck[0][1], tx_user, tx_username)
            bs.registr_uses(message.from_user.id, datacheck[0][1], tx_user, tx_username)

@dp.callback_query_handler()
async def send_random_value(call: types.CallbackQuery):
    print(call)
    await call.message.answer(str(call.message))

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates= True)