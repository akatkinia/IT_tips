# Задана целочисленная матрица, состоящая из N строк и M столбцов. Необходимо обойти элементы этой матрицы слева направо снизу вверх и вывести элементы именно в таком порядке в виде таблицы. 
# Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы. В каждой из последующих N строк записаны M целых чисел – элементы матрицы. 

n, m = list(map(int, input().split()))

a = []                               # создал новый список

for i in range(n):
    a.append(list(input().split()))  # добавляем элементы в список a

for i in range(n - 1, -1, -1):       # обход по строкам 
    for j in range(m):               # обход по строкам 
        print(a[i][j], end=' ')      # печатаем символ
    print()                          # переход на новую строку