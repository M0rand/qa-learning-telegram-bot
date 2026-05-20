from aiogram.types import Message

from data.interview_questions import questions

from services.interview_evaluator import (
    evaluate_answer
)

from keyboards.interview_keyboard import (
    next_question_keyboard
)

interview_state = {}

interview_score = {}


async def start_interview(message: Message):

    user_id = message.from_user.id

    interview_state[user_id] = 0

    await message.answer(

        "🎤 QA Interview\n\n"
        "Я буду задавать вопросы "
        "как на QA-собеседовании.\n\n"
        "Отвечай своими словами 🔥"
    )

    first_question = questions[0]["question"]

    await message.answer(

        f"❓ Вопрос 1\n\n"
        f"{first_question}"
    )


async def ask_question(message: Message):

    user_id = message.from_user.id

    current = interview_state[user_id]

    question = questions[current]["question"]

    await message.answer(

        f"{question}"
    )


async def handle_interview_answer(
    message: Message
):

    user_id = message.from_user.id

    if user_id not in interview_state:

        return

    user_answer = message.text

    index = interview_state[user_id]

    current_question = questions[index][
        "question"
    ]

    correct_answer = questions[index][
        "answer"
    ]

    feedback = evaluate_answer(

        current_question,

        user_answer,

        correct_answer
    )

    await message.answer(

        feedback,

        reply_markup=next_question_keyboard()
    )

    

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