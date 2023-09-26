# Ваша задача создать функцию create_matrix, которая принимает

#     необязательный числовой параметр size - размер квадратной матрицы, по умолчанию принимает значение 3;
#     необязательный числовой параметр up_fill - значение заполнителя элементов, находящихся выше главной диагонали. По умолчанию равен 0;
#     необязательный числовой параметр down_fill - значение заполнителя элементов, находящихся ниже главной диагонали. По умолчанию равен 0;

# Функция create_matrix должна возвращать квадратную матрицу размером size х size, на диагонали которой располагаются числа от 1 до size. Все остальные элементы заполнены согласно параметрам up_fill и down_fill.


def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list:
    mas = [ [0] * size for _ in range(size) ]
    count = 0
    for line in range(size):
        for elem in range(size):
            if line == elem:
                mas[line][elem] = count + 1
                count += 1
            elif line < elem:
                mas[line][elem] = up_fill
            elif line > elem:
                mas[line][elem] = down_fill
    return mas


assert create_matrix(4) == [[1, 0, 0, 0],
                             [0, 2, 0, 0],
                               [0, 0, 3, 0],
                                 [0, 0, 0, 4]]
assert create_matrix(up_fill=7) == [[1, 7, 7],
                             [0, 2, 7],
                             [0, 0, 3]]
assert create_matrix(up_fill=7, down_fill=9) == [[1, 7, 7],
                                          [9, 2, 7],
                                          [9, 9, 3]]
assert create_matrix(size=4, up_fill=7, down_fill=9) == [[1, 7, 7, 7],
                                                  [9, 2, 7, 7],
                                                  [9, 9, 3, 7],
                                                  [9, 9, 9, 4]]


# Ещё вариант - более приоритетный, так как матрица не предзаполняется
def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list:
    matrix = []
    for i in range(size):
        line = []
        for j in range(size):
            if i == j:
                line.append(i + 1)
            elif i < j:
                line.append(up_fill)
            else:
                line.append(down_fill)
        matrix.append(line)
    return matrix