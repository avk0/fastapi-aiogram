from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot

from .bot import dp, bot
from .config import WEBHOOK_PATH, WEBHOOK_URL, API_PATH


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )


@app.get("/")  # to test ngrok and fastAPI to work
async def home():
    return {"message": "homepage"}


@app.post(API_PATH + "/send_message")  # to send message to chat
async def send_message(chatid: str, message: str):
    await bot.send_message(chatid, message) # to get your chatid, start the app and send /start message to bot
    return {"message": "sent success"}


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()