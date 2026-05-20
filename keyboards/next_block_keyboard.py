from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def next_block_keyboard():

    return InlineKeyboardMarkup(

        inline_keyboard=[

            [
                InlineKeyboardButton(

                    text="➡️ Следующий блок",

                    callback_data="next_block"
                )
            ]
        ]
    )