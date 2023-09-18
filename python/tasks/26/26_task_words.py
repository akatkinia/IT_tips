# В этой задаче вам необходимо обработать файл с названием words.txt, содержащий множество неуникальных слов. Само содержимое файла можно посмотреть здесь. Ваша задача найти в нем все слова, заканчивающиеся на строку ЕЯ, и вывести их на экран. При этом нужно:
#     исключить дубли
#     привести все буквы к верхнему регистру
#     расположить слова в выводе в порядке двойной сортировки: сперва отсортировать по возрастанию длины слова, а при одинаковых значениях длины расположить по алфавиту

# Значит, если бы перед вам был файл с содержимым:
# панацея
# газосварщик
# ФЕЯ
# затея
# лапочка
# Гея
# панацея
# богая
# ливрея
# ШЕЯ
# я
# Камыш

# то ответ должен быть таким:
# ГЕЯ
# ФЕЯ
# ШЕЯ
# ЗАТЕЯ
# ЛИВРЕЯ
# ПАНАЦЕЯ

# Не забывайте про кодировку

RESULT = []

with open('words.txt') as file:
    upper_list = file.read().upper().split()
    for word in upper_list:
        if word.endswith('ЕЯ'):
            RESULT.append(word)

RESULT = set(RESULT)
RESULT = sorted(RESULT, key=lambda word: (len(word), word))

print(*RESULT, sep='\n')
# for i in RESULT:
    # print(i)


### Ещё вариант решения:
with open('words.txt', encoding='utf-8') as file:
    my_set = {i.strip().upper() for i in file if i.strip().upper().endswith('ЕЯ')}
    print(*sorted(my_set, key=lambda x: (len(x), x)), sep='\n')
