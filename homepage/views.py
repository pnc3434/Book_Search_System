# View-функции главной страницы.

from django.shortcuts import render


def index(request):
    # Главная страница — рендерим из шаблона.
    return render(request, "homepage/index.html")


def page_not_found(request, exception):
    # Собственная страница 404 на базовом шаблоне.
    return render(
        request,
        "homepage/404.html",
        status=404,
    )