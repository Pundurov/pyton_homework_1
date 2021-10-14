user_str = input('Введите строку: ')

list_user_str = user_str.split()

for n, word in enumerate(list_user_str):
    print(f'№{n} {word[:10]}')
