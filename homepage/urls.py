# Маршруты главной страницы.

from django.urls import path  # функция для описания маршрутов

from . import views  # импорт views из текущего приложения

urlpatterns = [
    # Пустой путь "" в приложении соответствует корню,
    path("", views.index, name="index"),
]
