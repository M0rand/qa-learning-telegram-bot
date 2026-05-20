import sqlite3

from aiogram.types import Message

from services.user_service import (
    get_xp_db,
)

from services.level_service import get_level

def get_total_completed_lessons(

    user_id
):

    conn = sqlite3.connect(
        "qa_bot.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT COUNT(*)

        FROM completed_lessons

        WHERE user_id = ?
        """,

        (user_id,)
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count

async def show_profile(message: Message):

    user_id = message.from_user.id

    xp = get_xp_db(user_id)

    level = get_level(xp)

    completed_lessons = get_total_completed_lessons(

        user_id
    )

    await message.answer(

        f"👤 Твой профиль\n\n"

        f"🏆 Уровень: {level}\n"
        f"⭐ XP: {xp}\n"
        f"📚 Пройдено уроков: {completed_lessons}\n"
    )