# rename this file to config.py

TOKEN = ""  # insert your telegram bot token

HOST = ""  # insert your ngrok host
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{HOST}{WEBHOOK_PATH}'

API_PATH = f'/api/{TOKEN}'
API_URL = f'{HOST}{API_PATH}'