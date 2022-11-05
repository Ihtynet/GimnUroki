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
    if len(user_dates) == 0:
        await bot.send_message(message.from_user.id, "Здравствуйте, {message.from_user}! Введите пароль класса:")



@dp.message_handler()
async def bot_message(message: types.Message):
    mes = message.text
    if mes[:3] == "ps#":
        datacheck = bs.check_psw_klass(mes[3:])
        if len(datacheck) == 1:
            bs.registr_uses(message.from_user.id, datacheck[0][1], message.from_user.name, message.from_user.name)
            #await bot.send_message(message.from_user.id, "Укажите ФАМИЛИЯ ИМЯ ученика: ")


"""    if message.text == "123":
        await bot.send_message(message.from_user.id,message.from_user)
    if message.text == "234":
        video = open('/home/user/vv1.mp4', 'rb')
        await bot.send_video(message.from_user.id,video, supports_streaming = True)
    if message.text=="1":
        pass"""
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates= True)