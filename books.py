from typing import List, Optional

from models.book import Book


def add_book(
    books: List[Book], title: str, author: str, genre: str
) -> Book:
    # Создать новую книгу и добавить её в коллекцию
    new_id = max((book.id for book in books), default=0) + 1
    book = Book(new_id, title, author, genre)
    books.append(book)
    return book


def find_book_by_id(books: List[Book], book_id: int) -> Optional[Book]:
    # Найти книгу по идентификатору
    for book in books:
        if book.id == book_id:
            return book
    return None


def search_by_genre(books: List[Book], genre: str) -> List[Book]:
    # Найти книги по жанру
    return [book for book in books if book.is_suitable_genre(genre)]


def search_by_title(books: List[Book], query: str) -> List[Book]:
    # Найти книги по подстроке в названии
    return [book for book in books if query.lower() in book.title.lower()]


def sort_books_by_rating(books: List[Book]) -> List[Book]:
    # Отсортировать книги по рейтингу (по убыванию)
    return sorted(books, key=lambda book: book.rating, reverse=True)


def get_top_books(books: List[Book], n: int = 3) -> List[Book]:
    # Вернуть топ-N книг по рейтингу
    return sort_books_by_rating(books)[:n]


def show_books(books: List[Book]) -> None:
    # Вывести список всех книг
    if not books:
        print("Список книг пуст.")
        return
    for book in books:
        print(book)