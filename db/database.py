import sqlite3

DB_PATH = "data/bookreview.sqlite"


def get_connection():
    """Создать подключение к базе данных."""
    conn = sqlite3.connect(DB_PATH)
    # Включаем проверку внешних ключей
    conn.execute("PRAGMA foreign_keys = ON")
    # Позволяем обращаться к полям по именам (row["title"], а не row[0])
    conn.row_factory = sqlite3.Row
    return conn