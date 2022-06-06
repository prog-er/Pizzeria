from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='5129293489:AAEz9j89AveDwlYf20GUe8XxPXAKkV1JW9k')
dp = Dispatcher(bot)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Купить', callback_data='www'))

@dp.message_handler(commands='test')
async def test_commands(message: types.Message):
    await message.answer('Инлайн кнопка', reply_markup=inkb)

@dp.callback_query_handler(text='www')
async def www_call(callback: types.CallbackQuery):
    await callback.answer('Куплена!!!')

executor.start_polling(dp, skip_updates=True)
