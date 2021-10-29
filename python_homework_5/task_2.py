with open('task_2.txt') as f_obj:
    n_lines = 0
    n_words = {}
    for line in f_obj:
        n_words[n_lines] = (len(line.split(' ')))
        n_lines += 1

print(f'Всего строк: {n_lines}.')
for key, value in n_words.items():
    print(f'В строке {key+1} - {value} слов.')
