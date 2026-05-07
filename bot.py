import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from keyboards.main_menu import main_menu

from handlers.lesson_handler import (
    start_lesson,
    handle_answer
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

TOKEN = "8722440828:AAH3tmQ8FSt6Ral6fahztSo6qJRbFUgNHso"

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

@dp.callback_query()
async def lesson_callback(callback: CallbackQuery):

    print("CALLBACK WORKS")

    if callback.data == "yes":

        user_answer = "да"

    else:

        user_answer = "нет"

    class FakeMessage:
        def __init__(self, text, from_user, answer_method):
            self.text = text
            self.from_user = from_user
            self.answer = answer_method

    fake_message = FakeMessage(
        text=user_answer,
        from_user=callback.from_user,
        answer_method=callback.message.answer
    )

    await handle_answer(fake_message)

    await callback.answer()

@dp.message(lambda message: message.text == "🏆 Рейтинг")
async def leaderboard(message: Message):

    await show_leaderboard(message)
    
#@dp.message()
#async def answer(message: Message):

#    user_id = message.from_user.id

#    if user_id in interview_state:

#        await handle_interview_answer(message)

#    else:

#        await handle_answer(message)


async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())