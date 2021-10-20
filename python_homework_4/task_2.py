my_list = [1, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[i] for i in range(len(my_list)-1) if my_list[i - 1] < my_list[i]]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
