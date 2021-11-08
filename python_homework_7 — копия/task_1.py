class Matrix:
    # атрибуты класса

    # методы класса
    def __init__(self, list_list):
        self.list_list = list_list

    def __add__(self, other):
        str_join = ''
        for i in range(len(self.list_list)):
            str_join_in = ''
            for j in range(len(self.list_list[i])):
                str_sum = self.list_list[i][j] + other.list_list[i][j]
                str_join_in += str(str_sum) + ' '
            str_join += str_join_in + '\n'
        return str_join

    def __str__(self):
        str_join = ''
        for i in range(len(self.list_list)):
            str_join += " ".join(map(str, self.list_list[i]))+ '\n'
        return str_join


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[10, 25, 30], [40, 50, 60], [70, 80, 90]])

print('Матрица matrix_1:')
print(matrix_1)
print('Матрица matrix_2:')
print(matrix_2)
print(matrix_1 + matrix_2)
