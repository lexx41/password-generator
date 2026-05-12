import random
import string

def generate_password(length=12):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return password

def main():
    length = int(input("Введите длину пароля: "))
    print(f"Пароль: {generate_password(length)}")

if __name__ == "__main__":
    main()