def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y


def main():
    print("🔢 Простой калькулятор")
    print("Операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    choice = input("Выбери операцию (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Неверный выбор.")
        return

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите число!")
        return

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)

    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
