import random
import string

def generate_password(length=12):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return password

def check_strength(password):
    """Проверяет надёжность пароля (простая версия)"""
    if len(password) >= 12:
        return "Надёжный"
    elif len(password) >= 8:
        return "Средний"
    else:
        return "Слабый"

def main():
    print("=== Генератор паролей ===")
    length = int(input("Введите длину пароля: "))
    password = generate_password(length)
    strength = check_strength(password)
    print(f"Пароль: {password}")
    print(f"Надёжность: {strength}")

if __name__ == "__main__":
    main()