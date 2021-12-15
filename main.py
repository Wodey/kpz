import json
import logging
from aiogram import Bot, executor, Dispatcher
from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv('API_TOKEN')

questions = {}

with open("questions.json", 'r', encoding="utf-8") as qst:
    raw_data = json.load(qst)
    questions = raw_data['questions']
    intro = raw_data['intro']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await bot.sendMessage(message.from_user.id, intro['body'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

