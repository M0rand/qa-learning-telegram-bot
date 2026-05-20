automation_basics = [

    {
        "title": "Что такое test automation",

        "theory": (

            "🤖 Test automation —\n"
            "это автоматическая проверка системы\n"
            "с помощью кода.\n\n"

            "Вместо ручных действий\n"
            "тесты выполняет программа.\n\n"

            "Automation помогает:\n"
            "• быстрее тестировать\n"
            "• экономить время\n"
            "• запускать regression tests"
        ),

        "example": (
            "Script automatically checks login."
        ),

        "question": (
            "Что такое test automation?"
        ),

        "options": [

            "Автоматическое тестирование",

            "Тип database",

            "UI redesign"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Automation использует код\n"
            "для проверки системы."
        ),

        "xp": 20
    },

    {
        "title": "Почему automation важен",

        "theory": (

            "⚡ Automation помогает QA\n"
            "тестировать быстрее.\n\n"

            "Automation особенно полезен для:\n"
            "• regression testing\n"
            "• repetitive tasks\n"
            "• large projects\n\n"

            "Manual testing и automation\n"
            "часто работают вместе."
        ),

        "example": (
            "Regression suite runs automatically."
        ),

        "question": (
            "Почему automation полезен?"
        ),

        "options": [

            "Потому что ускоряет testing",

            "Потому что меняет UI colors",

            "Потому что удаляет database"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Automation помогает экономить время."
        ),

        "xp": 20
    },

    {
        "title": "Manual vs Automation",

        "theory": (

            "🧑‍💻 Manual testing выполняется вручную.\n\n"

            "🤖 Automation testing выполняется script.\n\n"

            "Manual testing хорошо подходит\n"
            "для exploratory testing,\n"
            "а automation — для repetitive checks."
        ),

        "example": (
            "QA manually explores new feature."
        ),

        "question": (
            "Что выполняет automation testing?"
        ),

        "options": [

            "Человек вручную",

            "Script или program",

            "Только designer"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "Automation использует scripts."
        ),

        "xp": 20
    },

    {
        "title": "Test script",

        "theory": (

            "📜 Test script —\n"
            "это код для автоматического теста.\n\n"

            "Script выполняет действия:\n"
            "• открывает сайт\n"
            "• нажимает buttons\n"
            "• вводит данные\n"
            "• проверяет результат"
        ),

        "example": (
            "Automation script tests login."
        ),

        "question": (
            "Что такое test script?"
        ),

        "options": [

            "Код автоматического теста",

            "Тип mobile device",

            "Database backup"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Scripts помогают автоматизировать проверки."
        ),

        "xp": 20
    },

    {
        "title": "Selenium",

        "theory": (

            "🌐 Selenium —\n"
            "один из самых популярных\n"
            "automation tools.\n\n"

            "Он помогает:\n"
            "• управлять browser\n"
            "• кликать buttons\n"
            "• вводить text\n"
            "• проверять web pages"
        ),

        "example": (
            "Selenium opens Chrome browser."
        ),

        "question": (
            "Для чего используется Selenium?"
        ),

        "options": [

            "Для web automation",

            "Для video editing",

            "Для SQL joins"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Selenium автоматизирует web testing."
        ),

        "xp": 20
    },

    {
        "title": "Playwright",

        "theory": (

            "🎭 Playwright — современный\n"
            "automation framework.\n\n"

            "Он поддерживает:\n"
            "• Chromium\n"
            "• Firefox\n"
            "• WebKit\n\n"

            "Многие QA используют Playwright\n"
            "для modern web testing."
        ),

        "example": (
            "Playwright tests website automatically."
        ),

        "question": (
            "Что такое Playwright?"
        ),

        "options": [

            "Automation framework",

            "Database engine",

            "Photo editor"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Playwright помогает автоматизировать testing."
        ),

        "xp": 20
    },

    {
        "title": "Locator",

        "theory": (

            "🎯 Locator помогает automation script\n"
            "находить элементы на странице.\n\n"

            "Например:\n"
            "• button\n"
            "• input field\n"
            "• checkbox\n\n"

            "Без locator automation\n"
            "не сможет взаимодействовать с UI."
        ),

        "example": (
            "Script finds Login button."
        ),

        "question": (
            "Для чего нужен locator?"
        ),

        "options": [

            "Для поиска элементов",

            "Для Linux installation",

            "Для screenshots"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Locator помогает script находить UI elements."
        ),

        "xp": 20
    },

    {
        "title": "Assertion",

        "theory": (

            "✅ Assertion проверяет,\n"
            "что результат соответствует ожиданию.\n\n"

            "Например:\n"
            "• button visible\n"
            "• text exists\n"
            "• login successful\n\n"

            "Assertions — основа automation testing."
        ),

        "example": (
            "Assert login success message."
        ),

        "question": (
            "Что делает assertion?"
        ),

        "options": [

            "Изменяет database",

            "Проверяет результат",

            "Создаёт screenshots"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "Assertion сравнивает actual и expected result."
        ),

        "xp": 20
    },

    {
        "title": "Test run",

        "theory": (

            "▶️ Test run —\n"
            "это запуск automation tests.\n\n"

            "Во время test run:\n"
            "• scripts выполняются\n"
            "• assertions проверяются\n"
            "• results сохраняются"
        ),

        "example": (
            "CI system launches automation suite."
        ),

        "question": (
            "Что такое test run?"
        ),

        "options": [

            "Запуск automated tests",

            "Тип browser",

            "Network protocol"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Test run выполняет automation scripts."
        ),

        "xp": 20
    },

    {
        "title": "CI/CD basics",

        "theory": (

            "🚀 CI/CD помогает автоматически:\n"
            "• запускать tests\n"
            "• проверять code\n"
            "• делать deployments\n\n"

            "Automation tests часто работают\n"
            "внутри CI/CD pipeline."
        ),

        "example": (
            "GitHub Actions runs automation tests."
        ),

        "question": (
            "Для чего используется CI/CD?"
        ),

        "options": [

            "Для автоматизации процессов",

            "Для UI colors",

            "Для mobile gestures"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "CI/CD помогает автоматизировать development workflow."
        ),

        "xp": 20
    }

]