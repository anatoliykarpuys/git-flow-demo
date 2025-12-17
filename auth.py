# auth.py
def login(username, password):
    """Функция входа в систему"""
    # Простая проверка (для демонстрации)
    if username == "admin" and password == "12345":
        return f"Добро пожаловать, {username}!"
    else:
        return "Ошибка: неверный логин или пароль"
