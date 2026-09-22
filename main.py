from books import (
    add_book,
    get_top_books,
    search_by_genre,
    search_by_title,
)
from favorites import (
    add_to_favorites,
    remove_from_favorites,
    show_favorites,
)
from reviews import add_review, get_book_reviews
from storage import load_json, save_json
from utils import input_int, input_non_empty, input_rating

BOOKS_FILE = "data/books.json"
FAVORITES_FILE = "data/favorites.json"


def show_books(books: list[dict]) -> None:
# Вывести список всех книг
    if not books:
        print("Список книг пуст.")
        return
    for book in books:
        print(
            f"[{book['id']}] {book['title']} — {book['author']} "
            f"({book['genre']}), рейтинг: {book['rating']}"
        )


def show_books_list(books: list[dict], title: str) -> None:
#    Вывести список книг с заголовком
    print(f"\n{title}")
    if not books:
        print("  Ничего не найдено.")
        return
    for book in books:
        print(
            f"  [{book['id']}] {book['title']} — {book['author']}, "
            f"рейтинг: {book['rating']}"
        )


def main() -> None:
    # Основной цикл меню приложения
    books = load_json(BOOKS_FILE)
    favorites = load_json(FAVORITES_FILE)

    menu = (
        "\n=== Система книжных отзывов ===\n"
        "1. Показать все книги\n"
        "2. Поиск по жанру\n"
        "3. Поиск по названию\n"
        "4. Топ книг по рейтингу\n"
        "5. Показать отзывы книги\n"
        "6. Добавить отзыв\n"
        "7. Добавить книгу в избранное\n"
        "8. Удалить книгу из избранного\n"
        "9. Показать избранное\n"
        "10. Добавить новую книгу\n"
        "0. Выход"
    )

    while True:
        print(menu)
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_books(books)
        elif choice == "2":
            genre = input_non_empty("Жанр: ")
            show_books_list(
                search_by_genre(books, genre),
                f"Книги в жанре '{genre}':",
            )
        elif choice == "3":
            query = input_non_empty("Подстрока в названии: ")
            show_books_list(
                search_by_title(books, query),
                f"Найдено по запросу '{query}':",
            )
        elif choice == "4":
            show_books_list(
                get_top_books(books, 3),
                "Топ-3 книги по рейтингу:",
            )
        elif choice == "5":
            book_id = input_int("ID книги: ")
            print(get_book_reviews(books, book_id))
        elif choice == "6":
            book_id = input_int("ID книги: ")
            user = input_non_empty("Ваше имя: ")
            text = input_non_empty("Текст отзыва: ")
            rating = input_rating("Оценка (1–5): ")
            print(add_review(books, book_id, user, text, rating))
            save_json(BOOKS_FILE, books)
        elif choice == "7":
            book_id = input_int("ID книги: ")
            print(add_to_favorites(books, favorites, book_id))
            save_json(FAVORITES_FILE, favorites)
        elif choice == "8":
            book_id = input_int("ID книги: ")
            print(remove_from_favorites(favorites, book_id))
            save_json(FAVORITES_FILE, favorites)
        elif choice == "9":
            print(show_favorites(books, favorites))
        elif choice == "10":
            title = input_non_empty("Название: ")
            author = input_non_empty("Автор: ")
            genre = input_non_empty("Жанр: ")
            book = add_book(books, title, author, genre)
            print(f"Книга '{book['title']}' добавлена с id={book['id']}")
            save_json(BOOKS_FILE, books)
        elif choice == "0":
            save_json(BOOKS_FILE, books)
            save_json(FAVORITES_FILE, favorites)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неизвестная команда, попробуйте снова.")


if __name__ == "__main__":
    main()