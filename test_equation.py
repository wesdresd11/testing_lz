#Вариант 6
from equation import equation
import pytest

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

#Автоматическая проверка
def test_normal():
    assert equation(3, 4) == -11.0

def test_a_equal_to_b():
    with pytest.raises(ZeroDivisionError) as e:
        equation(3, 3)
    assert "Ошибка деления на ноль, a не должно быть равно b" in str(e)

def test_a_greater_than_b():
    with pytest.raises(ValueError) as e:
        equation(4, 3)
    assert "a не должно быть больше b, так как корень будет считаться из отрицательного чисал, и на выходе получим комплексное" in str(e)