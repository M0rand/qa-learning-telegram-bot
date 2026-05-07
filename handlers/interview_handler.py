from aiogram.types import Message

from data.interview_questions import questions


interview_state = {}

interview_score = {}


async def start_interview(message: Message):

    user_id = message.from_user.id

    interview_state[user_id] = 0
    interview_score[user_id] = 0

    await message.answer(

        "🎤 QA Interview\n\n"
        "Я буду задавать вопросы как на QA-собеседовании.\n\n"
        "Отвечай своими словами 🔥"
    )

    await ask_question(message)


async def ask_question(message: Message):

    user_id = message.from_user.id

    current = interview_state[user_id]

    question = questions[current]["question"]

    await message.answer(

        f"❓ Вопрос {current + 1}\n\n"
        f"{question}"
    )


async def handle_interview_answer(message: Message):

    user_id = message.from_user.id

    current = interview_state[user_id]

    correct_answer = questions[current]["answer"]

    user_answer = message.text.lower()

    if len(user_answer) > 5:

        interview_score[user_id] += 1

        await message.answer(

            "✅ Ответ принят\n\n"
            f"💡 Пример хорошего ответа:\n"
            f"{correct_answer}"
        )

    else:

        await message.answer(

            "❌ Ответ слишком короткий"
        )

    interview_state[user_id] += 1

    next_question = interview_state[user_id]

    if next_question < len(questions):

        await ask_question(message)

    else:

        score = interview_score[user_id]

        await message.answer(

            f"🏆 Interview Finished\n\n"
            f"Твой результат: {score}/{len(questions)}\n\n"
            "🔥 Продолжай обучение!"
        )

        del interview_state[user_id]