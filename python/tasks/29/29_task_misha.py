# 2. Дан файл в формате json, который представляет array из numeric. Файл не "красивый".
# вывести на экран сумму чисел


def sum_digits2(arr):

    with open(arr, 'r') as file:
        cleared_int = []
        
        for line in file:
            cleared = ''.join(filter(lambda char: char.isdigit() or char == ',', line)).split(',')
            cleared_int.extend([int(num) for num in cleared])  

        print(sum(cleared_int))


sum_digits2('test1.json')
