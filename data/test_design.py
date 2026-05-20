test_design = [

    {
        "title": "Что такое test design",

        "theory": (

            "🧠 Test design —\n"
            "это процесс создания эффективных тестов.\n\n"

            "QA анализирует систему\n"
            "и думает:\n"
            "• что важно проверить\n"
            "• где могут быть баги\n"
            "• какие сценарии самые рискованные\n\n"

            "Хороший test design помогает\n"
            "находить больше ошибок."
        ),

        "example": (
            "QA создаёт проверки для login form."
        ),

        "question": (
            "Что такое test design?"
        ),

        "options": [

            "Настройка сервера",

            "Тип database",

            "Создание эффективных тестов"
        ],

        "correct": "3",

        "explanation": (

            "Верно 👍\n\n"

            "Test design помогает QA\n"
            "создавать качественные проверки."
        ),

        "xp": 20
    },

    {
        "title": "Equivalence partitioning",

        "theory": (

            "📦 Equivalence partitioning делит\n"
            "данные на группы.\n\n"

            "QA не проверяет все значения подряд,\n"
            "а выбирает представителей групп.\n\n"

            "Например:\n"
            "Возраст:\n"
            "• 1–17\n"
            "• 18–60\n"
            "• 61+\n\n"

            "Это экономит время тестирования."
        ),

        "example": (
            "Тестирование возрастных категорий."
        ),

        "question": (
            "Что делает equivalence partitioning?"
        ),

        "options": [

            "Делит данные на группы",

            "Удаляет баги",

            "Настраивает browser"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "QA тестирует представителей\n"
            "каждой группы данных."
        ),

        "xp": 20
    },

    {
        "title": "Boundary value analysis",

        "theory": (

            "📏 Boundary value analysis проверяет\n"
            "граничные значения.\n\n"

            "Очень много багов появляется\n"
            "на границах диапазонов.\n\n"

            "Например:\n"
            "если лимит 1–100,\n"
            "QA проверит:\n"
            "0, 1, 100, 101"
        ),

        "example": (
            "Password max length = 20."
        ),

        "question": (
            "Что проверяет boundary value analysis?"
        ),

        "options": [

            "UI colors",

            "Граничные значения",

            "Размер database"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "Boundary testing помогает\n"
            "находить ошибки на границах."
        ),

        "xp": 20
    },

    {
        "title": "Decision table",

        "theory": (

            "📋 Decision table помогает\n"
            "проверять комбинации условий.\n\n"

            "Это полезно,\n"
            "когда логика сложная.\n\n"

            "Например:\n"
            "• карта валидна?\n"
            "• достаточно денег?\n"
            "• пользователь авторизован?\n\n"

            "QA проверяет разные комбинации."
        ),

        "example": (
            "Payment processing conditions."
        ),

        "question": (
            "Для чего используется decision table?"
        ),

        "options": [

            "Для комбинаций условий",

            "Для UI animation",

            "Для deployment"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Decision tables помогают\n"
            "тестировать сложную бизнес-логику."
        ),

        "xp": 20
    },

    {
        "title": "State transition testing",

        "theory": (

            "🔄 State transition testing проверяет,\n"
            "как система меняет состояния.\n\n"

            "Например:\n"
            "• Logged out → Logged in\n"
            "• Draft → Published\n"
            "• Active → Blocked\n\n"

            "QA проверяет корректность переходов."
        ),

        "example": (
            "Пользователь входит в аккаунт."
        ),

        "question": (
            "Что проверяет state transition testing?"
        ),

        "options": [

            "Только database",

            "Состояния системы",

            "Размер шрифта"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "Этот подход проверяет\n"
            "переходы между состояниями."
        ),

        "xp": 20
    },

    {
        "title": "Error guessing",

        "theory": (

            "🎯 Error guessing использует\n"
            "опыт и интуицию QA.\n\n"

            "Опытный QA может предположить,\n"
            "где вероятнее всего появится баг.\n\n"

            "Например:\n"
            "• пустые поля\n"
            "• очень длинный текст\n"
            "• нестабильный internet"
        ),

        "example": (
            "QA проверяет пустой password."
        ),

        "question": (
            "На чём основан error guessing?"
        ),

        "options": [

            "На опыте QA",

            "На backend deployment",

            "На UI colors"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Error guessing использует\n"
            "опыт тестировщика."
        ),

        "xp": 20
    },

    {
        "title": "Positive testing",

        "theory": (

            "✅ Positive testing использует\n"
            "правильные данные.\n\n"

            "QA проверяет,\n"
            "что система работает нормально.\n\n"

            "Например:\n"
            "• корректный login\n"
            "• валидный email\n"
            "• правильный payment"
        ),

        "example": (
            "Пользователь вводит правильный password."
        ),

        "question": (
            "Какие данные использует positive testing?"
        ),

        "options": [

            "Повреждённые",

            "Корректные",

            "Случайные"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "Positive testing проверяет\n"
            "нормальную работу системы."
        ),

        "xp": 20
    },

    {
        "title": "Negative testing",

        "theory": (

            "❌ Negative testing использует\n"
            "неправильные данные.\n\n"

            "QA проверяет,\n"
            "как система реагирует на ошибки.\n\n"

            "Например:\n"
            "• пустой password\n"
            "• неправильный email\n"
            "• слишком длинный input"
        ),

        "example": (
            "User leaves login field empty."
        ),

        "question": (
            "Что проверяет negative testing?"
        ),

        "options": [

            "Ошибочные сценарии",

            "Только successful login",

            "Только UI themes"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Negative testing помогает\n"
            "находить слабые места системы."
        ),

        "xp": 20
    },

    {
        "title": "Risk-based testing",

        "theory": (

            "⚠️ Risk-based testing фокусируется\n"
            "на самых рискованных частях системы.\n\n"

            "QA сначала проверяет:\n"
            "• payment\n"
            "• authentication\n"
            "• critical business flows\n\n"

            "Это помогает быстрее находить\n"
            "опасные баги."
        ),

        "example": (
            "Payment testing before release."
        ),

        "question": (
            "На чём фокусируется risk-based testing?"
        ),

        "options": [

            "На критичных рисках",

            "На цвете интерфейса",

            "На настройке Linux"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "QA уделяет больше внимания\n"
            "опасным зонам системы."
        ),

        "xp": 20
    },

    {
        "title": "Exploratory testing",

        "theory": (

            "🔍 Exploratory testing —\n"
            "исследовательское тестирование.\n\n"

            "QA изучает систему свободно,\n"
            "без строгих test cases.\n\n"

            "Во время exploratory testing\n"
            "часто находятся неожиданные баги."
        ),

        "example": (
            "QA исследует новую feature."
        ),

        "question": (
            "Что такое exploratory testing?"
        ),

        "options": [

            "Исследовательское тестирование",

            "Только automation",

            "Тип deployment"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Exploratory testing помогает\n"
            "искать нестандартные проблемы."
        ),

        "xp": 20
    }

]