from books import (
    Book,
    add_book,
    find_book_by_id,
    get_top_books,
    search_by_genre,
    search_by_title,
    sort_books_by_rating,
)
from models.review import Review


def make_sample_books() -> list[Book]:
    """Создать набор тестовых книг."""
    books: list[Book] = []
    b1 = add_book(books, "Война и мир", "Лев Толстой", "Роман")
    b1.add_review(Review("Анна", "Гениально!", 5))
    b1.add_review(Review("Иван", "Затянуто", 4))
    b2 = add_book(books, "Собачье сердце", "Михаил Булгаков", "Повесть")
    b2.add_review(Review("Пётр", "Отлично", 5))
    return books


def test_add_book():
    books: list[Book] = []
    book = add_book(books, "Тест", "Автор", "Жанр")
    assert book.id == 1
    assert book.title == "Тест"
    assert len(books) == 1


def test_find_book_by_id():
    books = make_sample_books()
    assert find_book_by_id(books, 1).title == "Война и мир"
    assert find_book_by_id(books, 99) is None


def test_search_by_genre():
    books = make_sample_books()
    result = search_by_genre(books, "роман")
    assert len(result) == 1
    assert result[0].title == "Война и мир"


def test_search_by_title():
    books = make_sample_books()
    result = search_by_title(books, "сердце")
    assert len(result) == 1
    assert result[0].author == "Михаил Булгаков"


def test_sort_and_top_books():
    books = make_sample_books()
    sorted_books = sort_books_by_rating(books)
    assert sorted_books[0].title == "Собачье сердце"
    top = get_top_books(books, 1)
    assert len(top) == 1


def test_book_rating_and_str():
    books = make_sample_books()
    book = books[0]
    assert book.rating == 4.5
    assert "Война и мир" in str(book)


def test_book_is_suitable_genre():
    books = make_sample_books()
    assert books[0].is_suitable_genre("роман")
    assert not books[0].is_suitable_genre("Повесть")