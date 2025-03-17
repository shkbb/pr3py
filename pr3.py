# Завдання 1: Перетворення рядка в число та зворотне перетворення

def convert_and_calculate(input_str):
    try:
        number = float(input_str)
        result = number * 2  # Просте арифметичне обчислення
        return str(result)
    except ValueError:
        return "Помилка: Введене значення не є числом."

# Приклад використання
input_value = "10.5"
print("Результат:", convert_and_calculate(input_value))

# Завдання 2: Арифметичні операції з введеними даними

def arithmetic_operations(str_num1, str_num2):
    try:
        num1, num2 = float(str_num1), float(str_num2)
        return (f"Сума: {num1 + num2}\n"
                f"Різниця: {num1 - num2}\n"
                f"Добуток: {num1 * num2}\n"
                f"Частка: {num1 / num2 if num2 != 0 else 'Помилка: ділення на нуль'}")
    except ValueError:
        return "Помилка: Введені значення мають бути числами."

# Приклад використання
print(arithmetic_operations("12", "4"))

# Завдання 3: Конвертація списку рядків у список чисел

def list_conversion(input_str):
    try:
        numbers = list(map(float, input_str.split(",")))
        return f"Сума: {sum(numbers)}\nСереднє значення: {sum(numbers) / len(numbers)}"
    except ValueError:
        return "Помилка: Невірний формат введення. Використовуйте коми для розділення чисел."

# Приклад використання
print(list_conversion("1, 2, 3, 4, 5"))

# Завдання 4: Форматування числових значень

def format_number(input_number, decimal_places=2):
    try:
        number = float(input_number)
        return f"Відформатоване число: {number:.{decimal_places}f}"
    except ValueError:
        return "Помилка: Введене значення не є числом."

# Приклад використання
print(format_number("3.1415926535", 4))
