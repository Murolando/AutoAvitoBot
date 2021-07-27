import logging
from aiogram import Bot, Dispatcher, executor,types

from app.config import get_token

API_TOKEN = get_token()


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


if __name__=="__main__":
    from app.handlers.start import dp #Команда start
    from app.handlers.info import dp #Команда info
    executor.start_polling(dp,skip_updates=True)