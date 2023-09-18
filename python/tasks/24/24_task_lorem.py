# В вашем распоряжении имеется следующий файл. Ваша задача скачать его и найти сколько уникальных слов используется в этом тексте, при этом регистр букв не нужно учитывать. Это значит, что слова Lorem и loRem являются эквивалентными.
# Например, если перед вами был бы такой текст:
    # Привет как дела
    # привет хорошо

# то здесь четыре уникальных слова.
# Между словами в файле стоят только пробелы и переносы строк, других разделителей нет.
# В качестве ответа укажите количество уникальных слов 


def find_uniq_words(file_name):
    words = []

    with open(file_name) as file:
        for line in file:
            for word in line.split():
                if word.lower() not in words:
                    words.append(word.lower())
        print(len(words))

find_uniq_words('lorem.txt')



#### Ещё вариант решения:
def find_uniq_words2(file_name):
    with open(file_name) as file:
        words = []

        for line in file:
            words.extend(line.rstrip().split(' '))
            lowercase_words = [item.lower() for item in words]
    print(len(set(lowercase_words)))

find_uniq_words2('lorem.txt')


### Ещё вариант решения:
import requests

url = r'https://stepik.org/media/attachments/course/63085/lorem.txt'
text = requests.get(url).text.lower()
print(len(set(text.split())))