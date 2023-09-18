# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Побеждает спортсмен, у которого максимален наилучший бросок. Если таких несколько, то из них побеждает тот, у которого наилучшая сумма результатов по всем попыткам. Если и таких несколько, победителем считается спортсмен с минимальным номером. Определите номер победителя соревнований.

# Входные данные
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.

# Выходные данные
# Программа должна вывести одно число - номер победителя соревнований. Не забудьте, что  строки  (спортсмены) нумеруются с 0.

n, m = map(int, input().split()) # n-кол-во строк, m-столбцов
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

max_score = 0
max_summ = 0
max_index = 0

for row in range(n):
    max_try = 0
    s = 0

    for column in range(m):
        s += a[row][column]
        if a[row][column] > max_try:
            max_try = a[row][column]

    # print(row, max_try, s)
    if max_try > max_score:
        max_score = max_try
        max_summ = s
        max_index = row
    elif max_try == max_score and s > max_summ:
        max_score = max_try
        max_summ = s
        max_index = row

print(max_index)

