import json
import os
from typing import List

from models.book import Book
from models.user import User


def load_json(filename: str) -> list:
    # Загрузить сырые данные из JSON-файла
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Ошибка чтения файла {filename}: {error}")
        return []


def save_json(filename: str, data: list) -> None:
    # Сохранить данные в JSON-файл
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError as error:
        print(f"Ошибка записи файла {filename}: {error}")


def load_books(filename: str) -> List[Book]:
    # Загрузить книги из JSON и преобразовать в объекты Book
    raw = load_json(filename)
    return [Book.from_data(item) for item in raw]


def save_books(filename: str, books: List[Book]) -> None:
    save_json(filename, [book.to_data() for book in books])


def load_users(filename: str) -> List[User]:
    # Загрузить пользователей из JSON
    raw = load_json(filename)
    return [User.from_data(item) for item in raw]


def save_users(filename: str, users: List[User]) -> None:
    # Сохранить пользователей в JSON
    save_json(filename, [user.to_data() for user in users])


def load_favorites(filename: str) -> list:
    # Загрузить список id избранного
    return load_json(filename)


def save_favorites(filename: str, favorites: list) -> None:
    # Сохранить список id избранного
    save_json(filename, favorites)