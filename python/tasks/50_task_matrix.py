# Ваша задача сформировать квадратную матрицу размером NxN, в которой используется следующее заполнение:
#     все элементы, находящиеся выше главной диагонали, заполняются значением A;
#     все элементы, находящиеся ниже главной диагонали, заполняются значением B;
#     все элементы, находящиеся на главной диагонали, заполняются значением C.
# В качестве ответа, выведите на экран полученную матрицу

# Входные данные
# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в матрицы, а затем на новой строке три целых числа  A, B и C. Данные числа используются для заполнения

# Выходные данные
# Заполните и распечатайте матрицу

n = int(input()) # количество строк и столбцов (матрица NxN)
A, B, C = map(str, input().split())

matrix = [] # Переменная для хранения матрицы (списка со вложенными списками)

for i in range(n):
    matrix.append([0] * n) # первичное заполнение матрицы нулями

# for i in matrix:
#     print(i)

for i in range(n): # обходим все строки
    for j in range(n): # обходим все столбцы
        if i == j: # проверка нахождения главной диагонали
            matrix[i][j] = C
        elif i > j: # если номер строки будет больше главной диагонали (всё что ниже главной диагонали)
            matrix[i][j] = B
        else:
            matrix[i][j] = A

for i in matrix:
    print(*i)