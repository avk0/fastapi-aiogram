from aiogram import Dispatcher, Bot, types

from .config import TOKEN, WEBHOOK_URL

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup():
    await bot.set_webhook(url=WEBHOOK_URL)


async def process_update(update):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name}, chat id {message.from_user.id}")


async def send_message(chatid: str, message: str):
    await bot.send_message(chatid, message) # to get your chatid, start the app and send /start message to bot


async def on_shutdown():
    await bot.session.close()