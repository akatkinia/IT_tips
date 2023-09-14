# Задача
# Перебор всевозможных комбинаций из 3 символов

from string import printable

for b1 in printable:
    for b2 in printable:
        for b3 in printable:
            print(b1, b2, b3)