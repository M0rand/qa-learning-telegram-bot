bug_reports = [

    {
        "title": "Что такое bug report",

        "theory": (

            "🐞 Bug report —\n"
            "это описание найденной проблемы.\n\n"

            "QA создаёт bug report,\n"
            "чтобы разработчики могли:\n"
            "• понять проблему\n"
            "• воспроизвести баг\n"
            "• исправить ошибку\n\n"

            "Хороший bug report помогает\n"
            "быстрее чинить баги."
        ),

        "example": (
            "Login button does not work."
        ),

        "question": (
            "Что такое bug report?"
        ),

        "options": [

            "Тип тестирования",

            "UI элемент",

            "Описание бага"
        ],

        "correct": "3",

        "explanation": (

            "Верно 👍\n\n"

            "Bug report описывает\n"
            "найденную проблему."
        ),

        "xp": 20
    },

    {
        "title": "Summary",

        "theory": (

            "📝 Summary —\n"
            "краткое описание проблемы.\n\n"

            "Разработчик должен быстро понять,\n"
            "в чём ошибка.\n\n"

            "Хороший summary:\n"
            "• короткий\n"
            "• понятный\n"
            "• конкретный"
        ),

        "example": (
            "Login button crashes app."
        ),

        "question": (
            "Что содержит summary?"
        ),

        "options": [

            "Краткое описание бага",

            "SQL запрос",

            "Пароль пользователя"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Summary помогает быстро понять\n"
            "суть проблемы."
        ),

        "xp": 20
    },

    {
        "title": "Steps to reproduce",

        "theory": (

            "📋 Steps to reproduce —\n"
            "шаги для повторения бага.\n\n"

            "Разработчик должен суметь\n"
            "увидеть проблему самостоятельно.\n\n"

            "Шаги должны быть:\n"
            "• последовательными\n"
            "• понятными\n"
            "• точными"
        ),

        "example": (

            "1. Open app\n"
            "2. Click Login\n"
            "3. App crashes"
        ),

        "question": (
            "Для чего нужны steps to reproduce?"
        ),

        "options": [

            "Для изменения UI",

            "Для повторения бага",

            "Для настройки сервера"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "Steps помогают\n"
            "воспроизвести проблему."
        ),

        "xp": 20
    },

    {
        "title": "Expected result",

        "theory": (

            "🎯 Expected result показывает,\n"
            "как система должна работать.\n\n"

            "QA заранее описывает\n"
            "правильное поведение системы.\n\n"

            "Это помогает понять:\n"
            "есть ошибка или нет."
        ),

        "example": (
            "User logs into account successfully."
        ),

        "question": (
            "Что показывает expected result?"
        ),

        "options": [

            "Настройки браузера",

            "Фактический результат",

            "Ожидаемое поведение системы"
        ],

        "correct": "3",

        "explanation": (

            "Да 👍\n\n"

            "Expected result описывает,\n"
            "что должно было произойти."
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

            "Если они отличаются —\n"
            "значит найден баг."
        ),

        "example": (
            "Application shows error 500."
        ),

        "question": (
            "Что такое actual result?"
        ),

        "options": [

            "Реальный результат работы системы",

            "Expected result",

            "Тип regression testing"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Actual result показывает,\n"
            "что произошло реально."
        ),

        "xp": 20
    },

    {
        "title": "Severity",

        "theory": (

            "🚨 Severity показывает,\n"
            "насколько серьёзна проблема.\n\n"

            "Например:\n"
            "• typo = low severity\n"
            "• crash = high severity\n\n"

            "Severity показывает влияние бага\n"
            "на систему."
        ),

        "example": (
            "Application crashes on startup."
        ),

        "question": (
            "Что показывает severity?"
        ),

        "options": [

            "Скорость исправления",

            "Критичность бага",

            "Имя разработчика"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "Severity показывает,\n"
            "насколько серьёзна проблема."
        ),

        "xp": 20
    },

    {
        "title": "Priority",

        "theory": (

            "⏰ Priority показывает,\n"
            "как быстро нужно исправить баг.\n\n"

            "Иногда баг не очень критичный,\n"
            "но его нужно срочно исправить.\n\n"

            "Priority помогает команде\n"
            "определять порядок работы."
        ),

        "example": (
            "Ошибка оплаты перед release."
        ),

        "question": (
            "Что показывает priority?"
        ),

        "options": [

            "Тип UI bug",

            "Срочность исправления",

            "Размер database"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "Priority отвечает за то,\n"
            "насколько быстро нужно чинить баг."
        ),

        "xp": 20
    },

    {
        "title": "Attachments",

        "theory": (

            "📎 Attachments помогают\n"
            "лучше понять проблему.\n\n"

            "QA может прикреплять:\n"
            "• screenshots\n"
            "• videos\n"
            "• logs\n\n"

            "Это помогает разработчику\n"
            "быстрее разобраться в проблеме."
        ),

        "example": (
            "Видео с воспроизведением бага."
        ),

        "question": (
            "Что можно прикрепить к bug report?"
        ),

        "options": [

            "Screenshot или video",

            "Только музыку",

            "Только CSS"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Attachments помогают\n"
            "быстрее понять проблему."
        ),

        "xp": 20
    },

    {
        "title": "Duplicate bug",

        "theory": (

            "♻️ Duplicate bug —\n"
            "это баг, который уже существует.\n\n"

            "Перед созданием нового bug report\n"
            "QA обычно проверяет,\n"
            "не зарегистрирован ли баг раньше."
        ),

        "example": (
            "Bug already exists in Jira."
        ),

        "question": (
            "Что такое duplicate bug?"
        ),

        "options": [

            "Новый feature",

            "Тип smoke testing",

            "Уже существующий баг"
        ],

        "correct": "3",

        "explanation": (

            "Верно 👍\n\n"

            "Duplicate означает,\n"
            "что баг уже был найден ранее."
        ),

        "xp": 20
    },

    {
        "title": "Bug status",

        "theory": (

            "📌 Bug status показывает,\n"
            "на каком этапе находится баг.\n\n"

            "Частые статусы:\n"
            "• Open\n"
            "• In Progress\n"
            "• Fixed\n"
            "• Closed\n"
            "• Reopened\n\n"

            "Статусы помогают отслеживать работу."
        ),

        "example": (
            "Open → Fixed → Closed"
        ),

        "question": (
            "Что показывает bug status?"
        ),

        "options": [

            "Текущее состояние бага",

            "Версию Android",

            "Тип browser"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Status показывает,\n"
            "что сейчас происходит с багом."
        ),

        "xp": 20
    }

]