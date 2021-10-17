def sum_max2_of3(arg_1, arg_2, arg_3):
    """Возвращает сумму двух наибольших чисел

    :param arg_1: float
    :param arg_2: float
    :param arg_3: float
    :return: float
    """
    arg_1 = float(arg_1)
    arg_2 = float(arg_2)
    arg_3 = float(arg_3)

    return arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)


print(sum_max2_of3(100, 20, 30))
