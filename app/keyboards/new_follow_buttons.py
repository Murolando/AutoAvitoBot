from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.keyboards.callback_datas import new_follow_callback, choise_mark_callback, choise_price_callback, unfollow_callback

from bot import db

# Клавиатура новой подписки и отписки,я просто хз как это сделать лучше
def new_follow(flag = False,id_follow = 0):
    new_follow_key = InlineKeyboardMarkup(row_width=1)
    if flag:
        unfollow_button = InlineKeyboardButton(text="Отписаться",
                                               callback_data=unfollow_callback.new(id_follow=id_follow))
        new_follow_key.insert(unfollow_button)
    new_follow_key.insert(InlineKeyboardButton(text="Новая подписка", callback_data=new_follow_callback.new(clown=12)))
    new_follow_key.insert(InlineKeyboardButton(text="Назад", callback_data="cancel"))
    return new_follow_key

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
    prices_radius = [500000, 1000000, "больше"]
    print(prices)
    for i in range(3):
        price_button = InlineKeyboardButton(text=str(f"{prices[i][1]}-{prices_radius[i]}"), callback_data=choise_price_callback.new(mark_id=mark_id, price_id=prices[i][0]))
        choise_price.insert(price_button)
    return choise_price
