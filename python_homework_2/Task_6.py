i = 0
product_next = 'да'
product_list = []

while product_next == 'да':
    i += 1
    name = input('название: ')
    price = input('цена: ')
    number = input('количество: ')
    unit = input('единица измерения: ')
    product_list.append((i, {'название': name, 'цена': price, 'количество': number, 'ед': unit}))
    product_next = input('вводим следующий ?: да/нет')

nomenclature_dict = {}

for numb, prod_dict in product_list:
    for key, value in prod_dict.items():
        if not nomenclature_dict.get(key):
            nomenclature_dict[key] = [value]
        else:
            nomenclature_dict[key].append(value)

for key, value in nomenclature_dict.items():
    nomenclature_dict[key] = list(set(value))

print(nomenclature_dict)
