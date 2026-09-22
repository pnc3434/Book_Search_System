from books import (
    add_book,
    find_book_by_id,
    get_top_books,
    search_by_genre,
    search_by_title,
    sort_books_by_rating,
)


def make_sample_books() -> list[dict]:
# cоздать набор тестовых книг
    books: list[dict] = []
    add_book(books, "Война и мир", "Лев Толстой", "Роман")
    add_book(books, "Собачье сердце", "Михаил Булгаков", "Повесть")
    books[0]["rating"] = 4.5
    books[1]["rating"] = 4.2
    return books


def test_add_book():
    books: list[dict] = []
    book = add_book(books, "Тест", "Автор", "Жанр")
    assert book["id"] == 1
    assert len(books) == 1


def test_find_book_by_id():
    books = make_sample_books()
    assert find_book_by_id(books, 1)["title"] == "Война и мир"
    assert find_book_by_id(books, 99) is None


def test_search_by_genre():
    books = make_sample_books()
    result = search_by_genre(books, "роман")
    assert len(result) == 1
    assert result[0]["title"] == "Война и мир"


def test_search_by_title():
    books = make_sample_books()
    result = search_by_title(books, "сердце")
    assert len(result) == 1
    assert result[0]["author"] == "Михаил Булгаков"


def test_sort_and_top_books():
    books = make_sample_books()
    sorted_books = sort_books_by_rating(books)
    assert sorted_books[0]["title"] == "Война и мир"
    top = get_top_books(books, 1)
    assert len(top) == 1