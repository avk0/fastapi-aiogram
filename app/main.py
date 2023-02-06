from fastapi import FastAPI
from pydantic import BaseModel

from . import bot as tgbot
from .config import WEBHOOK_PATH, API_PATH


# json body validation models
class MessageModel(BaseModel):
    chatid: str
    message: str

class MessagesModel(BaseModel):
    __root__: list[MessageModel]

class ImageModel(BaseModel):
    chatid: str
    img_path: str
    message: str | None = None

class ImagesModel(BaseModel):
    __root__: list[ImageModel]


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await tgbot.on_startup()

@app.on_event("shutdown")
async def on_shutdown():
    await tgbot.on_shutdown()

@app.get("/")  # test web server and fastAPI to work
async def home():
    return {"message": "homepage"}

@app.post(WEBHOOK_PATH)  # process events from webhook
async def bot_webhook(update: dict):
    await tgbot.process_update(update)


@app.post(API_PATH + "/send_message")  # send message to chat
async def send_message(chatid: str, message: str):
    await tgbot.send_message(chatid, message) # to get your chatid, start the app and send /start message to bot
    return {"message": "sent success"}

@app.post(API_PATH + "/send_image")  # send message to chat
async def send_image(chatid: str, img_path: str, message: str | None = None):
    await tgbot.send_image(chatid, img_path, message) # to get your chatid, start the app and send /start message to bot
    return {"message": "sent success"}

@app.post(API_PATH + "/send_messages")  # send message to chat
async def send_messages(send_data: MessagesModel):
    """ send_data: list of dicts 
        [{"chatid": id, "message": msg}, ...] """
    for data in send_data.__root__:
        await send_message(data.chatid, data.message)
    return {"message": "sent success"}

@app.post(API_PATH + "/send_images")  # send message to chat
async def send_images(send_data: ImagesModel):
    """ send_data: list of dicts 
        [{"chatid": id, "img_path": img_path, "message": msg}, ...] """
    for data in send_data.__root__:
        await send_image(data.chatid, data.img_path, data.message)
    return {"message": "sent success"}