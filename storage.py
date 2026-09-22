import json
import os

# Загрузить данные из JSON-файла
def load_json(filename: str) -> list:
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Ошибка чтения файла {filename}: {error}")
        return []

# Сохранить данные в JSON-файл
def save_json(filename: str, data: list) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError as error:
        print(f"Ошибка записи файла {filename}: {error}")