from aiogram.types import CallbackQuery

from app.keyboards.new_follow_buttons import choise_mark_but, choise_price_but, new_follow
import  app.keyboards.callback_datas
from bot import dp, db

# Событие после нажатия на "новую подписку"
@dp.callback_query_handler(text_contains="new")
async def make_new_follow(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Заполните форму, для оформления подписки:\n"
                              "Выберете марку, интересующего вас автомобиля", reply_markup=choise_mark_but())

# Событие после выбора нужной марки
@dp.callback_query_handler(text_contains="mark")
async def make_new_follow(call: CallbackQuery):
    await call.answer(cache_time=60)
    call_info = call.data.split(':')
    mark_id = int(call_info[1])
    await call.message.answer("Выберете максимальную цену, для фильтрации объявлений", reply_markup=choise_price_but(mark_id))

# Событие после выбора нужной цены
@dp.callback_query_handler(text_contains="price")
async def make_new_follow(call: CallbackQuery):
    call_info = call.data.split(':')
    mark_id = int(call_info[1])
    price_id = int(call_info[2])
    if not db.this_follow_exist(call.from_user.id, mark_id, price_id):
        db.add_follow(call.from_user.id, mark_id, price_id)
        await call.answer("Новая подписка успешно добавлена")
    else:
        await call.answer("Такая подписка уже есть нахуй наебываешь?")
