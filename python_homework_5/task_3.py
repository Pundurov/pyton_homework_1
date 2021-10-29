with open('task_3.txt', 'r', encoding='utf-8') as f_obj:
    n_lines = len(f_obj.readlines())
    mid_sal = 0
    i = 0
    f_obj.seek(0)
    print('Оклад менее 20 тысяч:')
    while i < n_lines:
        n_str = f_obj.readline()
        n_words = n_str.split()
        if float(n_words[1]) < 20000:
            print(f'{n_words[0]} {n_words[1]}')
        mid_sal += float(n_words[1])
        i += 1

print(f'Средний доход: {round(mid_sal / n_lines, 2)}')
