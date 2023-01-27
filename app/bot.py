from aiogram import Dispatcher, Bot, types

from .config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name}, chat id {message.from_user.id}")