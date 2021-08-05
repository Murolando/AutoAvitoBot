from aiogram import types
from bot import dp
from bot import db


@dp.message_handler(commands="start")
async def start(message: types.Message):
    if not db.user_exist(message.from_user.id):
        db.add_user(message.from_user.id)
    await message.answer("Добро пожаловать в бота для отслеживания объявлений об продаже автомобилей на всех популярных площадках\n"
                        "Для получения информации о возможностях бота используйте команду /info")