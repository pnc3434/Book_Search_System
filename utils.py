from datetime import date

# Запросить у пользователя целое число с повторением при ошибке
def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")

# Запросить оценку
def input_rating(prompt: str) -> int:
    while True:
        value = input_int(prompt)
        if 1 <= value <= 5:
            return value
        print("Ошибка: оценка должна быть от 1 до 5.")

# Запросить дату
def input_date(prompt: str) -> date:
    while True:
        try:
            return date.fromisoformat(
                input(prompt).replace(".", "-")
            )
        except ValueError:
            print("Ошибка: введите дату в формате ДД.ММ.ГГГГ.")

# Запросить непустую строку
def input_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: строка не может быть пустой.")