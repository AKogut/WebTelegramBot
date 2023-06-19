from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

# chat_id = 1001918796192

bot = Bot('6002497072:AAGb2F-V7auEfNkVP_6GwQMIeJfAwB7CxqE')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start (message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Open Menu", web_app=WebAppInfo(url='https://akogut.github.io/WebSiteForTelegramBot/')))
    await message.answer('Hey, it is delivery sushi', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}. Your order - {res["orderName"]}')
    # await bot.send_message(chat_id, 'hello')

executor.start_polling(dp)
