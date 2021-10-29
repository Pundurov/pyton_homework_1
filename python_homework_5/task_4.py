with open('task_4.txt', 'r', encoding='utf-8') as f_obj, open('task_4_2.txt', 'w', encoding='utf-8') as f_obj2:
    n_lines = len(f_obj.readlines())
    translate_list = ['Один ', 'Два ', 'Три ', 'Четыре ']
    i = 0
    f_obj.seek(0)
    while i < n_lines:
        n_str = f_obj.readline()
        n_words = n_str.split()
        n_words[0] = translate_list[i]
        n_words[1] = '- '
        n_words.append('\n')
        f_obj2.writelines(n_words)
        i += 1
