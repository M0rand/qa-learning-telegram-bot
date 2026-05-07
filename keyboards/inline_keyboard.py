from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def yes_no_keyboard():

    builder = InlineKeyboardBuilder()

    builder.button(
        text="✅ Да",
        callback_data="yes"
    )

    builder.button(
        text="❌ Нет",
        callback_data="no"
    )

    builder.adjust(2)

    return builder.as_markup()