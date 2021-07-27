from aiogram import types
from bot import dp

@dp.message_handler(commands="start")
async def test(message: types.Message):
    await message.reply("hello \n zaebal")
