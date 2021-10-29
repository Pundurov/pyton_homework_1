with open('task_5.txt', 'w+') as f_obj:
    f_obj.write('10 20 31 55 66.5 80')
    f_obj.seek(0)
    str_f = f_obj.read()
    list_f = str_f.split()
    sum_num = 0
    for i in list_f:
        sum_num += float(i)

print(sum_num)