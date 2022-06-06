from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, kb_MakeOrder , kb_choose, kb_sushi, kb_pizzas, kb_numb_sushi, kb_numb_pizz, kb_order_also
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# @dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'MakiMaki sushi 🍣 pizza 🍕 \n ⏰ Доставка с 10:00 до 02:00 \n 🛒 Заказывайте через нашего бота\n Или по номеру 📲 +7 775 005 40 20; +7 778 112 92 73', reply_markup=kb_client)
        await message.delete()
    except:
        message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/piz_zeriaBot')

# @dp.message_handler(commands=['buy'])
async def command_buy(message: types.Message):
        await sqlite_db.sql_read(message)
        await message.delete()


# @dp.message_handler(commands=['Меню'])
async  def menu(message: types.Message):
    await sqlite_db.sql_read(message)

# @dp.message_handler(commands=['Оставить_комментарий'])
async  def pizza_comment(message: types.Message):
    await bot.send_message(message.from_user.id, 'Можете оставить отзыв. Это поможет улучшить наш сервис', reply_markup = ReplyKeyboardRemove())

# @dp.message_handler(commands=['Сделать_заказ'])
async def pizza_make_order(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный пункт', reply_markup = kb_MakeOrder)

# @dp.message_handler(commands=['Служба_доставки'])
async  def pizza_delivery(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите что нужно', reply_markup= kb_choose)

# @dp.message_handler(commands=['Самовывоз'])
async  def pizza_pickup(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите из меню', reply_markup= kb_choose)

# @dp.message_handler(commands=['Назад'])
async  def back(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите нужный пункт', reply_markup= kb_client)

    # *********************************************** Sushi and sushi types ***********************************************

# @dp.message_handler(commands=['Суши'])
async  def sushi(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите суши', reply_markup= kb_sushi )

# @dp.message_handler(commands=['Фреш'])
async  def fresh(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите число суши', reply_markup= kb_numb_sushi )

# @dp.message_handler(commands=['Чиз_лосось'])
async  def lasos(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите число суши', reply_markup= kb_numb_sushi )

# @dp.message_handler(commands=['Чиз_крабс'])
async  def crabs(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите число суши', reply_markup= kb_numb_sushi )

# @dp.message_handler(commands=['Канада'])
async  def canada(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите число суши', reply_markup= kb_numb_sushi )

# @dp.message_handler(commands=['Киро'])
async  def kiro(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите число суши', reply_markup= kb_numb_sushi )

    #*********************************************** Pizza and  pizza types ***********************************************

# @dp.message_handler(commands=['Пицца'])
async  def pizza(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите пиццу', reply_markup= kb_pizzas )

# @dp.message_handler(commands=['Пицца_оливками'])
async  def pizz_olivki(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите число пиццы', reply_markup= kb_numb_pizz )

# @dp.message_handler(commands=['Пицца_ростбиф'])
async  def pizz_rosbif(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите число пиццы', reply_markup= kb_numb_pizz )

# @dp.message_handler(commands=['Пепперони'])
async def pepperoni(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите число пиццы', reply_markup=kb_numb_pizz)

# @dp.message_handler(commands=['Греческая'])
async def grecheskaya(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите число пиццы', reply_markup=kb_numb_pizz)

# @dp.message_handler(commands=['Вегетарианская'])
async def vegetarian(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Выберите число пиццы', reply_markup=kb_numb_pizz)


#*********************************************** Numbers of sushi ***********************************************

# @dp.message_handler(commands=['5_шт'])
async  def five(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо', reply_markup= kb_order_also )

# @dp.message_handler(commands=['10_шт'])
async  def ten(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо', reply_markup= kb_order_also )

# @dp.message_handler(commands=['15_шт'])
async def fifteen(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо', reply_markup=kb_order_also)

# @dp.message_handler(commands=['20_шт'])
async def twenty(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо', reply_markup=kb_order_also)

# @dp.message_handler(commands=['25_шт'])
async def twentyfive(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо', reply_markup=kb_order_also)

# @dp.message_handler(commands=['30_шт'])
async  def thirty(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо', reply_markup= kb_order_also )

# @dp.message_handler(commands=['35_шт'])
async  def thirtyfive(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо', reply_markup= kb_order_also )

# @dp.message_handler(commands=['40_шт'])
async def fourty(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо', reply_markup=kb_order_also)

# @dp.message_handler(commands=['45_шт'])
async def fourtyfive(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо', reply_markup=kb_order_also)

# @dp.message_handler(commands=['50_шт'])
async def fifty(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо', reply_markup=kb_order_also)

#*********************************************** Order or also ***********************************************

# @dp.message_handler(commands=['Заказать'])
async  def order(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Ваш заказ принято!!! В течений часа ваш продукт будет у вас.', reply_markup= ReplyKeyboardRemove() )

# @dp.message_handler(commands=['Еще'])
async  def also(message: types.Message):
    await  bot.send_message(message.from_user.id, 'Хотите еще либо?', reply_markup= kb_MakeOrder )



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_buy, commands=['buy'])
    dp.register_message_handler(menu, commands=['Меню'])
    dp.register_message_handler(pizza_comment, commands=['Оставить_комментарий'])
    dp.register_message_handler(pizza_make_order, commands=['Сделать_заказ'])
    dp.register_message_handler(pizza_delivery, commands=['Служба_доставки'])
    dp.register_message_handler(pizza_pickup, commands=['Самовывоз'])
    dp.register_message_handler(back, commands=['Назад'])

                    # ----Sushi----

    dp.register_message_handler(sushi, commands=['Суши'])
    dp.register_message_handler(fresh, commands=['Фреш'])
    dp.register_message_handler(lasos, commands=['Чиз_лосось'])
    dp.register_message_handler(crabs, commands=['Чиз_крабс'])
    dp.register_message_handler(canada, commands=['Канада'])
    dp.register_message_handler(kiro, commands=['Киро'])

                    #----Pizzas----

    dp.register_message_handler(pizza, commands=['Пицца'])
    dp.register_message_handler(pizz_olivki, commands=['Пицца_оливками'])
    dp.register_message_handler(pizz_rosbif, commands=['Пицца_ростбиф'])
    dp.register_message_handler(pepperoni, commands=['Пепперони'])
    dp.register_message_handler(grecheskaya, commands=['Греческая'])
    dp.register_message_handler(vegetarian, commands=['Вегетарианская'])

                        # ----Pizzas----

    dp.register_message_handler(five, commands=['5_шт'])
    dp.register_message_handler(ten, commands=['10_шт'])
    dp.register_message_handler(fifteen, commands=['15_шт'])
    dp.register_message_handler(twenty, commands=['20_шт'])
    dp.register_message_handler(twentyfive, commands=['25_шт'])
    dp.register_message_handler(thirty, commands=['30_шт'])
    dp.register_message_handler(thirtyfive, commands=['35_шт'])
    dp.register_message_handler(fourty, commands=['40_шт'])
    dp.register_message_handler(fourtyfive, commands=['45_шт'])
    dp.register_message_handler(fifty, commands=['50_шт'])

                # ---- order or also ----

    dp.register_message_handler(order, commands=['Заказать'])
    dp.register_message_handler(also, commands=['Еще'])


