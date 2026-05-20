def evaluate_answer(
    question,
    user_answer,
    correct_answer
):

    user_answer = user_answer.lower()

    keywords = correct_answer.lower().split()

    matches = 0

    for word in keywords:

        if word in user_answer:

            matches += 1

    score = int(
        (matches / len(keywords)) * 10
    )

    if score >= 8:

        feedback = (
            "✅ Отличный ответ!"
        )

    elif score >= 5:

        feedback = (
            "👍 Неплохой ответ.\n"
            "Но можно подробнее."
        )

    else:

        feedback = (
            "❌ Слабый ответ.\n"
            "Попробуй раскрыть тему глубже."
        )

    missing_words = []

    for word in keywords:

        if word not in user_answer:

            missing_words.append(word)

    tips = ""

    if missing_words:

        tips = (
            "\n\n💡 Добавь слова:\n"
            + ", ".join(
                missing_words[:3]
            )
        )

    return (

        f"🧠 Оценка: {score}/10\n\n"

        f"{feedback}"

        f"{tips}"
    )