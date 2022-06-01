from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='5129293489:AAEz9j89AveDwlYf20GUe8XxPXAKkV1JW9k')
dp = Dispatcher(bot)

#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
urlkb.add(urlButton, urlButton2)

@dp.message_handler(commands='ссылки')
async def url_command(message : types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)

executor.start_polling(dp, skip_updates=True)
