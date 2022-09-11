from aiogram import types, Bot
from getpass import getpass
from mysql.connector import connect, Error
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message, Location
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3, logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from random import randint
import mysql.connector

logging.basicConfig(level=logging.INFO)
conn = sqlite3.connect('Social Taxi.db')
cur = conn.cursor()
admin_id = [919865126, 1688428776]



def vodetel():
    return


def passajir():
    return


bot = Bot(token="5600064572:AAGMkXtGIgceO06n9VOYYAbgze7dFnJPRbg")
dp = Dispatcher(bot, storage=MemoryStorage())

inline_btn_1 = InlineKeyboardButton('Водитель!', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Пассажир!', callback_data='button2')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)


# bot.py
@dp.message_handler(commands=['start'])
async def process_command_11(message: types.Message):
    cur.execute(
        "SELECT count(*) FROM people WHERE chat_id=?", (message.chat.id,))
    if cur.fetchone()[0] == 1:
        await message.answer("Выбирите роль", reply_markup=inline_kb1)
        return
    else:
        await message.answer("Прежде чем перейти к делу давай познакомимся: Как тебя зовут?")

        @dp.message_handler(content_types=["text"])
        async def process_command_1(message: types.Message):
            chatidd = message.chat.id
            name = message.text
            await message.answer(f"Привет {name}, поделись своим контактом")
            await bot.copy_message(from_chat_id=919865126, chat_id=chatidd, message_id=1715)

            @dp.message_handler(content_types=["contact"])
            async def process_command_1(message: types.Message):
                number = message.contact.phone_number
                usernamee = message.from_user.username
                user = (chatidd, number, name, '@' + usernamee)
                cur.execute("INSERT INTO people VALUES(?, ?, ?, ?);", user)
                conn.commit()
                await message.answer("Вы успешно прошли регистрацию")
                await message.answer("Выбирите роль", reply_markup=inline_kb1)
                return


@dp.callback_query_handler(text="button1")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Поиск по заявкам"]
    keyboard.add(*buttons)
    await call.message.answer("Что вы хотите сделать?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Поиск по заявкам")
async def without_puree(message: types.Message):
    await message.answer("Введите никнейм пассажира из карты, Пример: @telegram")

    @dp.message_handler(content_types=['text'])
    async def handle_location11(message: types.Message):
        global chat_id2, chat_id, message_id1, message_id2, number
        chat_id2 = message.from_user.id
        cur.execute(
            "SELECT count(*) FROM PAS WHERE username=?", (message.text,))
        if cur.fetchone()[0]==0:
            await message.answer("Такой завки нет")
        else:
            cur.execute(
                "SELECT chat_id FROM PAS WHERE username=?", (message.text,))
            chat_id = cur.fetchone()[0]
            cur.execute(
                "SELECT message_id1 FROM PAS WHERE username=?", (message.text,))
            message_id1 = cur.fetchone()[0]
            cur.execute(
                "SELECT message_id2 FROM PAS WHERE username=?", (message.text,))
            message_id2 = cur.fetchone()[0]
            cur.execute(
                "SELECT number FROM people WHERE chat_id=?", (chat_id2,))
            number=cur.fetchone()[0]
            cur.execute(
                "SELECT name FROM people WHERE chat_id=?", (chat_id2,))
            name=cur.fetchone()[0]
            await message.answer("Начальная точка")
            await bot.copy_message(from_chat_id=chat_id, chat_id=chat_id2, message_id=message_id1)
            await message.answer("Конечная точка")
            taxist = message.chat.username
            await bot.copy_message(from_chat_id=chat_id, chat_id=chat_id2, message_id=message_id2)
            inline_btn_1 = InlineKeyboardButton('Принять!', callback_data='button11')
            inline_btn_2 = InlineKeyboardButton('Отклонить!', callback_data='button22')
            inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)
            await message.answer("Выберите вариант", reply_markup=inline_kb1)

            @dp.callback_query_handler(text="button11")
            async def send_random_value11(call: types.CallbackQuery):
                await bot.send_message(chat_id, f"Ваш заказ принял водитель {name},контакты для связи: @{taxist}, +{number}")
                cur.execute("DELETE FROM PAS WHERE chat_id=?", (chat_id,))
                conn.commit()

                @dp.message_handler(content_types=["text"])
                async def process_command_166(message: types.Message):
                    if chat_id == message.chat.id:
                        await bot.send_message(chat_id2, message.text)
                    else:
                        await bot.send_message(chat_id, message.text)

            @dp.callback_query_handler(text="button22")
            async def send_random_value11(call: types.CallbackQuery):
                await bot.send_message(chat_id2, "Заказ отклонен")

@dp.message_handler(content_types=["photo"])
async def video_and_text_id(message: types.Message):
    await message.answer(message.message_id)
@dp.message_handler(lambda message: message.text == "карта")
async def without_puree(message: types.Message):
    await message.answer("")


# ---------------------------------------------------------------------------------------------------


@dp.callback_query_handler(text="button2")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Подать заявку"]
    keyboard.add(*buttons)
    await call.message.answer("Что вы хотите сделать?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Подать заявку")
async def without_puree(message: types.Message):
    cur.execute(
        "SELECT count(*) FROM PAS WHERE chat_id=?", (message.chat.id,))
    if cur.fetchone()[0] == 1:
        await message.answer("Вы уже подали завку,отмените ее или подождите пока ее примут")
    else:

        await message.answer("Отправьте геопозицию начала поездки")
        await bot.copy_message(from_chat_id=919865126, chat_id=message.chat.id, message_id=2008)
        await bot.copy_message(from_chat_id=919865126, chat_id=message.chat.id, message_id=2007)
        global g
        g = 0

        @dp.message_handler(content_types=['location'])
        async def handle_location(message: types.Message):
            global g
            if g == 0:
                global lat1, lon1, chatid, msgid1, msgid2

                lat1 = message.location.latitude
                lon1 = message.location.longitude
                chatid = message.chat.id
                msgid1 = message.message_id
                await message.answer("Отправьте геопозицию конца поездки")
                g += 1
            elif chatid == message.chat.id:
                msgid2 = message.message_id
                lat2 = message.location.latitude
                lon2 = message.location.longitude
                user = (lat1, lon1, chatid, msgid1, lat2, lon2, msgid2, '@' + message.chat.username)
                cur.execute("INSERT INTO PAS VALUES(?, ?, ?, ?, ?, ?, ?, ?);", user)
                conn.commit()
                g = 0
                inline_btn_222 = InlineKeyboardButton('Отклонить!', callback_data='button222')
                inline_kb111 = InlineKeyboardMarkup().add(inline_btn_222)
                await message.answer("Заявка создана", reply_markup=inline_kb111)

                @dp.callback_query_handler(text="button222")
                async def send_random_value11(call: types.CallbackQuery):
                    cur.execute("DELETE FROM PAS WHERE chat_id=?", (chatid,))
                    conn.commit()
                    await message.answer("Заявка отклонена")
            else:
                await message.answer("Error: Попробуйте подать заявку еще раз (сорри)")


# ------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    executor.start_polling(dp)
