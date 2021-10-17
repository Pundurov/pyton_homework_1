def user_sum(str_numbers, stop):
    sum_1 = 0
    str_list = str_numbers.split(' ')
    for i in str_list:
        if i == stop:
            break
        sum_1 += float(i)
    return sum_1


stopper = 'Y'
sum_sum = 0
finish = False

while not finish:
    user_input = input('Введи строку с числами через пробел. Для завершения введи: Y ')
    sum_sum += user_sum(user_input, stopper)
    finish = stopper in user_input
    print(sum_sum)
