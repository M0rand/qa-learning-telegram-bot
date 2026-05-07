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