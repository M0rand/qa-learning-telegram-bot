questions = [

    {
        "question":
        "Что такое баг?",

        "answer":
        (
            "Баг — это ошибка или неправильное "
            "поведение системы.\n\n"

            "Проще говоря:\n"
            "ожидаемый результат "
            "не совпадает с фактическим."
        )
    },

    {
        "question":
        "Чем QA отличается от тестирования?",

        "answer":
        (
            "Тестирование — это поиск дефектов.\n\n"

            "QA шире:\n"
            "он улучшает процессы разработки "
            "и помогает повышать качество продукта."
        )
    },

    {
        "question":
        "Что такое тест-кейс?",

        "answer":
        (
            "Тест-кейс — это инструкция "
            "для проверки функциональности.\n\n"

            "Он содержит:\n"
            "• шаги\n"
            "• тестовые данные\n"
            "• ожидаемый результат"
        )
    },

    {
        "question":
        "Что такое severity?",

        "answer":
        (
            "Severity показывает, "
            "насколько серьёзна проблема.\n\n"

            "Например:\n"
            "если payment completely broken — "
            "это высокая severity."
        )
    },

    {
        "question":
        "Что такое priority?",

        "answer":
        (
            "Priority показывает, "
            "насколько срочно нужно исправить баг.\n\n"

            "Иногда даже маленький баг "
            "может иметь высокий priority."
        )
    },

    {
        "question":
        "Что такое smoke testing?",

        "answer":
        (
            "Smoke testing — это быстрая проверка "
            "основной функциональности системы.\n\n"

            "Например:\n"
            "login, registration, payment."
        )
    },

    {
        "question":
        "Что такое regression testing?",

        "answer":
        (
            "Regression testing проверяет, "
            "не сломались ли старые функции "
            "после изменений в системе."
        )
    },

    {
        "question":
        "Что такое API?",

        "answer":
        (
            "API помогает системам "
            "обмениваться данными.\n\n"

            "Например:\n"
            "frontend отправляет request backend."
        )
    },

    {
        "question":
        "Что такое HTTP?",

        "answer":
        (
            "HTTP — протокол передачи данных "
            "между клиентом и сервером."
        )
    },

    {
        "question":
        "Что означает status code 404?",

        "answer":
        (
            "404 означает, "
            "что запрашиваемый ресурс не найден."
        )
    },

    {
        "question":
        "Что означает status code 500?",

        "answer":
        (
            "500 означает внутреннюю ошибку сервера.\n\n"

            "Обычно проблема находится "
            "на backend стороне."
        )
    },

    {
        "question":
        "Что такое SQL?",

        "answer":
        (
            "SQL — язык для работы "
            "с базами данных.\n\n"

            "QA использует SQL "
            "для проверки данных."
        )
    },

    {
        "question":
        "Что делает SELECT в SQL?",

        "answer":
        (
            "SELECT получает данные "
            "из таблицы database."
        )
    },

    {
        "question":
        "Что такое frontend?",

        "answer":
        (
            "Frontend — это часть системы, "
            "которую видит пользователь."
        )
    },

    {
        "question":
        "Что такое backend?",

        "answer":
        (
            "Backend — серверная логика системы.\n\n"

            "Он обрабатывает данные "
            "и business logic."
        )
    },

    {
        "question":
        "Что такое cookie?",

        "answer":
        (
            "Cookie хранит данные пользователя "
            "в браузере.\n\n"

            "Например:\n"
            "login session."
        )
    },

    {
        "question":
        "Что такое cache?",

        "answer":
        (
            "Cache хранит временные данные, "
            "чтобы ускорить загрузку страниц."
        )
    },

    {
        "question":
        "Что такое positive testing?",

        "answer":
        (
            "Positive testing проверяет "
            "валидные сценарии использования."
        )
    },

    {
        "question":
        "Что такое negative testing?",

        "answer":
        (
            "Negative testing проверяет, "
            "как система ведёт себя "
            "при неправильных данных."
        )
    },

    {
        "question":
        "Что такое bug report?",

        "answer":
        (
            "Bug report — это описание дефекта.\n\n"

            "Он помогает developer "
            "понять и исправить проблему."
        )
    },

    {
        "question":
        "Как бы ты протестировал login form?",

        "answer":
        (
            "Я бы проверил:\n"
            "• правильный login/password\n"
            "• неправильные данные\n"
            "• пустые поля\n"
            "• SQL injection\n"
            "• remember me\n"
            "• validation messages"
        )
    },

    {
        "question":
        "Что делать, если баг не воспроизводится?",

        "answer":
        (
            "Я бы попробовал:\n"
            "• проверить логи\n"
            "• изменить environment\n"
            "• уточнить steps\n"
            "• проверить browser/device\n"
            "• собрать больше информации"
        )
    },

    {
        "question":
        "Какой баг самый критичный?",

        "answer":
        (
            "Самые критичные баги:\n"
            "• loss of money\n"
            "• data leak\n"
            "• system crash\n"
            "• payment failure\n"
            "• security issues"
        )
    },

    {
        "question":
        "Что бы ты проверил перед release?",

        "answer":
        (
            "Перед release я бы проверил:\n"
            "• smoke testing\n"
            "• regression testing\n"
            "• critical user flows\n"
            "• payment\n"
            "• login\n"
            "• API errors"
        )
    },

    {
        "question":
        "Как протестировать search?",

        "answer":
        (
            "Я бы проверил:\n"
            "• корректный поиск\n"
            "• пустой запрос\n"
            "• special characters\n"
            "• long text\n"
            "• скорость поиска\n"
            "• no results behavior"
        )
    }

]