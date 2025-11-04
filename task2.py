import re
from typing import Callable


def generator_numbers(text: str):

    pattern = r'\s\d+\.\d+\s'
    matches = re.findall(pattern, text)

    for match in matches:
        number_str = match.strip()

        try:
            yield float(number_str)
        except ValueError:
            print(f"Помилка перетворення числа: {number_str}")
            continue


def sum_profit(text: str, func: Callable):
    # Викликаємо функцію-генератор, передану як аргумент,щоб отримати генератор чисел.
    number_generator = func(text)

    # Використовуємо вбудовану функцію sum() для ефективного підсумовування значень, що генеруються.
    total_sum = sum(number_generator)
    return total_sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
