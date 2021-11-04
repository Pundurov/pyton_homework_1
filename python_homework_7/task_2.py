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
    def __init__(self, V):
        self.V = V

    def fabric_consumption(self):
        return f'Расход ткани для пальто: {round(self.V / 6.5 + 0.5, 2)} м'


class SuitClass(ClothesAbstractClass):
    # атрибуты класса

    # методы класса
    def __init__(self, H):
        self.H = H

    @property
    def fabric_consumption(self):
        return f'Расход ткани для костюм: {round(self.H * 2 + 0.3, 2)} м'


coat_1 = CoatClass(10)
suit_1 = SuitClass(10)
print(coat_1.fabric_consumption())
print(suit_1.fabric_consumption)
