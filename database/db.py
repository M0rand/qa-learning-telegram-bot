import sqlite3

conn = sqlite3.connect("qa_bot.db")

cursor = conn.cursor()


cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    telegram_id INTEGER PRIMARY KEY,

    username TEXT,

    xp INTEGER DEFAULT 0,

    current_lesson INTEGER DEFAULT 1,

    streak INTEGER DEFAULT 0,

    last_login TEXT DEFAULT ''

)

""")

conn.commit()