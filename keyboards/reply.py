from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    )


search_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🔍 Начать поиск'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


cancel_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Остановить'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


type_kb = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Аренда'),
            KeyboardButton(text='Продажа'),
        ],
        [
            KeyboardButton(text='Отменить'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


type_housing_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Квартира'),
            KeyboardButton(text='Комната'),
        ],
        [
            KeyboardButton(text='Дом'),
            KeyboardButton(text='Гараж'),
        ],
        [
            KeyboardButton(text='Земля'),
            KeyboardButton(text='Местный'),
        ],
        [
            KeyboardButton(text='Офис/Комерческое помещение'),
            KeyboardButton(text='Бизнес-Здание'),
        ],
        [
            KeyboardButton(text='Зал'),
            KeyboardButton(text='Склад'),
        ],
        [
            KeyboardButton(text='Объект общественного питания'),
            KeyboardButton(text='Киоск'),
        ],
        [
            KeyboardButton(text='Склад'),
        ],
        [
            KeyboardButton(text='Отменить'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)