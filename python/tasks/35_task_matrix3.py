# Задана целочисленная квадратная матрица размером N x N. Необходимо обойти элементы этой матрицы сверху вниз слева направо и вывести элементы именно в таком порядке в виде таблицы. 
# Программа принимает на вход натуральное число N – количество строк и столбцов матрицы. В каждой из последующих N строк записаны N целых чисел – элементы матрицы. Все числа во входных данных не превышают 100 по абсолютной величине.

n = int(input())		                     # Получаем размер матрицы	
a = []				                         # Переменная для хранения матрицы

for i in range(n):		                     # Каждый цикл это 1 строка
    a.append(list(map(int,input().split()))) # В строку добавляем массив

for i in range(n):  			             # Строка		 
    for j in range(n):  		             # Столбец
        print(a[j][i],end=' ')		         # Меняем индексы местами, столбец через пробел
    print()			                         # Переход на новую строку