# Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).

# Входные данные
# Программа получает на вход два числа n и m.

# Выходные данные
# Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.


n, m = map(int, input().split())    # ввод строки/стобцы
u = 0                   # счетчик

for i in range(n):      # цикл строка
    a = []              # список для строки
    for j in range(m):  # цикл столбцы в строке
        a.append(u)     # добавляем в список число
        u += 1          # к числу прибавляем +1
        
    # сразу же в этом цикле печатаем матрицу
    if i % 2 != 0:        # если не четная строка 
        a.reverse()       # переворачиваем список
    if i == 0:
        print(*a) # для 0 строки
    else:
        print(*a)


# Ещё вариант:
n, m = map(int, input().split())

for i in range(n):
    if i % 2 == 0:
        print(*list(range(i * m, i * m + m)))
    else:
        print(*list(range(i * m, i * m + m))[::-1])


# Ещё вариант:
n, m = map(int, input().split())
k = []
u = 0
for i in range(n):
    a = []
    for j in range(m):
        a.append(u)
        u += 1
    k.append(a)
    if i % 2 != 0:
        a.reverse()
    if i == 0:
        print(*a, sep = '  ')
    else:
        print('', *a)