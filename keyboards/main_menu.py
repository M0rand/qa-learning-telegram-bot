from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(

    keyboard=[

        [
            KeyboardButton(text="📚 Учиться")
        ],

        [
            KeyboardButton(text="👤 Профиль")
        ],

        [
            KeyboardButton(text="🎤 Собеседование")
        ],
        
        [
            KeyboardButton(text="🏆 Рейтинг")
        ]
    ],

    resize_keyboard=True
)