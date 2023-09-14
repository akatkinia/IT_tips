# Задача
# Определить, все ли элементы в списке являются чётными

a = [54, 4, 58, 24, 48]

while len(a) > 0:
    last = a.pop()
    if last % 2 != 0:
        print(f'Найдено нечетное число {last}')
        break
else:
    print ('YES')