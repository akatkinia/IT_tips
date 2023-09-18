# 1. Дан файл в формате json, который представляет array из numeric. 
# Файл "красивый": на первой строке в самом начале скобка [, далее на каждой строке по числе, до числа 4 пробела, на последней строке в начале ], строки оканчиваются \n.
# вывести на экран сумму чисел


def find_digits(json_file):
    digits = []

    with open(json_file) as file:
        for line in file:
            cleared_line = line.strip('[],\n ')
            if cleared_line:
                digits.append(int(cleared_line))
        print(f'1. Сумма чисел в красивом json: {sum(digits)}')


# вариант без промежуточного массива

def find_digits2(json_file):
    digits_sum = 0

    with open(json_file) as file:
        for line in file:
            cleared_line = line.strip('[],\n ')
            if cleared_line:
                digits_sum += int(cleared_line)
        print(f'2. Сумма чисел в красивом json: {digits_sum}')


# вариант с модулем json

def find_digits3(json_file):
    import json

    with open(json_file, 'r') as file:
        data = json.load(file)
        print(f'3. Сумма чисел в красивом json: {sum(data)}')


find_digits('misha1.json')
find_digits2('misha1.json')
find_digits3('misha1.json')
