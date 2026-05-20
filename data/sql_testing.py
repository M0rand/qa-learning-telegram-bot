sql_testing = [

    {
        "title": "Что такое SQL",

        "theory": (

            "🗄 SQL (Structured Query Language) —\n"
            "язык для работы с базой данных.\n\n"

            "QA использует SQL,\n"
            "чтобы:\n"
            "• проверять данные\n"
            "• искать ошибки\n"
            "• сравнивать результаты\n"
            "• проверять backend logic\n\n"

            "SQL — очень полезный навык для QA."
        ),

        "example": (
            "SELECT * FROM users"
        ),

        "question": (
            "Для чего QA использует SQL?"
        ),

        "options": [

            "Для работы с database",

            "Для UI animation",

            "Для настройки browser"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "SQL помогает QA\n"
            "работать с данными."
        ),

        "xp": 20
    },

    {
        "title": "Database",

        "theory": (

            "🗂 Database хранит данные системы.\n\n"

            "Например:\n"
            "• пользователи\n"
            "• пароли\n"
            "• заказы\n"
            "• сообщения\n\n"

            "Многие QA bugs связаны\n"
            "именно с database."
        ),

        "example": (
            "User data stored in database."
        ),

        "question": (
            "Что хранит database?"
        ),

        "options": [

            "Только screenshots",

            "Данные системы",

            "Только CSS"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "Database хранит информацию продукта."
        ),

        "xp": 20
    },

    {
        "title": "Table",

        "theory": (

            "📋 Table — таблица в database.\n\n"

            "Каждая table хранит\n"
            "определённый тип данных.\n\n"

            "Например:\n"
            "• users\n"
            "• orders\n"
            "• payments\n\n"

            "Tables состоят из rows и columns."
        ),

        "example": (
            "users table"
        ),

        "question": (
            "Что такое table?"
        ),

        "options": [

            "UI component",

            "Server error",

            "Таблица в database"
        ],

        "correct": "3",

        "explanation": (

            "Верно 👍\n\n"

            "Table хранит данные в database."
        ),

        "xp": 20
    },

    {
        "title": "Row",

        "theory": (

            "📄 Row — это одна запись в таблице.\n\n"

            "Например:\n"
            "один пользователь = одна row.\n\n"

            "Каждая row содержит\n"
            "конкретные данные."
        ),

        "example": (
            "User: John, age: 25"
        ),

        "question": (
            "Что такое row?"
        ),

        "options": [

            "Одна запись в таблице",

            "Тип API request",

            "UI bug"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Row содержит одну запись данных."
        ),

        "xp": 20
    },

    {
        "title": "Column",

        "theory": (

            "📑 Column — это столбец таблицы.\n\n"

            "Columns определяют,\n"
            "какие данные хранит table.\n\n"

            "Например:\n"
            "• name\n"
            "• email\n"
            "• age"
        ),

        "example": (
            "email column"
        ),

        "question": (
            "Что такое column?"
        ),

        "options": [

            "Тип regression testing",

            "Столбец таблицы",

            "Deployment tool"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "Columns описывают структуру данных."
        ),

        "xp": 20
    },

    {
        "title": "SELECT",

        "theory": (

            "🔍 SELECT используется\n"
            "для получения данных.\n\n"

            "Это один из самых популярных\n"
            "SQL commands.\n\n"

            "QA часто использует SELECT,\n"
            "чтобы проверять database."
        ),

        "example": (
            "SELECT * FROM users"
        ),

        "question": (
            "Для чего используется SELECT?"
        ),

        "options": [

            "Для изменения UI",

            "Для удаления database",

            "Для получения данных"
        ],

        "correct": "3",

        "explanation": (

            "Да 👍\n\n"

            "SELECT получает данные из database."
        ),

        "xp": 20
    },

    {
        "title": "WHERE",

        "theory": (

            "🎯 WHERE помогает\n"
            "фильтровать данные.\n\n"

            "Без WHERE запрос может вернуть\n"
            "слишком много информации.\n\n"

            "QA часто использует WHERE,\n"
            "чтобы находить нужные записи."
        ),

        "example": (
            "SELECT * FROM users WHERE age = 25"
        ),

        "question": (
            "Для чего используется WHERE?"
        ),

        "options": [

            "Для фильтрации данных",

            "Для UI colors",

            "Для screenshots"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "WHERE помогает выбирать нужные данные."
        ),

        "xp": 20
    },

    {
        "title": "INSERT",

        "theory": (

            "➕ INSERT добавляет новые данные\n"
            "в database.\n\n"

            "Например:\n"
            "• новый пользователь\n"
            "• новый заказ\n"
            "• новое сообщение"
        ),

        "example": (
            "INSERT INTO users VALUES (...)"
        ),

        "question": (
            "Для чего используется INSERT?"
        ),

        "options": [

            "Для добавления данных",

            "Для удаления данных",

            "Для browser testing"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "INSERT создаёт новые записи."
        ),

        "xp": 20
    },

    {
        "title": "UPDATE",

        "theory": (

            "✏️ UPDATE изменяет существующие данные.\n\n"

            "Например:\n"
            "• изменение email\n"
            "• смена password\n"
            "• обновление profile"
        ),

        "example": (
            "UPDATE users SET age = 30"
        ),

        "question": (
            "Для чего используется UPDATE?"
        ),

        "options": [

            "Для screenshots",

            "Для обновления данных",

            "Для deployment"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "UPDATE помогает изменять записи."
        ),

        "xp": 20
    },

    {
        "title": "DELETE",

        "theory": (

            "🗑 DELETE удаляет данные из database.\n\n"

            "Например:\n"
            "• удалить пользователя\n"
            "• удалить заказ\n"
            "• удалить сообщение\n\n"

            "QA должен осторожно использовать DELETE."
        ),

        "example": (
            "DELETE FROM users WHERE id = 1"
        ),

        "question": (
            "Для чего используется DELETE?"
        ),

        "options": [

            "Для UI testing",

            "Для network setup",

            "Для удаления данных"
        ],

        "correct": "3",

        "explanation": (

            "Да 👍\n\n"

            "DELETE удаляет записи из database."
        ),

        "xp": 20
    }

]