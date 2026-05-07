import sqlite3

connection = sqlite3.connect("career_bot.db")
cursor = connection.cursor()

# таблиця користувачів
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    username TEXT,
    answer1 TEXT,
    answer2 TEXT,
    profession TEXT
)
""")

connection.commit()

print("Таблиця створена!")