with open('task_1.txt', 'w') as file:
    input_line = ' '
    while input_line:
        input_line = input('Введите текст: \n')
        if input_line == '':
            break
        file.write(f'{input_line}\n')


