# Сколько шестибуквенных слов можно составить, начинающихся и заканчивающихся согласной буквой и содержащих 2 гласные?
# Из букв ТЫКВА. Каждая из допустимых букв может входить в слово несколько раз

count = 0

for b1 in 'ТЫКВА':
    for b2 in 'ТЫКВА':
        for b3 in 'ТЫКВА':
            for b4 in 'ТЫКВА':
                for b5 in 'ТЫКВА':
                    for b6 in 'ТЫКВА':
                        res = b1 + b2 + b3 + b4 + b5 + b6
                        if res[0] in 'ТКВ' and res[-1] in 'ТКВ':
                            if res.count('Ы') +  res.count('А') == 2:
                                print(res)
                                count += 1

print(f'Найдено {count} слова')