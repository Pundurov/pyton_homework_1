# создание пустого списка
my_list = []

# заполнение списка
my_list.append(1)  # int
my_list.append('time')  # str
my_list.append(True)  # bool
my_list.append([1, 2, 3])  # list
my_list.append(('a', 'b', 3))  # tuple
my_list.append({1, 2})  # set
my_list.append({'age': '40', 'name': 'Anton', 'man': True})  # dict

print(my_list)

for item in my_list:
    print(type(item))
