revenues = int(input("Enter the company's revenues/выручка: "))  # выручка
costs = int(input("Enter the company's costs/издержки: "))  # издержки

if revenues > costs:
    print("Фирма работает с прибылью !")
    print(f"Рентабельность фирмы: {(revenues - costs) / revenues}")
    number_of_employees = int(input("Enter the number of employees: "))  # число сотрудников
    print(f"Прибыль в среднем на сотрудника: {(revenues - costs) / number_of_employees}")
elif revenues < costs:
    print("Фирма принесла убыток (")
else:
    print("Отработали ноль-в-ноль.")
