def division(arg_1, arg_2):
    """Возвращает частное от деления

    :param arg_1: float
    :param arg_2: float
    :return: arg_1 / arg_2 or message "Деление на ноль!"
    """
    arg_1 = float(arg_1)
    arg_2 = float(arg_2)
    return round(arg_1 / arg_2, 3) if arg_2 != 0 else "Деление на ноль!"


print(division(input('Введи делимое: '), input('Введи делитель: ')))
