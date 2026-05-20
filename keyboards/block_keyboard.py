from aiogram.types import (

    InlineKeyboardMarkup,

    InlineKeyboardButton
)

from data.blocks import blocks


def block_keyboard():

    keyboard = []

    for block_id, block_data in blocks.items():

        keyboard.append(

            [

                InlineKeyboardButton(

                    text=block_data["title"],

                    callback_data=f"block:{block_id}"
                )
            ]
        )

    return InlineKeyboardMarkup(

        inline_keyboard=keyboard
    )