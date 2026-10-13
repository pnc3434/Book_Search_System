# Система книжных отзывов

Консольное приложение для поиска книг, просмотра отзывов и ведения списка избранного.

## Возможности

- просмотр списка книг;
- поиск книг по жанру;
- поиск книг по подстроке в названии;
- топ книг по рейтингу;
- просмотр отзывов и оценок;
- добавление отзывов с пересчётом рейтинга;
- добавление и удаление книг из избранного;
- добавление новых книг.

## Структура проекта

- `main.py` — точка запуска и меню;
- `books.py` — работа с книгами (поиск, сортировка, топ);
- `reviews.py` — отзывы и оценки;
- `favorites.py` — избранное;
- `storage.py` — сохранение/загрузка JSON;
- `utils.py` — вспомогательные функции ввода;
- `data/` — JSON-файлы данных;
- `tests/` — автоматизированные тесты.

## Формат данных

- `data/books.json` — список книг;
- `data/favorites.json` — список id избранных книг.

## Требования

- Python 3.x;
- pytest;
- flake8.

## Установка зависимостей

pip install -r requirements.txt
## Запуск

python main.py
## Тесты

pytest

## Основные классы

### Book (`models/book.py`)
Атрибуты: `id`, `title`, `author`, `genre`, `rating`, `reviews`.

Методы:
- `add_review()` — добавить отзыв и пересчитать средний рейтинг;
- `is_suitable_genre()` — проверить, относится ли книга к жанру;
- `_calculate_rating()` — пересчитать средний рейтинг;
- `__str__()` — строковое представление;
- `from_data()` / `to_data()` — сериализация в JSON и обратно.

### Review (`models/review.py`)
Атрибуты: `user`, `text`, `rating`.

Методы:
- `__str__()` — строковое представление;
- `from_data()` / `to_data()` — сериализация.

Оценка валидируется в конструкторе: при значении вне диапазона 1–5 возбуждается `ValueError`.

### User (`models/user.py`)
Атрибуты: `id`, `name`.

Методы:
- `__str__()`, `from_data()`, `to_data()`.

## Взаимодействие объектов

- `Book` содержит коллекцию объектов `Review`.
- При добавлении отзыва `Book.add_review()` пересчитывает средний рейтинг.
- Список избранного хранится как список `id` книг.
- Функции работы с коллекциями (`books.py`, `reviews.py`, `favorites.py`) остаются обычными функциями.

## Веб-интерфейс (Django)

Проект дополнен веб-интерфейсом на Django 5.2.
Консольная версия (`main.py`) сохранена и продолжает работать.

### Запуск веб-версии

    python manage.py migrate    # один раз
    python manage.py runserver

Открыть в браузере: http://127.0.0.1:8000/

### Страницы

| URL | Назначение |
|---|---|
| `/` | Главная страница |
| `/books/` | Список книг |
| `/books/<id>/` | Карточка книги с отзывами |
| `/reviews/` | Все отзывы |
| `/admin/` | Админ-зона Django |

### Структура Django

- `bookreview/` — настройки Django-проекта;
- `homepage/` — главная страница и общий каркас `page()`;
- `catalog/` — книги (список, карточка);
- `feedback/` — отзывы.

Данные загружаются из JSON-файлов через `storage.py`.
Сущности `Book`, `Review`, `User` из `models/` используются напрямую.
Django ORM и база данных будут подключены на следующих практических работах.

## Django-шаблоны (ПР6)

Веб-интерфейс переведён с формирования HTML в Python на Django Template Language.

### Структура шаблонов

- `templates/base.html` — базовый шаблон;
- `templates/includes/navigation.html` — навигация;
- `homepage/templates/homepage/index.html` — главная;
- `homepage/templates/homepage/404.html` — страница 404;
- `catalog/templates/catalog/book_list.html` — список книг;
- `catalog/templates/catalog/book_detail.html` — карточка книги;
- `catalog/templates/catalog/includes/book_card.html` — карточка (include);
- `feedback/templates/feedback/review_list.html` — список отзывов.

### Статические файлы

- `homepage/static/homepage/css/style.css` — стили;
- `homepage/static/homepage/js/main.js` — JavaScript;
- `homepage/static/homepage/img/logo.png` — логотип (если добавлен).

### Использовано

- `{% extends %}` и `{% block %}` — наследование;
- `{% include %}` — повторно используемые фрагменты;
- `{% for %}` / `{% empty %}` — циклы;
- `{% if %}` — условия;
- `{% url %}` — именованные маршруты (с пространствами имён);
- фильтры `|length`, `|default`;
- `{% load static %}` и `{% static %}` — статика.

Функция `page()` удалена. Предметная область, JSON-хранилище и консольная версия сохранены.
Django ORM, база данных и формы — темы следующих практических работ.


