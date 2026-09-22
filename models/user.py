from typing import List

class User:

    def __init__(self, user_id: int, name: str) -> None:
        # Создать объект пользователя
        self.id = user_id
        self.name = name

    def __str__(self) -> str:
        # Строковое представление пользователя
        return f"[{self.id}] {self.name}"

    @classmethod
    def from_data(cls, data: dict) -> "User":
        # Создать пользователя из словаря
        return cls(user_id=data["id"], name=data["name"])

    def to_data(self) -> dict:
        # Преобразовать объект в словарь.
        return {"id": self.id, "name": self.name}


def add_user(users: List[User], name: str) -> User:
    # Создать нового пользователя и добавить его в коллекцию
    new_id = max((user.id for user in users), default=0) + 1
    user = User(new_id, name)
    users.append(user)
    return user


def find_user_by_id(users: List[User], user_id: int) -> User | None:
    # Найти пользователя по идентификатору
    for user in users:
        if user.id == user_id:
            return user
    return None


def show_users(users: List[User]) -> None:
    if not users:
        print("Список пользователей пуст.")
        return
    for user in users:
        print(user)