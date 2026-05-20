from aiogram.types import (

    InlineKeyboardMarkup,

    InlineKeyboardButton
)


def answer_keyboard():

    keyboard = InlineKeyboardMarkup(

        inline_keyboard=[

            [

                InlineKeyboardButton(

                    text="1️⃣",

                    callback_data="answer:1"
                ),

                InlineKeyboardButton(

                    text="2️⃣",

                    callback_data="answer:2"
                ),

                InlineKeyboardButton(

                    text="3️⃣",

                    callback_data="answer:3"
                )
            ]
        ]
    )

    return keyboard