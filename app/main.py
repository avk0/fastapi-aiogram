from fastapi import FastAPI

from . import bot as tgbot
from .config import WEBHOOK_PATH, API_PATH


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await tgbot.on_startup()


@app.get("/")  # test ngrok and fastAPI to work
async def home():
    return {"message": "homepage"}


@app.post(WEBHOOK_PATH)  # process events from webhook
async def bot_webhook(update: dict):
    await tgbot.process_update(update)


@app.post(API_PATH + "/send_message")  # send message to chat
async def send_message(chatid: str, message: str):
    await tgbot.send_message(chatid, message) # to get your chatid, start the app and send /start message to bot
    return {"message": "sent success"}


@app.on_event("shutdown")
async def on_shutdown():
    await tgbot.shutdown()