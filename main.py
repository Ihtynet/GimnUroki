import os
from aiogram import Bot,Dispatcher,executor,types
from config import bot_token, admin
import markup as nav

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):

    #await bot.send_message(message.from_user.id,"Привет!".format(message.from_user),reply_markup=nav.mainMenu)
    await bot.send_message(message.from_user.id, "Привет!".format(message.from_user))
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "123":
        await bot.send_message(message.from_user.id,message.from_user)
    if message.text == "234":
        video = open('/home/user/vv1.mp4', 'rb')
        await bot.send_video(message.from_user.id,video, supports_streaming = True)
    if message.text=="1":
        pass
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates= True)