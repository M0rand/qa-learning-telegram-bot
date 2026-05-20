blocks = {

    "basics": {

        "title": "📗 Основы тестирования",

        "description": (
            "Что такое баг, "
            "тестирование и QA"
        ),

        "lessons": [

            {
                "title": "Что такое баг",

                "theory": (
                    "Баг — это отклонение "
                    "фактического результата "
                    "от ожидаемого."
                ),

                "example": (
                    "🍕 Ты заказал пиццу,\n"
                    "а привезли суши 🍣"
                ),

                "question": (
                    "Это баг?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Результат не совпал "
                    "с ожиданием пользователя."
                ),

                "xp": 20
            },

            {
                "title": "Severity",

                "theory": (
                    "Severity показывает "
                    "насколько баг "
                    "критичен для системы."
                ),

                "example": (
                    "💥 Приложение падает "
                    "при открытии."
                ),

                "question": (
                    "Это высокая severity?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Падение приложения "
                    "— критичный баг."
                ),

                "xp": 20
            },
            
            {
                "title": "Expected vs Actual",

                "theory": (
                    "Тестировщик сравнивает "
                    "ожидаемый результат "
                    "с фактическим."
                ),

                "example": (
                    "Ожидали: кнопка работает ✅\n"
                    "Фактически: кнопка не нажимается ❌"
                ),

                "question": (
                    "Если actual result "
                    "не совпадает с expected "
                    "— это баг?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Главная задача QA — "
                    "находить различия "
                    "между expected и actual."
                ),

                "xp": 20
            },

            {
                "title": "Что такое тестирование",

                "theory": (
                    "Тестирование — это "
                    "проверка продукта "
                    "на наличие дефектов."
                ),

                "example": (
                    "QA проверяет:\n"
                    "работает ли login,\n"
                    "оплата,\n"
                    "поиск."
                ),

                "question": (
                    "Цель тестирования "
                    "— найти баги?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Тестирование помогает "
                    "найти проблемы "
                    "до пользователей."
                ),

                "xp": 20
            },

            {
                "title": "Почему невозможно протестировать всё",

                "theory": (
                    "У продукта слишком "
                    "много сценариев "
                    "для полной проверки."
                ),

                "example": (
                    "Ты не сможешь проверить\n"
                    "все устройства,\n"
                    "браузеры и действия."
                ),

                "question": (
                    "Можно ли сделать "
                    "100% testing?"
                ),

                "correct": "нет",

                "explanation": (
                    "Верно 👍\n\n"
                    "Полное тестирование "
                    "почти невозможно."
                ),

                "xp": 20
            },
            
            {
                "title": "Functional bug",

                "theory": (
                    "Functional bug — это "
                    "ошибка в работе "
                    "функции системы."
                ),

                "example": (
                    "Кнопка Login "
                    "не выполняет вход."
                ),

                "question": (
                    "Если функция не работает "
                    "— это functional bug?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Functional bug связан "
                    "с неправильной "
                    "работой функционала."
                ),

                "xp": 20
            },

            {
                "title": "UI bug",

                "theory": (
                    "UI bug связан "
                    "с внешним видом "
                    "интерфейса."
                ),

                "example": (
                    "Текст выходит "
                    "за границы кнопки."
                ),

                "question": (
                    "Это UI bug?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "UI bug влияет "
                    "на отображение "
                    "интерфейса."
                ),

                "xp": 20
            },

            {
                "title": "Logic bug",

                "theory": (
                    "Logic bug — это "
                    "ошибка в логике "
                    "работы приложения."
                ),

                "example": (
                    "Скидка должна "
                    "применяться от 100$,\n"
                    "но применяется от 10$."
                ),

                "question": (
                    "Это logic bug?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Приложение работает "
                    "не по бизнес-логике."
                ),

                "xp": 20
            },

            {
                "title": "QA vs Tester",

                "theory": (
                    "Tester ищет баги,\n"
                    "а QA улучшает "
                    "качество процессов."
                ),

                "example": (
                    "QA предлагает "
                    "улучшить процесс "
                    "разработки."
                ),

                "question": (
                    "QA занимается "
                    "только поиском багов?"
                ),

                "correct": "нет",

                "explanation": (
                    "Верно 👍\n\n"
                    "QA отвечает "
                    "за качество "
                    "всего процесса."
                ),

                "xp": 20
            },

            {
                "title": "Post-release bugs",

                "theory": (
                    "Иногда баги попадают "
                    "в production "
                    "после релиза."
                ),

                "example": (
                    "После обновления "
                    "сломалась оплата."
                ),

                "question": (
                    "Могут ли баги "
                    "попасть в production?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Даже хорошие команды "
                    "не могут избежать "
                    "всех багов."
                ),

                "xp": 20
            },
            
            {
                "title": "Severity",

                "theory": (
                    "Severity показывает "
                    "насколько баг "
                    "критичен для системы."
                ),

                "example": (
                    "💥 Приложение падает "
                    "при запуске."
                ),

                "question": (
                    "Падение приложения "
                    "— высокая severity?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Если система не работает "
                    "— severity высокая."
                ),

                "xp": 20
            },

            {
                "title": "Priority",

                "theory": (
                    "Priority показывает "
                    "насколько быстро "
                    "нужно исправить баг."
                ),

                "example": (
                    "Ошибка в логотипе "
                    "на главной странице "
                    "перед релизом."
                ),

                "question": (
                    "Может ли баг иметь "
                    "высокий priority "
                    "и низкий severity?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Некоторые некритичные баги "
                    "важно исправить срочно."
                ),

                "xp": 20
            },

            {
                "title": "Regression testing",

                "theory": (
                    "Regression testing "
                    "проверяет, "
                    "не сломалось ли "
                    "старое поведение."
                ),

                "example": (
                    "После обновления "
                    "QA проверяет login,\n"
                    "оплату и поиск."
                ),

                "question": (
                    "Regression testing "
                    "проверяет старый функционал?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Regression помогает "
                    "убедиться, что "
                    "новые изменения "
                    "не сломали старое."
                ),

                "xp": 20
            },

            {
                "title": "Smoke testing",

                "theory": (
                    "Smoke testing — "
                    "это быстрая проверка "
                    "основного функционала."
                ),

                "example": (
                    "QA проверяет:\n"
                    "login,\n"
                    "регистрацию,\n"
                    "главную страницу."
                ),

                "question": (
                    "Smoke testing "
                    "проверяет основные функции?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Smoke testing помогает "
                    "быстро понять, "
                    "можно ли тестировать дальше."
                ),

                "xp": 20
            },

            {
                "title": "Стоимость багов",

                "theory": (
                    "Чем позже найден баг, "
                    "тем дороже "
                    "его исправление."
                ),

                "example": (
                    "Баг в production "
                    "может привести "
                    "к потере денег."
                ),

                "question": (
                    "Баги в production "
                    "обычно дороже?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Исправление багов "
                    "после релиза "
                    "может стоить очень дорого."
                ),

                "xp": 20
            }
        ]
    },

    "test_cases": {

        "title": "📘 Test Cases",

        "description": (
            "Учимся писать "
            "тест-кейсы"
        ),

        "lessons": [

            {
                "title": "Что такое test case",

                "theory": (
                    "Test case — это "
                    "сценарий проверки "
                    "функциональности."
                ),

                "example": (
                    "Проверка login формы:\n"
                    "1. Ввести логин\n"
                    "2. Ввести пароль\n"
                    "3. Нажать Login"
                ),

                "question": (
                    "Test case помогает "
                    "проверять систему?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Test case описывает "
                    "как проверять функционал."
                ),

                "xp": 20
            },

            {
                "title": "Structure of test case",

                "theory": (
                    "У test case есть "
                    "структура:\n"
                    "steps,\n"
                    "expected result,\n"
                    "test data."
                ),

                "example": (
                    "Step:\n"
                    "Нажать Login\n\n"
                    "Expected:\n"
                    "Пользователь вошёл."
                ),

                "question": (
                    "Expected result — "
                    "часть test case?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Expected result показывает "
                    "что должно произойти."
                ),

                "xp": 20
            },

            {
                "title": "Preconditions",

                "theory": (
                    "Preconditions — это "
                    "условия перед тестом."
                ),

                "example": (
                    "Пользователь должен "
                    "быть зарегистрирован."
                ),

                "question": (
                    "Preconditions нужны "
                    "до начала теста?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Preconditions описывают "
                    "подготовку к тесту."
                ),

                "xp": 20
            },

            {
                "title": "Test steps",

                "theory": (
                    "Steps — это "
                    "последовательность действий."
                ),

                "example": (
                    "1. Открыть сайт\n"
                    "2. Нажать Login\n"
                    "3. Ввести пароль"
                ),

                "question": (
                    "Steps показывают "
                    "что делать QA?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Steps помогают "
                    "выполнять тест."
                ),

                "xp": 20
            },

            {
                "title": "Expected result",

                "theory": (
                    "Expected result — "
                    "ожидаемый результат теста."
                ),

                "example": (
                    "После login "
                    "открывается профиль."
                ),

                "question": (
                    "Expected result "
                    "описывает ожидание?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "QA сравнивает "
                    "actual result "
                    "с expected."
                ),

                "xp": 20
            },

            {
                "title": "Test data",

                "theory": (
                    "Test data — это "
                    "данные для проверки."
                ),

                "example": (
                    "Email:\n"
                    "test@gmail.com"
                ),

                "question": (
                    "Логин и пароль "
                    "могут быть test data?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Test data используется "
                    "для выполнения теста."
                ),

                "xp": 20
            },

            {
                "title": "Positive testing",

                "theory": (
                    "Positive testing "
                    "проверяет корректные данные."
                ),

                "example": (
                    "Ввести правильный пароль."
                ),

                "question": (
                    "Positive testing "
                    "использует валидные данные?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Positive testing "
                    "проверяет нормальное поведение."
                ),

                "xp": 20
            },

            {
                "title": "Negative testing",

                "theory": (
                    "Negative testing "
                    "проверяет невалидные данные."
                ),

                "example": (
                    "Ввести пустой пароль."
                ),

                "question": (
                    "Negative testing "
                    "проверяет ошибки?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Negative testing "
                    "ищет проблемы в системе."
                ),

                "xp": 20
            },

            {
                "title": "Good vs bad test case",

                "theory": (
                    "Хороший test case "
                    "понятный и подробный."
                ),

                "example": (
                    "❌ Нажать кнопку\n\n"
                    "✅ Нажать кнопку Login"
                ),

                "question": (
                    "Хороший test case "
                    "должен быть понятным?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "QA и команда должны "
                    "понимать test case."
                ),

                "xp": 20
            },

            {
                "title": "Test suites",

                "theory": (
                    "Test suite — это "
                    "группа test cases."
                ),

                "example": (
                    "Login suite:\n"
                    "login,\n"
                    "logout,\n"
                    "forgot password"
                ),

                "question": (
                    "Test suite содержит "
                    "несколько test cases?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Test suites помогают "
                    "организовывать тесты."
                ),

                "xp": 20
            },

            {
                "title": "Checklist vs test case",

                "theory": (
                    "Checklist проще,\n"
                    "а test case подробнее."
                ),

                "example": (
                    "Checklist:\n"
                    "✔ Login\n\n"
                    "Test case:\n"
                    "подробные steps"
                ),

                "question": (
                    "Test case подробнее checklist?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Test cases содержат "
                    "детальные шаги."
                ),

                "xp": 20
            },

            {
                "title": "Reusable test cases",

                "theory": (
                    "Некоторые test cases "
                    "можно использовать повторно."
                ),

                "example": (
                    "Login test case "
                    "используется в regression."
                ),

                "question": (
                    "Test cases можно "
                    "переиспользовать?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Это экономит время QA."
                ),

                "xp": 20
            },

            {
                "title": "Edge cases",

                "theory": (
                    "Edge cases проверяют "
                    "граничные ситуации."
                ),

                "example": (
                    "Пароль длиной 255 символов."
                ),

                "question": (
                    "Edge cases проверяют "
                    "нестандартные значения?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Edge cases помогают "
                    "находить скрытые баги."
                ),

                "xp": 20
            },

            {
                "title": "Missing expected result",

                "theory": (
                    "Без expected result "
                    "трудно понять "
                    "что проверять."
                ),

                "example": (
                    "Есть steps,\n"
                    "но нет expected result."
                ),

                "question": (
                    "Expected result важен "
                    "для test case?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Без expected result "
                    "невозможно сравнить результат."
                ),

                "xp": 20
            },

            {
                "title": "First real test case",

                "theory": (
                    "QA должен уметь "
                    "создавать test cases "
                    "для реальных функций."
                ),

                "example": (
                    "Login form test case."
                ),

                "question": (
                    "Test cases используются "
                    "в реальной QA работе?"
                ),

                "correct": "да",

                "explanation": (
                    "Да 👍\n\n"
                    "Это один из основных "
                    "инструментов QA."
                ),

                "xp": 20
            }
        ]
    }
}