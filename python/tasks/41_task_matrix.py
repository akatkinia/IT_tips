# Проверьте, является ли двумерный массив симметричным относительно главной диагонали. Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний.

# Входные данные
# Программа получает на вход число n<100, являющееся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по n чисел, являющихся элементами массива.

# Выходные данные
# Программа должна выводить слово Yes для симметричного массива и слово No для несимметричного.

n = int(input())
mas = []

# создадим массив с матрицей
for i in range(n):
    mas.append(list(map(int, input().split())))


count = 0 # счетчик для подсчёта колличества неравных элементов

# пройдёмся по индексам строк и столбцов
for i in range(n):          # строки
    for j in range(n):      # столбцы
        if mas[i][j] != mas[j][i]:   # если элемент массива не равен равен противоположному элементу (чтобы с уверенностью сказать, что массив будет несимметричным)
            count += 1

if count > 0:
    print('No')
else:
    print('Yes')


