# Напишите функцию shift_letter , которая принимает два аргумента:
#     letter одна английская буква в нижнем регистре
#     shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
# Функция shift_letter  сдвигает символ letter вперед или назад на заданное значение shift .Сдвиг может быть цикличным в пределах от a до z.

def shift_letter(letter: str, shift: int) -> str:
    "Функция сдвигает символ letter на shift позиций"
    shifted_code = ord(letter) + shift
    if shifted_code < ord('a'):
        shifted_code += 26
    elif shifted_code > ord('z'):
        shifted_code -= 26
    
    return chr(((shifted_code - ord('a')) % 26) + ord('a'))

print(shift_letter('d', 26))


# Ещё вариант решения:
def shift_letter(letter: str, shift: int):
    "Функция сдвигает символ letter на shift позиций"
    letter = ord(letter)
    ((letter - 97 + shift) % 26) + 97
    shletter = ((letter - 97 + shift) % 26) + 97
    res = chr(shletter)
    return res