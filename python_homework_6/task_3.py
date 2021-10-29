class Worker:
    # атрибуты класса

    # методы класса
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    # атрибуты класса

    # методы класса
    def get_full_name(self):
        return (f'{self.name} {self.surname}')

    def get_total_income(self):
        return (f'{self._income["wage"] + self._income["bonus"]}')


# экземпляр класса Road:
a = Position('May', 'Chao', 'Director', 100000, 50000)
print(f'Имя: {a.name}')
print(f'Фамилия: {a.surname}')
print(f'Должность: {a.position}')
print(f'Доходы: {a._income}')
print(f'З/п: {a._income["wage"]}')
print(f'Премия: {a._income["bonus"]}')
print(f'Полное имя: {a.get_full_name()}')
print(f'Полный доход: {a.get_total_income()}')

b = Worker('May', 'Chao', 'Director', 10, 5)
print(b._income)
