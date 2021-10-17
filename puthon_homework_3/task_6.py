def h1(user_str):
    word = user_str[0].upper() + user_str[1:].lower()
    return word


str_h1 = input('Введи строку измаленьких букв: ')
print(h1(str_h1))
