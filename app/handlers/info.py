from aiogram import types
from bot import dp

@dp.message_handler(commands="info")
async def info(message: types.Message):
    await message.answer("infa dlya pidora")

