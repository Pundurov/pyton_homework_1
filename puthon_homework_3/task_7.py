def h1(user_str):
    word = user_str[0].upper() + user_str[1:].lower()
    return word


str_h1 = input('Введи строку слов из маленьких букв: ')

str_list = str_h1.split(' ')

for i in str_list:
    print(f'{h1(i)} ', end=' ')
