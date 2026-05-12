import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("=== Генератор паролей ===")
    length = int(input("Введите длину пароля: ") or 12)
    print(f"Пароль: {generate_password(length)}")

if __name__ == "__main__":
    main()