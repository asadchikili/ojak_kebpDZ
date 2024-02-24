import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.types import InputFile
import sqlite3
from datetime import datetime

API_TOKEN = '6790825307:AAGQD9JLMWe6U0YWyRMAQIHBnEhhgYUvEgk'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def save_user_to_db(user):
    conn = sqlite3.connect('ojak_kebab.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id=?", (user.id,))
    existing_user = cursor.fetchone()

    if existing_user is None:
        
        cursor.execute("INSERT INTO users (id, username, first_name, last_name, date_joined) VALUES (?, ?, ?, ?, ?)",
                       (user.id, user.username, user.first_name, user.last_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        conn.commit()

    conn.close()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    save_user_to_db(message.from_user)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_menu = types.KeyboardButton("Меню")
    item_about_us = types.KeyboardButton("О нас")
    item_address = types.KeyboardButton("Адрес")
    item_order_food = types.KeyboardButton("Заказать еду")

    markup.add(item_menu, item_about_us, item_address, item_order_food)

    await message.answer("Добро пожаловать в Ojak Kebab! Как я могу помочь вам?", reply_markup=markup)

@dp.message_handler(lambda message: message.text == "Меню")
async def send_menu(message: types.Message):
    await message.answer("Вот наше меню: https://nambafood.kg/ojak-kebap")

@dp.message_handler(lambda message: message.text == "О нас")
async def send_about_us(message: types.Message):
    await message.answer("Информация о нас: https://ocak.uds.app/c/about")

@dp.message_handler(lambda message: message.text == "Адрес")
async def send_address(message: types.Message):
    await message.answer("Наш адрес: <ваш адрес>")

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
