from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from main import res


botPrivate = Bot('6153740632:AAHWU3SRGXUJhCttZK1dyvwzTrCiLt8e8do')


dpPrivate = Dispatcher(botPrivate)


@dpPrivate.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}. Your order - {res["orderName"]}')

executor.start_polling(dpPrivate)


534715062