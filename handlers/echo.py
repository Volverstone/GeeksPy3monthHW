from aiogram import types, Dispatcher
from math import pow

async def echo_handler(message: types.Message):
    if message.text.isdigit() == True:
        await message.answer(round(pow(int(message.text),2)))
    else:
        await message.answer(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo_handler)