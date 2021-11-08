from abc import ABC, abstractmethod


class ClothesAbstractClass(ABC):
    # атрибуты класса

    # методы класса
    @abstractmethod
    def fabric_consumption(self):
        pass


class CoatClass(ClothesAbstractClass):
    # атрибуты класса

    # методы класса
    def __init__(self, v):
        self.v = v

    def fabric_consumption(self):
        return f'Расход ткани для пальто: {round(self.v / 6.5 + 0.5, 2)} м'


class SuitClass(ClothesAbstractClass):
    # атрибуты класса

    # методы класса
    def __init__(self, h):
        self.h = h

    @property
    def fabric_consumption(self):
        return round(self.h * 2 + 0.3, 2)

    def sum_suits(self, list_suits):
        sum_suits = 0
        for suit in list_suits:
            sum_suits += suit.fabric_consumption
        return f'Расход ткани на все костюмы: {sum_suits} м'


coat_1 = CoatClass(20)
suit_1 = SuitClass(10.5)
suit_2 = SuitClass(4.3)
suit_3 = SuitClass(8.5)
suit_4 = SuitClass(11)
list_all_suits = [suit_1, suit_2, suit_3, suit_4]
print(coat_1.fabric_consumption())
print(suit_1.fabric_consumption)
print(suit_1.sum_suits(list_all_suits))
