# n = int(input())
# count = 0

# for p in range(n + 1, n * 2):
#     if p % 2 == 0 and p != 2 or p == 1:
#         continue

#     d = 3
#     is_plain = True
#     while d * d <= p:
#         if p % d == 0:
#             is_plain = False
#             break
#         d += 2
#     if is_plain:
#         count += 1

# print(count)


# Ещё решение

def is_plain_number(p):
    if p % 2 == 0 and p != 2 or p == 1:
        return False

    d = 3
    while d * d <= p:
        if p % d == 0:
            return False
        d += 2
    return True

n = int(input())
count = 0
for p in range(n + 1, n * 2):
    if is_plain_number(p):
        count += 1

print(count)

