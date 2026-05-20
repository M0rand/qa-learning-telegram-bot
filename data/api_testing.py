api_testing = [

    {
        "title": "Что такое API",

        "theory": (

            "🌐 API помогает разным системам\n"
            "обмениваться данными.\n\n"

            "Например:\n"
            "📱 мобильное приложение отправляет запрос серверу:\n"
            "\"Покажи мои сообщения\"\n\n"

            "Сервер отвечает:\n"
            "\"Вот сообщения\"\n\n"

            "Так frontend общается с backend.\n\n"

            "QA тестирует API,\n"
            "чтобы проверять backend логику."
        ),

        "example": (
            "Telegram загружает сообщения через API."
        ),

        "question": (
            "Для чего используется API?"
        ),

        "options": [

            "Для UI animation",

            "Для настройки browser",

            "Для обмена данными"
        ],

        "correct": "3",

        "explanation": (

            "Верно 👍\n\n"

            "API помогает системам\n"
            "общаться друг с другом."
        ),

        "xp": 20
    },

    {
        "title": "Request",

        "theory": (

            "📤 Request —\n"
            "это запрос клиента к серверу.\n\n"

            "Приложение отправляет request,\n"
            "когда хочет:\n"
            "• получить данные\n"
            "• создать данные\n"
            "• изменить данные\n"
            "• удалить данные"
        ),

        "example": (
            "GET /users"
        ),

        "question": (
            "Что такое request?"
        ),

        "options": [

            "Запрос к серверу",

            "Ответ сервера",

            "Ошибка UI"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "Client отправляет request серверу."
        ),

        "xp": 20
    },

    {
        "title": "Response",

        "theory": (

            "📥 Response —\n"
            "ответ сервера на request.\n\n"

            "Response обычно содержит:\n"
            "• status code\n"
            "• data\n"
            "• error messages\n\n"

            "QA проверяет response,\n"
            "чтобы убедиться,\n"
            "что API работает правильно."
        ),

        "example": (
            "200 OK + user data"
        ),

        "question": (
            "Что такое response?"
        ),

        "options": [

            "Тип browser",

            "Ответ сервера",

            "Настройка frontend"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "Server возвращает response клиенту."
        ),

        "xp": 20
    },

    {
        "title": "GET request",

        "theory": (

            "📥 GET request используется,\n"
            "когда приложение хочет получить данные.\n\n"

            "Например:\n"
            "• список товаров\n"
            "• профиль пользователя\n"
            "• сообщения\n\n"

            "GET ничего не изменяет.\n"
            "Он только получает информацию."
        ),

        "example": (
            "GET /products"
        ),

        "question": (
            "Для чего используется GET?"
        ),

        "options": [

            "Для удаления данных",

            "Для получения данных",

            "Для UI testing"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "GET request получает данные с сервера."
        ),

        "xp": 20
    },

    {
        "title": "POST request",

        "theory": (

            "📨 POST request используется\n"
            "для создания новых данных.\n\n"

            "Например:\n"
            "• регистрация пользователя\n"
            "• создание заказа\n"
            "• отправка сообщения\n\n"

            "POST обычно изменяет систему."
        ),

        "example": (
            "POST /users"
        ),

        "question": (
            "Для чего используется POST?"
        ),

        "options": [

            "Для создания данных",

            "Для browser cache",

            "Для screenshots"
        ],

        "correct": "1",

        "explanation": (

            "Верно 👍\n\n"

            "POST создаёт новые ресурсы."
        ),

        "xp": 20
    },

    {
        "title": "PUT request",

        "theory": (

            "✏️ PUT request используется\n"
            "для обновления данных.\n\n"

            "Например:\n"
            "• изменение profile\n"
            "• обновление password\n"
            "• изменение email\n\n"

            "PUT изменяет уже существующий ресурс."
        ),

        "example": (
            "PUT /profile"
        ),

        "question": (
            "Для чего используется PUT?"
        ),

        "options": [

            "Для получения данных",

            "Для обновления данных",

            "Для UI colors"
        ],

        "correct": "2",

        "explanation": (

            "Да 👍\n\n"

            "PUT помогает изменять данные."
        ),

        "xp": 20
    },

    {
        "title": "DELETE request",

        "theory": (

            "🗑 DELETE request удаляет данные.\n\n"

            "Например:\n"
            "• удалить аккаунт\n"
            "• удалить комментарий\n"
            "• удалить товар\n\n"

            "DELETE изменяет состояние системы."
        ),

        "example": (
            "DELETE /users/1"
        ),

        "question": (
            "Для чего используется DELETE?"
        ),

        "options": [

            "Для screenshots",

            "Для UI testing",

            "Для удаления данных"
        ],

        "correct": "3",

        "explanation": (

            "Верно 👍\n\n"

            "DELETE request удаляет ресурсы."
        ),

        "xp": 20
    },

    {
        "title": "Status code 200",

        "theory": (

            "✅ Status code 200 означает,\n"
            "что request успешно выполнен.\n\n"

            "Это один из самых популярных\n"
            "HTTP status codes.\n\n"

            "QA часто проверяет,\n"
            "что API возвращает 200 OK."
        ),

        "example": (
            "GET /users → 200 OK"
        ),

        "question": (
            "Что означает 200 OK?"
        ),

        "options": [

            "Успешный запрос",

            "Server crash",

            "Unauthorized access"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "200 означает успешный response."
        ),

        "xp": 20
    },

    {
        "title": "Status code 404",

        "theory": (

            "❌ Status code 404 означает,\n"
            "что ресурс не найден.\n\n"

            "Например:\n"
            "• неправильный URL\n"
            "• удалённая страница\n"
            "• отсутствующий endpoint"
        ),

        "example": (
            "GET /unknown-page"
        ),

        "question": (
            "Что означает 404?"
        ),

        "options": [

            "Успешный response",

            "Ресурс не найден",

            "Database connected"
        ],

        "correct": "2",

        "explanation": (

            "Верно 👍\n\n"

            "404 означает,\n"
            "что resource отсутствует."
        ),

        "xp": 20
    },

    {
        "title": "Status code 500",

        "theory": (

            "💥 Status code 500 означает,\n"
            "что на сервере произошла ошибка.\n\n"

            "Обычно это backend problem.\n\n"

            "QA проверяет:\n"
            "• когда появляется 500\n"
            "• какие действия вызывают ошибку\n"
            "• как система обрабатывает failure"
        ),

        "example": (
            "Server crashes during request."
        ),

        "question": (
            "Что означает status code 500?"
        ),

        "options": [

            "Ошибка сервера",

            "Правильный login",

            "Successful deployment"
        ],

        "correct": "1",

        "explanation": (

            "Да 👍\n\n"

            "500 говорит\n"
            "о server-side проблеме."
        ),

        "xp": 20
    }

]