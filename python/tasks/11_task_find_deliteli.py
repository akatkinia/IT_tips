# Задача
# Найти все делители входного числа (на которые можно разделить без остатка)

# Алгоритм неплохой, но он линейный
# n = int(input())
# i = 1

# while i <= n // 2:
#     if n % i == 0:
#         print(i, end = ' ')
#     i += 1
# print(n)

# Более лучший алгоритм:

n = int(input())
i = 1
a = []

while i * i < n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n//i)
    i += 1

a.sort()
print(sum(a))
print(a)
