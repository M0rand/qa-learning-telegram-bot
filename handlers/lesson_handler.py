from aiogram.types import Message
from aiogram.filters import CommandStart

from data.lessons import lessons
from keyboards.inline_keyboard import yes_no_keyboard
from services.user_service import (
    create_user,
    add_xp_db,
    set_lesson
)

from services.user_service import create_user

from services.achievement_service import (
    unlock_achievement
)

from services.streak_service import update_streak

user_state = {}

async def start_lesson(message: Message):
    create_user(

        message.from_user.id,

        message.from_user.first_name
    )
    
    
    user_state[message.from_user.id] = 1

    lesson = lessons[1]

    streak = update_streak(
        message.from_user.id
    )
    await message.answer(
        f"🔥 Серия дней: {streak}\n\n"
        f"📚 {lesson['title']}\n\n"
        f"📖 Теория:\n{lesson['theory']}\n\n"
        f"💡 Пример:\n{lesson['example']}\n\n"
        f"❓ Вопрос:\n{lesson['question']}",
        reply_markup=yes_no_keyboard()
    )


async def handle_answer(message: Message):

    state = user_state.get(message.from_user.id)

    if not state:

        await message.answer("Нажми 📚 Учиться")
        return

    lesson = lessons.get(state)

    if message.text.lower() == lesson["correct"]:

        # XP
        add_xp_db(
            message.from_user.id,
            lesson["xp"]
        )

    # Achievement за первый урок
        if state == 1:

            achievement = unlock_achievement(
                message.from_user.id,
                "first_lesson"
            )

            if achievement:

                await message.answer(

                    f"🏆 Новая ачивка!\n\n"
                    f"{achievement['title']}\n"
                    f"{achievement['description']}"
                )

    # Achievement за XP
        from services.user_service import get_xp_db

        current_xp = get_xp_db(
            message.from_user.id
        )

        if current_xp >= 50:

            achievement = unlock_achievement(
                message.from_user.id,
                "xp_50"
            )

            if achievement:

                await message.answer(

                    f"🏆 Новая ачивка!\n\n"
                    f"{achievement['title']}"
                )

        await message.answer(

            f"{lesson['success']}\n\n"
            f"⭐ XP начислен: +{lesson['xp']}"
        )

        next_lesson = state + 1

        if next_lesson in lessons:

            user_state[message.from_user.id] = next_lesson

            set_lesson(
                message.from_user.id,
                next_lesson
            )

            next_data = lessons[next_lesson]

            await message.answer(

                f"📚 {next_data['title']}\n\n"

                f"📖 Теория:\n"
                f"{next_data['theory']}\n\n"

                f"💡 Пример:\n"
                f"{next_data['example']}\n\n"

                f"❓ Вопрос:\n"
                f"{next_data['question']}",

                reply_markup=yes_no_keyboard()
            )

        else:

            await message.answer(

                "🏆 Поздравляю!\n\n"
                "Ты прошёл все уроки 🚀"
            )

    else:

        await message.answer(

            "❌ Неверно, попробуй ещё"
        )