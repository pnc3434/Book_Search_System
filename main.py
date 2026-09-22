from books import (
    Book,
    add_book,
    find_book_by_id,
    get_top_books,
    search_by_genre,
    search_by_title,
    show_books,
)
from favorites import (
    add_to_favorites,
    remove_from_favorites,
    show_favorites,
)
from models.review import Review
from models.user import add_user, show_users
from storage import (
    load_books,
    load_favorites,
    load_users,
    save_books,
    save_favorites,
    save_users,
)
from utils import input_int, input_non_empty, input_rating

BOOKS_FILE = "data/books.json"
USERS_FILE = "data/users.json"
FAVORITES_FILE = "data/favorites.json"


def show_books_list(books: list[Book], title: str) -> None:
    # Вывести список книг с заголовком
    print(f"\n{title}")
    if not books:
        print("  Ничего не найдено.")
        return
    for book in books:
        print(f"  {book}")


def show_book_reviews(books: list[Book]) -> None:
    # Сценарий просмотра отзывов книг
    book_id = input_int("ID книги: ")
    book = find_book_by_id(books, book_id)
    if book is None:
        print("Книга не найдена")
        return
    print(f"\nКнига: {book.title}")
    print(f"Автор: {book.author}")
    print(f"Жанр: {book.genre}")
    print(f"Рейтинг: {book.rating}")
    print(f"Всего отзывов: {len(book.reviews)}")
    if not book.reviews:
        print("Отзывов пока нет.")
    else:
        for i, review in enumerate(book.reviews, 1):
            print(f"  {i}. {review}")


def add_review_to_book(books: list[Book]) -> None:
    # Сценарий добавления отзыва
    book_id = input_int("ID книги: ")
    book = find_book_by_id(books, book_id)
    if book is None:
        print("Книга не найдена")
        return
    user = input_non_empty("Ваше имя: ")
    text = input_non_empty("Текст отзыва: ")
    rating = input_rating("Оценка (1–5): ")
    book.add_review(Review(user, text, rating))
    print(f"Отзыв добавлен. Новый рейтинг: {book.rating}")


def main() -> None:
    # Основной цикл меню приложения
    books = load_books(BOOKS_FILE)
    users = load_users(USERS_FILE)
    favorites = load_favorites(FAVORITES_FILE)

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
        "11. Показать пользователей\n"
        "12. Добавить пользователя\n"
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
            show_book_reviews(books)
        elif choice == "6":
            add_review_to_book(books)
            save_books(BOOKS_FILE, books)
        elif choice == "7":
            book_id = input_int("ID книги: ")
            print(add_to_favorites(books, favorites, book_id))
            save_favorites(FAVORITES_FILE, favorites)
        elif choice == "8":
            book_id = input_int("ID книги: ")
            print(remove_from_favorites(favorites, book_id))
            save_favorites(FAVORITES_FILE, favorites)
        elif choice == "9":
            print(show_favorites(books, favorites))
        elif choice == "10":
            title = input_non_empty("Название: ")
            author = input_non_empty("Автор: ")
            genre = input_non_empty("Жанр: ")
            book = add_book(books, title, author, genre)
            print(f"Книга '{book.title}' добавлена с id={book.id}")
            save_books(BOOKS_FILE, books)
        elif choice == "11":
            show_users(users)
        elif choice == "12":
            name = input_non_empty("Имя пользователя: ")
            user = add_user(users, name)
            print(f"Пользователь '{user.name}' добавлен с id={user.id}")
            save_users(USERS_FILE, users)
        elif choice == "0":
            save_books(BOOKS_FILE, books)
            save_users(USERS_FILE, users)
            save_favorites(FAVORITES_FILE, favorites)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неизвестная команда, попробуйте снова.")


if __name__ == "__main__":
    main()