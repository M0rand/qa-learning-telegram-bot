from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def continue_keyboard():

    return InlineKeyboardMarkup(

        inline_keyboard=[

            [
                InlineKeyboardButton(

                    text="➡️ Продолжить",

                    callback_data="continue_lesson"
                )
            ]
        ]
    )