from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.keyboards.callback_datas import new_follow_callback, choise_mark_callback, choise_price_callback

from bot import db

# Клавиатура новой подписки
new_follow = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Новая подписка", callback_data=new_follow_callback.new(clown=12))
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="cancel")
        ]
    ]
)

# Клавиатура выбора нужной марки
def choise_mark_but():
    choise_mark = InlineKeyboardMarkup(row_width=3)
    marks = db.show_marks()
    for mark in marks:
        mark_button = InlineKeyboardButton(text=str(mark[1]), callback_data=choise_mark_callback.new(mark_id=mark[0]))
        choise_mark.insert(mark_button)
    return choise_mark

# Клавиатура выбора нужной цены
def choise_price_but(mark_id):
    choise_price = InlineKeyboardMarkup(row_width=3)
    prices = db.show_prices()
    for price in prices:
        price_button = InlineKeyboardButton(text=str(price[1]), callback_data=choise_price_callback.new(mark_id=mark_id, price_id=price[0]))
        choise_price.insert(price_button)
    return choise_price
