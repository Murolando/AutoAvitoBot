from aiogram import types
from bot import dp

@dp.message_handler(commands="info")
async def test(message: types.Message):
    await message.reply("infa dlya pidora")

