def my_func(x, y):
    float(x)
    int(y)
    first_way = x ** y

    for _ in range(abs(y) - 1):
        x *= x
    second_way = 1 / x
    return {'способ **: ': round(first_way, 3),
            'способ без **: ': round(second_way, 3)}


for key, value in my_func(9.1, -2).items():
    print(f'{key}: {value}')
