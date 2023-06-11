from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6002497072:AAGb2F-V7auEfNkVP_6GwQMIeJfAwB7CxqE')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start (message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Open Menu", web_app=WebAppInfo(url='https://github.com/AKogut/telegramBotWeb')))
    await message.answer('Hey, it is delivery sushi', reply_markup=markup)

executor.start_polling(dp)
