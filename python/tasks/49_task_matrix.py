# Дана матрица размером NxN, требуется найти максимальное значение среди элементов, расположенных на побочной диагонали.
# Под побочной диагональю матрицы подразумевается диагональ, проведённая из правого верхнего угла до левого нижнего угла.

# Входные данные
# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в списке, а затем в N строках записаны элементы списка.

# Выходные данные
# Вывести самой большой элемент на побочной диагонали 

n = int(input())

matrix= []

for i in range(n):
    matrix.append(list(map(int,input().split())))
max_value = matrix[0][n - 1]

for i in range (1, n):
    j = n - 1 - i
    if matrix[i][j] > max_value:
        max_value = matrix[i][j]

print(max_value)

