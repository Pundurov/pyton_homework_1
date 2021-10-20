from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    print(el)

i = 1
num_list = [x for x in range(5)]
for el in cycle(num_list):
    if i > 12:
        break
    print(el)
    i += 1


