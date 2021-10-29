class Road:
    # атрибуты класса

    # методы класса
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_road(self, sq_m_sm, road_thns_sm):
        self.sq_m_sm = sq_m_sm
        self.road_thns_sm = road_thns_sm
        return self._length * self._width * self.sq_m_sm * self.road_thns_sm / 1000


# экземпляр класса Road:
a = Road(1000, 10)
print(f'{a.mass_road(20, 10)} т.')
