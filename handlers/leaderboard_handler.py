from aiogram.types import Message

from services.leaderboard_service import (
    get_top_users
)


async def show_leaderboard(message: Message):

    users = get_top_users()

    text = "🏆 Топ QA студентов\n\n"

    for index, user in enumerate(users, start=1):

        username = user[0]
        xp = user[1]

        text += (
            f"{index}. {username} — {xp} XP\n"
        )

    await message.answer(text)