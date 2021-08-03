from aiogram import types

from app.keyboards.new_follow_buttons import new_follow
from bot import dp
from bot import db


# Выводит подписки если они есть
@dp.message_handler(commands=['follows'])
async def show_follows(message: types.Message):
    if db.follows_exists(message.from_user.id) != 0:
        subs = db.show_subs(message.from_user.id)
        for line in subs:
            await message.answer(line[0] + line[1], reply_markup=new_follow)
    else:
        await message.answer("У вас еще нет подписок", reply_markup=new_follow)
