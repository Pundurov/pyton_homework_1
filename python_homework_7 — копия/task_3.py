class CellOrg:
    # атрибуты класса

    # методы класса
    def __init__(self, cell_num):
        self.cell_num = cell_num

    def __add__(self, other):
        return CellOrg(self.cell_num + other.cell_num)

    def __sub__(self, other):
        if self.cell_num > other.cell_num:
            return CellOrg(self.cell_num - other.cell_num)
        else:
            return 'Разность меньше 0'

    def __mul__(self, other):
        return CellOrg(self.cell_num * other.cell_num)

    def __truediv__(self, other):
        return CellOrg(self.cell_num // other.cell_num)

    def __str__(self):
        return str(self.cell_num)

    def make_order(self, count):
        str_order = ''
        for i in range(1, self.cell_num + 1):
            str_order = str_order + '*' + '\n' if i % count == 0 else str_order + '*'
        return str_order


cell_1 = CellOrg(50)
cell_2 = CellOrg(31)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(7))
print(cell_2.make_order(10))
