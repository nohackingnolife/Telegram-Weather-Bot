from aiogram import types

from loader import dp
from .get_weather import get_weather


@dp.message_handler()
async def send_weather(message: types.Message, middleware_data=True):
    if middleware_data is False:
        return
    current_weather = await get_weather(message)
    if current_weather:
        await message.reply(current_weather)
