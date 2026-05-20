from aiogram.utils.keyboard import (
    InlineKeyboardBuilder
)


def next_question_keyboard():

    builder = InlineKeyboardBuilder()

    builder.button(

        text="➡️ Дальше",

        callback_data="next_question"
    )

    return builder.as_markup()