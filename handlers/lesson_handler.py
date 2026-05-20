from aiogram.types import (
    Message,
    CallbackQuery
)

from data.blocks import blocks

from keyboards.block_keyboard import (
    block_keyboard
)

from keyboards.continue_keyboard import (
    continue_keyboard
)

from keyboards.next_block_keyboard import (
    next_block_keyboard
)

from keyboards.answer_keyboard import (
    answer_keyboard
)

from services.user_service import (

    add_xp_db,

    complete_lesson,

    is_lesson_completed,

    get_completed_lessons_count
)

from services.progress_service import (
    generate_progress_bar
)

user_state = {}

block_order = list(

    blocks.keys()
)

async def start_lesson(
    message: Message
):

    text = (

        "📚 Выбери раздел\n\n"

        "👇 Доступные блоки:"
    )

    await message.answer(

        text,

        reply_markup=block_keyboard()
    )


async def select_block(
    callback: CallbackQuery
):

    user_id = callback.from_user.id

    block_id = callback.data.split(":")[1]

    user_state[user_id] = {

        "block": block_id,

        "lesson": 0
    }

    await send_lesson(

        callback.message,

        user_id
    )

    await callback.answer()


async def send_lesson(
    message,
    user_id
):

    state = user_state[user_id]

    block_id = state["block"]

    lesson_index = state["lesson"]

    block = blocks[block_id]

    lessons = block["lessons"]

    lesson = lessons[lesson_index]

    completed = get_completed_lessons_count(

        user_id,

        block_id
    )

    display_progress = completed

    if display_progress >= len(lessons):

        display_progress = len(lessons) - 1

    progress = generate_progress_bar(

        display_progress,

        len(lessons)
    )

    if "options" in lesson:

        options_text = "\n\n"

        for index, option in enumerate(

            lesson["options"],

            start=1
        ):

            options_text += (

                f"{index}️⃣ {option}\n"
            )

    else:

        options_text = ""


    text = (

        f"{block['title']}\n\n"

        f"📚 Урок "
        f"{lesson_index + 1} "
        f"из {len(lessons)}\n\n"

        f"📈 Прогресс:\n"
        f"{progress}\n\n"

        f"🧠 Главное:\n"
        f"{lesson['theory']}\n\n"

        f"💡 Пример:\n"
        f"{lesson['example']}\n\n"

        f"❓ Вопрос:\n"
        f"{lesson['question']}\n"

        f"{options_text}"
    )

    await message.answer(

        text,

        reply_markup=answer_keyboard()
    )


async def handle_answer(
    message: Message
):

    user_id = message.from_user.id

    if user_id not in user_state:

        await message.answer(

            "Нажми 📚 Учиться"
        )

        return

    state = user_state[user_id]

    block = blocks[state["block"]]

    lessons = block["lessons"]

    lesson = lessons[state["lesson"]]

    user_answer = message.text.strip()

    correct = lesson["correct"]

    if user_answer == correct:

        already_completed = is_lesson_completed(

            user_id,

            state["block"],

            state["lesson"]
        )

        if not already_completed:

            add_xp_db(

                user_id,

                lesson["xp"]
            )

            complete_lesson(

                user_id,

                state["block"],

                state["lesson"]
            )

            xp_text = (

                f"⭐ +{lesson['xp']} XP"
            )

        else:

            xp_text = (

                "✅ XP уже получен "
                "за этот урок"
            )

        text = (

            "🎉 Отлично!\n\n"

            f"📘 Объяснение:\n"
            f"{lesson['explanation']}\n\n"

            f"{xp_text}"
        )

    else:

        text = (

            "❌ Пока неверно\n\n"

            f"📘 Объяснение:\n"
            f"{lesson['explanation']}"
        )

    if user_answer == correct:

        await message.answer(

            text,

            reply_markup=continue_keyboard()
        )

    else:

        await message.answer(text)

async def continue_lesson(
    callback: CallbackQuery
):

    user_id = callback.from_user.id

    if user_id not in user_state:

        await callback.answer()

        return

    state = user_state[user_id]

    block = blocks[state["block"]]

    lessons = block["lessons"]

    state["lesson"] += 1

    if state["lesson"] >= len(lessons):

        final_progress = generate_progress_bar(

            len(lessons),

            len(lessons)
        )
        
        await callback.message.answer(

            "🏆 Блок завершён!\n\n"

            f"{final_progress}\n\n"

            f"Ты прошёл:\n"
            f"{block['title']}",

            reply_markup=next_block_keyboard()
        )

        await callback.answer()

        return

    await send_lesson(

        callback.message,

        user_id
    )

    await callback.answer()

async def next_block(
    callback: CallbackQuery
):

    user_id = callback.from_user.id

    if user_id not in user_state:

        await callback.answer()

        return

    state = user_state[user_id]

    current_block = state["block"]

    current_index = block_order.index(
        current_block
    )

    next_index = current_index + 1

    if next_index >= len(block_order):

        await callback.message.answer(

            "🎉 Ты прошёл все блоки!"
        )

        del user_state[user_id]

        await callback.answer()

        return

    next_block_id = block_order[
        next_index
    ]

    next_block_lessons = blocks[
        next_block_id
    ]["lessons"]

    if not next_block_lessons:

        await callback.message.answer(

            "🚧 Этот блок "
            "ещё в разработке"
        )

        await callback.answer()

        return

    user_state[user_id] = {

        "block": next_block_id,

        "lesson": 0
    }

    await send_lesson(

        callback.message,

        user_id
    )

    await callback.answer()