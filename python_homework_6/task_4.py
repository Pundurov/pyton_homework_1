class Car:
    # атрибуты класса

    # методы класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула: {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')


class TownCar(Car):
    # атрибуты класса

    # методы класса
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Превышаете !')


class SportCar(Car):
    # атрибуты класса

    # методы класса
    def show_speed(self):
        super().show_speed()

class WorkCar(Car):
    # атрибуты класса

    # методы класса
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Превышаете !')


class PoliceCar(Car):
    # атрибуты класса

    # методы класса
    def show_speed(self):
        super().show_speed()

print('обращение к классу Car')
c = Car(100, 'Red', 'Lada', False)
print(f'Скорость: {c.speed} км/ч, Цвет: {c.color}, Название: {c.name}')
print(c.is_police)
c.go()
c.stop()
c.turn('вправо')
c.show_speed()

print()

print('обращение к классу TownCar')
t = TownCar(70, 'Green', 'Niva', False)
print(f'Скорость: {t.speed} км/ч, Цвет: {t.color}, Название: {t.name}')
print(t.is_police)
t.go()
t.stop()
t.turn('влево')
t.show_speed()

print()

print('обращение к классу SportCar')
s = SportCar(170, 'Yellow', 'F1', False)
print(f'Скорость: {s.speed} км/ч, Цвет: {s.color}, Название: {s.name}')
print(s.is_police)
s.go()
s.stop()
s.turn('назад')
s.show_speed()

print()

print('обращение к классу WorkCar')
w = WorkCar(50, 'Grey', 'Gazelle', False)
print(f'Скорость: {w.speed} км/ч, Цвет: {w.color}, Название: {w.name}')
print(w.is_police)
w.go()
w.stop()
w.turn('разворот')
w.show_speed()

print()

print('обращение к классу PoliceCar')
p = PoliceCar(120, 'Blue', 'Ford', True)
print(f'Скорость: {p.speed} км/ч, Цвет: {p.color}, Название: {p.name}')
print(p.is_police)
p.go()
p.stop()
p.turn('разворот')
p.show_speed()