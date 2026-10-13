# View-функции главной страницы и общий каркас страниц.

from django.http import HttpResponse


def page(title, content):
    # Собираем HTML-страницу с единым каркасом.
    # title — заголовок вкладки, content — HTML-содержимое.
    bootstrap = (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
        "/dist/css/bootstrap.min.css"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{bootstrap}">
</head>
<body>
<nav class="nav bg-light px-3 py-2 mb-3">
    <a class="nav-link" href="/">Главная</a>
    <a class="nav-link" href="/books/">Книги</a>
    <a class="nav-link" href="/reviews/">Отзывы</a>
</nav>
<main class="container pb-5">{content}</main>
</body>
</html>"""


def index(request):
    # Главная страница с кнопками-ссылками на разделы.
    content = """
    <h1 class="display-4">Система книжных отзывов</h1>
    <p class="lead">Каталог книг с отзывами и оценками.</p>
    <p>Основные разделы:</p>
    <a href="/books/" class="btn btn-primary me-2">Книги</a>
    <a href="/reviews/" class="btn btn-secondary">Отзывы</a>
    """
    return HttpResponse(page("Система книжных отзывов", content))


def page_not_found(request, exception):
    # Собственная страница 404.
    content = """
    <h1 class="text-danger">404 — страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 — страница не найдена", content),
        status=404,
    )
