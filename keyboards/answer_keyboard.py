from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

answer_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ]
    ],
    resize_keyboard=True
)