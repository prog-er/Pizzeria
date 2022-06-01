from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='5129293489:AAEz9j89AveDwlYf20GUe8XxPXAKkV1JW9k')
dp = Dispatcher(bot, storage=storage)

