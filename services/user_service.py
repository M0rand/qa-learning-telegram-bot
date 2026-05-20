import sqlite3

from database.db import conn, cursor


def create_user(user_id, username):

    cursor.execute(

        """

        INSERT OR IGNORE INTO users (
            telegram_id,
            username
        )

        VALUES (?, ?)

        """,

        (
            user_id,
            username
        )
    )

    conn.commit()


def add_xp_db(user_id, xp):

    cursor.execute(

        "UPDATE users SET xp = xp + ? WHERE telegram_id = ?",

        (xp, user_id)
    )

    conn.commit()


def get_xp_db(user_id):

    cursor.execute(

        "SELECT xp FROM users WHERE telegram_id = ?",

        (user_id,)
    )

    result = cursor.fetchone()

    return result[0]


def set_lesson(user_id, lesson):

    cursor.execute(

        "UPDATE users SET current_lesson = ? WHERE telegram_id = ?",

        (lesson, user_id)
    )

    conn.commit()


def get_lesson(user_id):

    cursor.execute(

        "SELECT current_lesson FROM users WHERE telegram_id = ?",

        (user_id,)
    )

    result = cursor.fetchone()

    return result[0]

def complete_lesson(

    user_id,

    block_id,

    lesson_index
):

    conn = sqlite3.connect(
        "qa_bot.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        INSERT OR IGNORE INTO
        completed_lessons

        (
            user_id,
            block_id,
            lesson_index
        )

        VALUES (?, ?, ?)
        """,

        (
            user_id,
            block_id,
            lesson_index
        )
    )

    conn.commit()

    conn.close()


def is_lesson_completed(

    user_id,

    block_id,

    lesson_index
):

    conn = sqlite3.connect(
        "qa_bot.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT *
        FROM completed_lessons

        WHERE user_id = ?
        AND block_id = ?
        AND lesson_index = ?
        """,

        (
            user_id,
            block_id,
            lesson_index
        )
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def get_completed_lessons_count(

    user_id,

    block_id
):

    conn = sqlite3.connect(
        "qa_bot.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT COUNT(*)

        FROM completed_lessons

        WHERE user_id = ?
        AND block_id = ?
        """,

        (
            user_id,
            block_id
        )
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count