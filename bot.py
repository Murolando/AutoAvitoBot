import logging
from aiogram import Bot, Dispatcher, executor,types

from app.config import get_token
from db import AutoBotDB

API_TOKEN = get_token()


logging.basicConfig(level=logging.INFO)

# Инициализруем бота
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

#Инициализрую соединение с бд
db = AutoBotDB('auto_bot_base.db')


if __name__=="__main__":
    from app.handlers.start import dp # Команда start
    from app.handlers.info import dp # Команда info
    from app.handlers.show_follows import dp # Команда follows
    from app.handlers.stop import dp # Команда stop
    from app.handlers.new_follow import dp # События на добавление новой подписки
    from app.handlers.unfollow import dp # Событие на удаление подписка
    from app.handlers.avito import dp # avito actions
    executor.start_polling(dp, skip_updates=True)