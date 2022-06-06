from aiogram import types
from create_bot import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



    #---Main buttons----

b1 = KeyboardButton('/Сделать_заказ')
b2 = KeyboardButton('/Оставить_комментарий')
b3 = KeyboardButton('/Меню')
#b4 = KeyboardButton('Поделиться номером', request_contact=True)
#b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).row(b2, b3)

     #---При нажатий на сделать заказ----

btnDelivery = KeyboardButton('/Служба_доставки', request_location=True)
btnPickup = KeyboardButton('/Самовывоз')
btnMain = KeyboardButton('/Назад')

kb_MakeOrder = ReplyKeyboardMarkup(resize_keyboard=True)
kb_MakeOrder.add(btnDelivery, btnPickup, btnMain)

        #---Пица или сущи ----

btn_sushi = KeyboardButton('/Суши')
btn_pizza = KeyboardButton('/Пицца')

kb_choose = ReplyKeyboardMarkup(resize_keyboard=True)
kb_choose.row(btn_sushi, btn_pizza)

        #---Pizza----

btn_olivka = KeyboardButton('/Пицца_оливками')#, row_width=2)
btn_rostbif = KeyboardButton('/Пицца_ростбиф')
btn_pepperoni = KeyboardButton('/Пепперони')
btn_greek = KeyboardButton('/Греческая')
btn_vegetarian = KeyboardButton('/Вегетарианская')

kb_pizzas = ReplyKeyboardMarkup(resize_keyboard=True)
kb_pizzas.add(btn_olivka, btn_rostbif, btn_pepperoni, btn_greek, btn_vegetarian)

        # ---Пицца_оливками----



        #---Sushi----

btn_fresh = KeyboardButton('/Фреш')
btn_cheese_losos = KeyboardButton('/Чиз_лосось')
btn_cheese_crabs = KeyboardButton('/Чиз_крабс')
btn_canada = KeyboardButton('/Канада')
btn_kiro = KeyboardButton('/Киро')

kb_sushi = ReplyKeyboardMarkup(resize_keyboard=True)
kb_sushi.add(btn_fresh, btn_cheese_losos, btn_cheese_crabs, btn_canada, btn_kiro)


        # ---Сколько суши----

btns1 = KeyboardButton('/5_шт')
btns2 = KeyboardButton('/10_шт')
btns3 = KeyboardButton('/15_шт')
btns4 = KeyboardButton('/20_шт')
btns5 = KeyboardButton('/25_шт')
btns6 = KeyboardButton('/30_шт')
btns7 = KeyboardButton('/35_шт')
btns8 = KeyboardButton('/40_шт')
btns9 = KeyboardButton('/45_шт')
btns10 = KeyboardButton('/50_шт')

kb_numb_sushi = ReplyKeyboardMarkup(resize_keyboard=True)
kb_numb_sushi.add(btns1, btns2, btns3, btns4, btns5, btns6, btns7, btns8, btns9, btns10)

        # ---Сколько пицц----

btnp1 = KeyboardButton('/1_шт')
btnp2 = KeyboardButton('/2_шт')
btnp3 = KeyboardButton('/3_шт')
btnp4 = KeyboardButton('/4_шт')
btnp5 = KeyboardButton('/5_шт')
btnp6 = KeyboardButton('/6_шт')
btnp7 = KeyboardButton('/7_шт')
btnp8 = KeyboardButton('/8_шт')
btnp9 = KeyboardButton('/9_шт')
btnp10 = KeyboardButton('/10_шт')

kb_numb_pizz = ReplyKeyboardMarkup(resize_keyboard=True)
kb_numb_pizz.add(btnp1, btnp2, btnp3, btnp4, btnp5, btnp6, btnp7, btnp8, btnp9, btnp10)

# --- Заказать или еще ----
btn_order = KeyboardButton('/Заказать')
btn_also = KeyboardButton('/Еще')

kb_order_also = ReplyKeyboardMarkup(resize_keyboard=True)
kb_order_also.add(btn_order, btn_also)

        #---Menu----

btn_Menu = KeyboardButton('/Меню')
kb_Menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_Menu.add(btn_Menu)

      #---Inline keyboard----
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Заказать', callback_data='www'))

@dp.message_handler(commands='test')
async def test_commands(message: types.Message):
    await message.answer('Инлайн кнопка', reply_markup=inkb)

@dp.callback_query_handler(text='www')
async def www_call(callback: types.CallbackQuery):
    await callback.answer('Заказано!!!')