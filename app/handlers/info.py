from aiogram import types
from bot import dp

@dp.message_handler(commands="info")
async def info(message: types.Message):
    await message.answer("Чтобы посмотреть активные подписки или создать новые используйте команду /follows\n"
                         "Чтобы отписаться от всех подписок разом используйте команду /stop \n"
                         "Чтобы вывести список автомобилей по подписке используйте команду /avito")

