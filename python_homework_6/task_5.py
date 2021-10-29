class Stationery:
    # атрибуты класса

    # методы класса
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    # атрибуты класса

    # методы класса
    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    # атрибуты класса

    # методы класса
    def draw(self):
        print('Запуск отрисовки карандашом.')


class Handle(Stationery):
    # атрибуты класса

    # методы класса
    def draw(self):
        print('Запуск отрисовки маркером.')

print('обращение к классу Stationery:')
s = Stationery('рисовальная принадлежность')
print(s.title)
s.draw()

print()

print('обращение к классу Pen:')
p = Pen('рисовальная принадлежность: ручка')
print(p.title)
p.draw()

print()

print('обращение к классу Pencil:')
pl = Pencil('рисовальная принадлежность: карандаш')
print(pl.title)
pl.draw()

print()

print('обращение к классу Handle:')
h = Handle('рисовальная принадлежность: маркер')
print(h.title)
h.draw()
