my_list = [7, 5, 3, 3, 2]

user_rtg = int(input('Введите оценку 1-9: '))

inserted = False
for i, elem in enumerate(my_list):
    if user_rtg > elem:
        my_list.insert(i, user_rtg)
        inserted = True
        break

if not inserted:
    my_list.append(user_rtg)

print(my_list)

# вариант решения
# my_list.append(user_rtg)
# my_list.sort(reverse=True)
# print(my_list)
