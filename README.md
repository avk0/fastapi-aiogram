# fastapi-aiogram

To run:
1. Create Telegram bot (with BotFather) and get bot token
2. Download and run [ngrok](https://ngrok.com/download) 
3. In ngrok shell run `ngrok http 8000` and get ngrok host from a field `Forwarding` (for example: https://bfs2-83-28-107-121.eu.ngrok.io)
4. Install dependencies `pip install aiogram fastapi uvicorn`
5. Rename `config_default.py` to `config.py`
6. Insert ngrok host and bot token to `config.py` file
7. In terminal inside the project folder run `uvicorn app.main:app`

To test:
1. Start conversation with bot by sending him `/start` message and get your `chatid` in bot reply message
2. Use API to send messages from bot
`curl -X POST 'https://YOUR_NGROK_HOST/api/YOUR_BOT_TOKEN/send_message?chatid=YOUR_CHAT_ID&message=any_test_message'`
