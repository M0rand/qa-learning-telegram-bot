testing_types = [

    {
        "title": "Что такое testing types",

        "theory": (

            "🧪 В QA существует много видов тестирования.\n\n"

            "Каждый testing type проверяет\n"
            "разные части системы.\n\n"

            "Например:\n"
            "• functional testing проверяет функции\n"
            "• performance testing проверяет скорость\n"
            "• security testing проверяет безопасность\n\n"

            "QA использует разные типы testing\n"
            "в зависимости от задачи."
        ),

        "example": (
            "Login testing и load testing — разные виды проверок."
        ),

        "question": (
            "Зачем нужны разные testing types?"
        ),

        "options": [

            "Для проверки разных аспектов системы",

            "Для изменения UI",

            "Для установки Windows"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Разные testing types помогают\n"
            "проверять продукт с разных сторон."
        ),

        "xp": 20
    },

    {
        "title": "Functional testing",

        "theory": (

            "⚙️ Functional testing проверяет,\n"
            "правильно ли работают функции системы.\n\n"

            "QA проверяет:\n"
            "• login\n"
            "• registration\n"
            "• search\n"
            "• payment\n\n"

            "Главный вопрос:\n"
            "делает ли система то,\n"
            "что должна делать?"
        ),

        "example": (
            "Проверка оформления заказа."
        ),

        "question": (
            "Что проверяет functional testing?"
        ),

        "options": [

            "Только дизайн",

            "Работу функций системы",

            "Температуру сервера"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "Functional testing проверяет\n"
            "логику и функциональность."
        ),

        "xp": 20
    },

    {
        "title": "UI testing",

        "theory": (

            "🎨 UI testing проверяет интерфейс приложения.\n\n"

            "QA смотрит:\n"
            "• отображение кнопок\n"
            "• размеры элементов\n"
            "• цвета\n"
            "• расположение текста\n\n"

            "UI bugs влияют\n"
            "на user experience."
        ),

        "example": (
            "Текст выходит за границы кнопки."
        ),

        "question": (
            "Что проверяет UI testing?"
        ),

        "options": [

            "Интерфейс приложения",

            "SQL queries",

            "Backend logs"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "UI testing связан\n"
            "с отображением интерфейса."
        ),

        "xp": 20
    },

    {
        "title": "Regression testing",

        "theory": (

            "🔁 Regression testing проверяет,\n"
            "не сломались ли старые функции\n"
            "после изменений.\n\n"

            "Даже маленькое изменение кода\n"
            "может неожиданно сломать систему.\n\n"

            "Поэтому QA повторно проверяет\n"
            "важные сценарии."
        ),

        "example": (
            "После update QA проверяет login."
        ),

        "question": (
            "Когда выполняют regression testing?"
        ),

        "options": [

            "После изменений в системе",

            "Только перед дизайном",

            "Только при установке приложения"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Regression testing помогает\n"
            "находить новые поломки."
        ),

        "xp": 20
    },

    {
        "title": "Smoke testing",

        "theory": (

            "🔥 Smoke testing —\n"
            "быстрая проверка основных функций.\n\n"

            "QA смотрит:\n"
            "• запускается ли приложение\n"
            "• работает ли login\n"
            "• открываются ли страницы\n\n"

            "Если smoke test падает —\n"
            "система нестабильна."
        ),

        "example": (
            "Проверка login и homepage."
        ),

        "question": (
            "Для чего нужен smoke testing?"
        ),

        "options": [

            "Для быстрой проверки основных функций",

            "Для проверки шрифтов",

            "Для анализа database"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Smoke testing быстро показывает,\n"
            "можно ли тестировать дальше."
        ),

        "xp": 20
    },

    {
        "title": "Integration testing",

        "theory": (

            "🔗 Integration testing проверяет,\n"
            "как разные части системы\n"
            "работают вместе.\n\n"

            "Например:\n"
            "• frontend ↔ backend\n"
            "• API ↔ database\n"
            "• payment ↔ bank service\n\n"

            "Даже если модули работают отдельно,\n"
            "между ними могут быть ошибки."
        ),

        "example": (
            "Frontend отправляет данные backend."
        ),

        "question": (
            "Что проверяет integration testing?"
        ),

        "options": [

            "Только UI",

            "Работу модулей вместе",

            "Только colors"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "Integration testing проверяет\n"
            "взаимодействие частей системы."
        ),

        "xp": 20
    },

    {
        "title": "System testing",

        "theory": (

            "🖥 System testing проверяет\n"
            "всю систему целиком.\n\n"

            "QA тестирует:\n"
            "• frontend\n"
            "• backend\n"
            "• integrations\n"
            "• business logic\n\n"

            "Цель:\n"
            "убедиться,\n"
            "что весь продукт работает."
        ),

        "example": (
            "Полная проверка интернет-магазина."
        ),

        "question": (
            "Что проверяет system testing?"
        ),

        "options": [

            "Всю систему полностью",

            "Только API",

            "Только browser cache"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "System testing проверяет\n"
            "полную работу продукта."
        ),

        "xp": 20
    },

    {
        "title": "Performance testing",

        "theory": (

            "⚡ Performance testing проверяет,\n"
            "насколько быстро и стабильно\n"
            "работает система.\n\n"

            "QA анализирует:\n"
            "• скорость ответа\n"
            "• нагрузку\n"
            "• стабильность\n"
            "• время загрузки\n\n"

            "Это важно для больших систем."
        ),

        "example": (
            "1000 пользователей одновременно открывают сайт."
        ),

        "question": (
            "Что проверяет performance testing?"
        ),

        "options": [

            "Размер шрифта",

            "Производительность системы",

            "Цвет background"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "Performance testing помогает\n"
            "оценить скорость и стабильность."
        ),

        "xp": 20
    },

    {
        "title": "Load testing",

        "theory": (

            "📈 Load testing проверяет,\n"
            "как система работает под нагрузкой.\n\n"

            "Например:\n"
            "• тысячи пользователей online\n"
            "• большое количество запросов\n"
            "• высокий traffic\n\n"

            "QA проверяет,\n"
            "выдержит ли система нагрузку."
        ),

        "example": (
            "5000 пользователей одновременно оформляют заказ."
        ),

        "question": (
            "Что проверяет load testing?"
        ),

        "options": [

            "Работу системы под нагрузкой",

            "Только documentation",

            "Только animations"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "Load testing показывает,\n"
            "как система ведёт себя при нагрузке."
        ),

        "xp": 20
    },

    {
        "title": "Security testing",

        "theory": (

            "🔒 Security testing проверяет\n"
            "безопасность системы.\n\n"

            "QA и security engineers ищут:\n"
            "• уязвимости\n"
            "• слабую авторизацию\n"
            "• утечки данных\n"
            "• insecure requests\n\n"

            "Без security testing\n"
            "данные пользователей могут быть украдены."
        ),

        "example": (
            "Проверка SQL injection."
        ),

        "question": (
            "Что проверяет security testing?"
        ),

        "options": [

            "Безопасность системы",

            "Только UI",

            "Только скорость браузера"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Security testing помогает\n"
            "защитить систему и данные."
        ),

        "xp": 20
    }

]