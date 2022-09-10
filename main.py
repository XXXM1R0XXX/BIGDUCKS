<<<<<<< HEAD
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
=======
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message, Location
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
admin_id=[919865126, 1688428776]

def vodetel():

    return
def passajir():


    return
bot = Bot(token="5600064572:AAGMkXtGIgceO06n9VOYYAbgze7dFnJPRbg")
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")




@dp.message_handler(commands=['startz'])
async def send_welcome(message: types.Message):
    await message.reply(message.chat.id)

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())
inline_btn_1 = InlineKeyboardButton('водитель!', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('пассажир!', callback_data='button2')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)

#bot.py
@dp.message_handler(commands=['1'])
async def process_command_1(message: types.Message):
    await message.answer("Выберите роль", reply_markup=inline_kb1)
@dp.callback_query_handler(text="button1")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer("1")
    vodetel()
class FSMInputName(StatesGroup):
    geo = State()
@dp.callback_query_handler(text="button2")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Подать Заявку", "Водители"]
    keyboard.add(*buttons)
    await call.message.answer("что вы хотите сделать", reply_markup=keyboard)
    @dp.callback_query_handler(text="Подать Заявку")
    async def send_random_value1(call: types.CallbackQuery):
        await call.message.answer("что вы хотите сделать", reply_markup=keyboard)



@dp.callback_query_handler(text="b")
async def edit_message_live_location(call: types.CallbackQuery, latitude: float, longitude: float):
    await call.message.answer("2")


if __name__ == '__main__':
    executor.start_polling(dp)
>>>>>>> 55a5c94 (Initial commit)
