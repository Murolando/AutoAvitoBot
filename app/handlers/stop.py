from aiogram import types
from bot import dp
from bot import db


@dp.message_handler(commands="stop")
async def stop(message: types.Message):
    if db.follows_exists(message.from_user.id) != 0:
        db.del_follow(message.from_user.id)
        await message.answer("Вы отписались от всех рассылок")
    else:
        await message.answer("Вы и так уже от всего отписались")
