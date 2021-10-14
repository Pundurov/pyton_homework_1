# создание пустого списка
my_list = []
i = 0

# заполнение списка
while True:
    print('Введи новый элемент списка: число, текст, bool, список, кортеж, множетсво, словарь')
    print('Чтобы закончить ввод: пробел')
    my_list_mbr = input()
    if my_list_mbr == ' ':
        break
    else:
        my_list.insert(i, my_list_mbr)
        i += 1

i = 0
my_list_len = len(my_list)

# переворот попарно, кроме последнего нечётного
if my_list_len > 1:
    while i < my_list_len-1:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2

print(my_list)
