from aiogram import types

from app.keyboards.new_follow_buttons import new_follow
from bot import dp, db


# Выводит подписки если они есть
@dp.message_handler(commands=['follows'])
async def show_follows(message: types.Message):
    if db.follows_exists(message.from_user.id) != 0:
        subs = db.show_subs(message.from_user.id)
        for line in subs:
            await message.answer(line[1] + line[2], reply_markup=new_follow(True, line[0]))
    else:
        await message.answer("У вас еще нет подписок", reply_markup=new_follow())
