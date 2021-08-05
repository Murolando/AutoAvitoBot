from aiogram.types import CallbackQuery
from bot import dp, db

# Событие нажатия на кнопку "unfollow"
@dp.callback_query_handler(text_contains="unfollow")
async def unfollow_hand(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_data = call.data.split(':')
    id_follow = call_data[1]
    if db.this_follow_exist2(id_follow):
        db.del_this_follow(id_follow)
        await call.message.answer("Вы успешно отписались от этой подписки")
    else:
        await call.message.answer("Вы уже давно отписались от этой подписки")