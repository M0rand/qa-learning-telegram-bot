from database.db import cursor


def get_top_users():

    cursor.execute(

        """

        SELECT username, xp

        FROM users

        ORDER BY xp DESC

        LIMIT 10

        """
    )

    return cursor.fetchall()