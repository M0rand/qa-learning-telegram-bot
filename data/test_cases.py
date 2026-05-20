test_cases = [

    {
        "title": "Что такое test case",

        "theory": (

            "🧪 Test case — это подробный сценарий проверки.\n\n"

            "Он помогает QA проверять систему одинаково\n"
            "и ничего не забывать.\n\n"

            "Обычно test case содержит:\n"
            "• шаги\n"
            "• тестовые данные\n"
            "• expected result\n\n"

            "Test cases особенно важны\n"
            "в больших проектах."
        ),

        "example": (

            "1. Открыть login page\n"
            "2. Ввести email\n"
            "3. Ввести password\n"
            "4. Нажать Login"
        ),

        "question": (
            "Что такое test case?"
        ),

        "options": [

            "Bug report",

            "Сценарий тестирования",

            "Тип браузера"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "Test case описывает,\n"
            "как именно проверять систему."
        ),

        "xp": 20
    },

    {
        "title": "Steps to reproduce",

        "theory": (

            "📋 Steps to reproduce —\n"
            "это последовательность действий,\n"
            "которые нужно выполнить.\n\n"

            "Они помогают:\n"
            "• повторить баг\n"
            "• проверить функционал\n"
            "• понять проблему\n\n"

            "Шаги должны быть:\n"
            "• понятными\n"
            "• короткими\n"
            "• последовательными"
        ),

        "example": (

            "1. Open app\n"
            "2. Click Login\n"
            "3. App crashes"
        ),

        "question": (
            "Для чего нужны steps?"
        ),

        "options": [

            "Для повторения сценария",

            "Для изменения дизайна",

            "Для настройки браузера"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Steps помогают повторить\n"
            "действия пользователя."
        ),

        "xp": 20
    },

    {
        "title": "Expected result",

        "theory": (

            "🎯 Expected result показывает,\n"
            "как система должна работать.\n\n"

            "QA заранее определяет,\n"
            "какой результат считается правильным.\n\n"

            "Это помогает понять:\n"
            "есть баг или нет."
        ),

        "example": (
            "User successfully logs into account."
        ),

        "question": (
            "Что показывает expected result?"
        ),

        "options": [

            "Ожидаемое поведение системы",

            "Настройки сервера",

            "Имя разработчика"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Expected result показывает,\n"
            "как система должна работать."
        ),

        "xp": 20
    },

    {
        "title": "Actual result",

        "theory": (

            "📌 Actual result показывает,\n"
            "что произошло на самом деле.\n\n"

            "QA сравнивает actual result\n"
            "с expected result.\n\n"

            "Если результаты отличаются —\n"
            "значит найден баг."
        ),

        "example": (
            "Application shows error 500."
        ),

        "question": (
            "Что показывает actual result?"
        ),

        "options": [

            "Ожидаемый результат",

            "Фактический результат",

            "Тип тестирования"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "Actual result —\n"
            "это реальное поведение системы."
        ),

        "xp": 20
    },

    {
        "title": "Positive test case",

        "theory": (

            "✅ Positive test case проверяет,\n"
            "что система работает правильно.\n\n"

            "Используются валидные данные:\n"
            "• правильный password\n"
            "• корректный email\n"
            "• валидная карта оплаты\n\n"

            "Это основной happy path сценарий."
        ),

        "example": (
            "Пользователь вводит правильный password."
        ),

        "question": (
            "Что проверяет positive test case?"
        ),

        "options": [

            "Ошибки backend",

            "Корректную работу системы",

            "Crash reports"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "Positive testing проверяет,\n"
            "что система работает как ожидается."
        ),

        "xp": 20
    },

    {
        "title": "Negative test case",

        "theory": (

            "❌ Negative test case использует\n"
            "неправильные данные.\n\n"

            "Например:\n"
            "• пустой password\n"
            "• слишком длинный username\n"
            "• неправильный email\n\n"

            "QA проверяет,\n"
            "как система реагирует на ошибки."
        ),

        "example": (
            "Пользователь оставляет password пустым."
        ),

        "question": (
            "Что проверяет negative test case?"
        ),

        "options": [

            "Только UI",

            "Ошибки системы",

            "Только performance"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "Negative testing помогает\n"
            "находить баги."
        ),

        "xp": 20
    },

    {
        "title": "Boundary values",

        "theory": (

            "📏 Boundary testing проверяет\n"
            "граничные значения.\n\n"

            "Баги часто появляются\n"
            "на границах диапазонов.\n\n"

            "Например:\n"
            "если возраст должен быть 1–100,\n"
            "QA проверит:\n"
            "0, 1, 100, 101"
        ),

        "example": (
            "Password max length = 20 symbols."
        ),

        "question": (
            "Что проверяет boundary testing?"
        ),

        "options": [

            "Граничные значения",

            "Только database",

            "Только colors"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Boundary testing ищет ошибки\n"
            "на границах значений."
        ),

        "xp": 20
    },

    {
        "title": "Test data",

        "theory": (

            "🗂 Test data —\n"
            "это данные для проверки системы.\n\n"

            "QA использует:\n"
            "• valid data\n"
            "• invalid data\n"
            "• edge cases\n\n"

            "Качество test data\n"
            "сильно влияет на тестирование."
        ),

        "example": (
            "Emails, passwords, phone numbers."
        ),

        "question": (
            "Что такое test data?"
        ),

        "options": [

            "Тестовые данные",

            "Тип браузера",

            "Название проекта"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Test data используется\n"
            "для проверки системы."
        ),

        "xp": 20
    },

    {
        "title": "Preconditions",

        "theory": (

            "⚙️ Preconditions —\n"
            "это условия перед началом теста.\n\n"

            "Например:\n"
            "• пользователь зарегистрирован\n"
            "• интернет работает\n"
            "• приложение установлено\n\n"

            "Без preconditions\n"
            "test case может быть некорректным."
        ),

        "example": (
            "User must have active account."
        ),

        "question": (
            "Что такое preconditions?"
        ),

        "options": [

            "Условия перед тестом",

            "Результат теста",

            "Тип API"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Preconditions описывают,\n"
            "что должно быть выполнено заранее."
        ),

        "xp": 20
    },

    {
        "title": "Postconditions",

        "theory": (

            "📌 Postconditions показывают,\n"
            "что должно произойти после теста.\n\n"

            "Например:\n"
            "• пользователь вошёл\n"
            "• заказ создан\n"
            "• данные сохранены\n\n"

            "Они помогают проверить итог."
        ),

        "example": (
            "Order appears in purchase history."
        ),

        "question": (
            "Что такое postconditions?"
        ),

        "options": [

            "Тип UI",

            "Условия после теста",

            "Скорость сети"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "Postconditions описывают\n"
            "состояние после выполнения теста."
        ),

        "xp": 20
    }

]