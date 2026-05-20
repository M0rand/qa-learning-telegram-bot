import sqlite3

conn = sqlite3.connect(
    "qa_bot.db"
)

cursor = conn.cursor()

cursor.execute(

    """
    CREATE TABLE IF NOT EXISTS users (

        user_id INTEGER PRIMARY KEY,

        xp INTEGER DEFAULT 0,

        level TEXT DEFAULT 'Intern',

        current_lesson INTEGER DEFAULT 1,

        streak INTEGER DEFAULT 0,

        last_login TEXT
    )
    """
)

cursor.execute(

    """
    CREATE TABLE IF NOT EXISTS completed_lessons (

        user_id INTEGER,

        block_id TEXT,

        lesson_index INTEGER,

        PRIMARY KEY (
            user_id,
            block_id,
            lesson_index
        )
    )
    """
)

conn.commit()