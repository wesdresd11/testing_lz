

def equation(a: float, b: float) -> float:
    if a == b:
        raise ZeroDivisionError("Ошибка деления на ноль, a не должно быть равно b")
    if a > b:
        raise ValueError("a не должно быть больше b, так как корень будет считаться из отрицательного чисал, и на выходе получим комплексное")
    return (((a * b) / (a - b)) + (b - a) ** 0.5)