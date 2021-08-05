from aiogram.utils.callback_data import CallbackData

# Инфа после выбора "Новой подписки"
new_follow_callback = CallbackData("new", "clown")

# Инфа после выбора нужной марки
choise_mark_callback = CallbackData("mark", "mark_id")

# Инфа после выбора нужной цены
choise_price_callback = CallbackData("price", "mark_id", "price_id")

# Инфа для удаления подписки
unfollow_callback = CallbackData("unfollow", "id_follow")