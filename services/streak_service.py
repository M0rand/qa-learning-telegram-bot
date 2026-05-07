from datetime import datetime, timedelta

from database.db import conn, cursor


def update_streak(user_id):

    today = datetime.now().date()

    cursor.execute(

        "SELECT last_login, streak FROM users WHERE telegram_id = ?",

        (user_id,)
    )

    result = cursor.fetchone()

    last_login = result[0]
    streak = result[1]

    if last_login:

        last_date = datetime.strptime(
            last_login,
            "%Y-%m-%d"
        ).date()

        if last_date == today:

            return streak

        elif last_date == today - timedelta(days=1):

            streak += 1

        else:

            streak = 1

    else:

        streak = 1

    cursor.execute(

        "UPDATE users SET streak = ?, last_login = ? WHERE telegram_id = ?",

        (
            streak,
            str(today),
            user_id
        )
    )

    conn.commit()

    return streak