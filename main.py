import random
import string


def generate_password(length=12):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return password


def check_strength(password):
    if len(password) >= 12:
        return "Надёжный"
    elif len(password) >= 8:
        return "Средний"
    else:
        return "Слабый"


def main():
    print("=== Генератор паролей ===")

    while True:
        length = int(input("\nВведите длину пароля (0 - выход): "))
        if length == 0:
            print("До свидания!")
            break
        if length < 4:
            print("Минимальная длина 4 символа")
            continue

        password = generate_password(length)
        strength = check_strength(password)
        print(f"Пароль: {password}")
        print(f"Надёжность: {strength}")


if __name__ == "__main__":
    main()