import os

from google import genai

from dotenv import load_dotenv


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


async def evaluate_answer(
    question,
    user_answer
):

    try:

        prompt = f"""

Ты QA interviewer.

Вопрос:
{question}

Ответ пользователя:
{user_answer}

Кратко оцени ответ.

Если ответ хороший:
- похвали

Если ответ слабый:
- объясни что улучшить

Отвечай кратко.
На русском языке.

"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",

            contents=prompt
        )

        print(response.text)

        return response.text

    except Exception as e:

        print("GEMINI ERROR:", e)

        return (
            "⚠️ AI временно недоступен"
        )