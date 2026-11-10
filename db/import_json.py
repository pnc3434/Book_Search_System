import json
from db.database import get_connection

BOOKS_FILE = "data/books.json"


def load_json(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def import_books(conn):
    books = load_json(BOOKS_FILE)
    conn.executemany(
        """
        INSERT INTO books (id, title, author, genre)
        VALUES (?, ?, ?, ?)
        """,
        [
            (book["id"], book["title"], book["author"], book["genre"])
            for book in books
        ],
    )


def import_reviews(conn):
    books = load_json(BOOKS_FILE)
    reviews_data = []
    review_id = 1

    # Собираем отзывы из всех книг в один список
    for book in books:
        for review in book.get("reviews", []):
            reviews_data.append((
                review_id,
                book["id"],
                review["user"],
                review["text"],
                review["rating"]
            ))
            review_id += 1

    conn.executemany(
        """
        INSERT INTO reviews (id, book_id, user_name, text, rating)
        VALUES (?, ?, ?, ?, ?)
        """,
        reviews_data,
    )


def import_users(conn):
    conn.execute(
        "INSERT INTO users (id, name) VALUES (?, ?)",
        (1, "Иван Петров")
    )


def main():
    conn = get_connection()
    try:
        print("Импорт книг...")
        import_books(conn)
        print("Импорт отзывов...")
        import_reviews(conn)
        print("Импорт пользователей...")
        import_users(conn)
        
        conn.commit()
        print("Импорт успешно завершен!")
    except Exception as e:
        conn.rollback()
        print(f"Ошибка импорта: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()