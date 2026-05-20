import asyncio

import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from keyboards.main_menu import main_menu

from handlers.lesson_handler import (

    start_lesson,

    handle_answer,

    select_block,

    continue_lesson,

    next_block,

    user_state
)

from handlers.profile_handler import show_profile

from handlers.interview_handler import (
    start_interview,
    handle_interview_answer,
    interview_state
)

from handlers.leaderboard_handler import (
    show_leaderboard
)

from data.interview_questions import (
    questions
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):

    await message.answer(

        "👋 Добро пожаловать в QA Academy\n\n"

        "Ты научишься:\n"
        "• понимать тестирование\n"
        "• находить баги\n"
        "• писать тест-кейсы\n"
        "• проходить собеседования\n\n"

        "🏆 Твой путь:\n"
        "Intern → Junior → Middle → Senior\n\n"

        "Выбери действие 👇",

        reply_markup=main_menu
    )

@dp.message(lambda message: message.text == "📚 Учиться")
async def learn(message: Message):

    await start_lesson(message)

@dp.message(lambda message: message.text == "👤 Профиль")
async def profile_button(message: Message):

    await show_profile(message)

@dp.message(lambda message: message.text == "🎤 Собеседование")
async def interview(message: Message):

    await start_interview(message)

@dp.message(Command("profile"))
async def profile(message: Message):

    await show_profile(message)

@dp.message(lambda message: message.text == "🏆 Рейтинг")
async def leaderboard(message: Message):

    await show_leaderboard(message)

@dp.callback_query(
    lambda c: c.data.startswith("block:")
)
async def block_selection(
    callback: CallbackQuery
):

    await select_block(callback)

@dp.callback_query(
    lambda c: c.data == "continue_lesson"
)
async def continue_callback(
    callback: CallbackQuery
):

    await continue_lesson(callback)

@dp.callback_query(
    lambda c: c.data == "next_block"
)
async def next_block_callback(
    callback: CallbackQuery
):

    await next_block(callback)

@dp.message()
async def fallback(message: Message):

    user_id = message.from_user.id

    if user_id in interview_state:

        await handle_interview_answer(message)

        return

    await message.answer(

        "Используй кнопки меню 👇"
    )

@dp.callback_query(
    lambda c: c.data == "next_question"
)
async def next_interview_question(
    callback: CallbackQuery
):

    user_id = callback.from_user.id

    if user_id not in interview_state:

        await callback.answer()

        return

    interview_state[user_id] += 1

    index = interview_state[user_id]

    if index >= len(questions):

        await callback.message.answer(

            "🏆 Собеседование завершено!"
        )

        del interview_state[user_id]

        await callback.answer()

        return

    question = questions[index][
        "question"
    ]

    await callback.message.answer(

        f"❓ Вопрос {index + 1}\n\n"
        f"{question}"
    )

    await callback.answer()

@dp.callback_query(
    lambda c: c.data.startswith(
        "answer:"
    )
)
async def answer_callback(
    callback: CallbackQuery
):

    answer = callback.data.split(":")[1]

    class FakeMessage:

        def __init__(
            self,
            text,
            from_user,
            answer_method
        ):

            self.text = text
            self.from_user = from_user
            self.answer = answer_method

    fake_message = FakeMessage(

        text=answer,

        from_user=callback.from_user,

        answer_method=callback.message.answer
    )
    
    await handle_answer(fake_message)

    await callback.answer()

async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())