from aiogram.types import Message

from services.user_service import (
    get_xp_db,
    get_lesson
)

from services.level_service import get_level


async def show_profile(message: Message):

    user_id = message.from_user.id

    xp = get_xp_db(user_id)

    level = get_level(xp)

    progress = get_lesson(user_id)

    await message.answer(

        f"👤 Твой профиль\n\n"

        f"🏆 Уровень: {level}\n"
        f"⭐ XP: {xp}\n"
        f"📚 Пройдено уроков: {progress - 1}\n"
    )