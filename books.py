from typing import Optional

# Добавить новую книгу в список
def add_book(books: list[dict], title: str, author: str, genre: str) -> dict:
    new_id = max((book["id"] for book in books), default=0) + 1
    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "genre": genre,
        "rating": 0.0,
        "reviews": [],
    }
    books.append(book)
    return book

# Найти книгу по идентификатору
def find_book_by_id(books: list[dict], book_id: int) -> Optional[dict]:
    for book in books:
        if book["id"] == book_id:
            return book
    return None

# Найти книги по жанру
def search_by_genre(books: list[dict], genre: str) -> list[dict]:
    return [book for book in books if book["genre"].lower() == genre.lower()]

# Найти книги по подстроке в названии
def search_by_title(books: list[dict], query: str) -> list[dict]:
    return [book for book in books if query.lower() in book["title"].lower()]

# Отсортировать книги по рейтингу
def sort_books_by_rating(books: list[dict]) -> list[dict]:
    return sorted(books, key=lambda book: book["rating"], reverse=True)

# Вернуть топ-N книг по рейтингу
def get_top_books(books: list[dict], n: int = 3) -> list[dict]:
    return sort_books_by_rating(books)[:n]