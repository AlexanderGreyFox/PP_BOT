import hashlib
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle

API_TOKEN = os.environ.get('BOT_TOKEN')

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class Handler:
    @dp.message_handler(commands='start')
    def start(self):
        pass

    @dp.message_handler(commands='help')
    def help(self):
        pass

    @dp.message_handler(lambda message: message.text and 'рецепт дня' in message.text.lower())
    def random_recipe(self):
        pass

    @dp.message_handler(lambda message: message.text and 'рецепт из' in message.text.lower())
    async def recipe_handler(self, message: types.Message):
        pass

    @dp.message_handler(lambda message: message.text and 'калорийность' in message.text.lower())
    async def caloric_value(self, message: types.Message):
        pass
