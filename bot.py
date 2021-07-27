import logging
from aiogram import Bot, Dispatcher, executor,types

from app.config import get_token

API_TOKEN = get_token()


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def test(message: types.Message):
    await message.reply("Safasf")

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)