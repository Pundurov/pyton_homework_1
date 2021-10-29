import time


class TrafficLight:
    # атрибуты класса

    # методы класса
    def running(self, color_red, color_yellow, color_green):
        if (color_red != 'Красный') or (color_yellow != 'Жёлтый') or (color_green != 'Зелёный'):
            print("Неправильный порядок цветов светофора !")
        else:
            self.color_red = color_red
            print(color_red)
            time.sleep(7)
            self.color_yellow = color_yellow
            print(color_yellow)
            time.sleep(2)
            self.color_green = color_green
            print(color_green)
            time.sleep(10)



# экземпляр класса TrafficLight:
a = TrafficLight()
a.running('Красный', 'Жёлтый', 'Зелёный')

b = TrafficLight()
b.running('Жёлтый', 'Зелёный', 'Красный')
