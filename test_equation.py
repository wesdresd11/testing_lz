from equation import equation

'''Ручная проверка по 3 тестам:
тест 1: a = 3, b = 4 - результат: -11.0, тест пройден
тест 2: a = 3, b = 3 - тест пройден, вызвана ошибка деления на ноль
тест 3: a = 4, b = 3 - тест пройден, вызвана ошибка, что a не должно быть больше b'''


test_cases = [(3, 4), (3, 3),(4, 3)]

for a, b in test_cases:
    try:
        result = equation(a, b)
        print(f"{a, b}: {result}")
    except (ZeroDivisionError, ValueError) as e:
        print(f"{a, b}: {e}")