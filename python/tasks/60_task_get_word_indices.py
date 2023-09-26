# В этой задаче вам необходимо создать функцию get_word_indices, которая принимает список строк и возвращает словарь, где ключи - это уникальные слова из списка строк в нижнем регистре, а значения - это списки индексов строк, в которых эти слова встречаются.
# Регистр букв не учитывается поэтому слова «String» и «STRING» считаются одинаковыми
# Нужно написать только определение функции get_word_indices 

def get_word_indices(strings: list[str]) -> dict:
    word_indices = {}
    for i, string in enumerate(strings):
        words = string.lower().split()
        for word in words:
            if word not in word_indices:
                word_indices[word] = [i]
            else:
                word_indices[word].append(i)

    return word_indices



# Проверка
assert get_word_indices(['This is a string',
                         'test String',
                         'test',
                         'string']) == {'this': [0], 'is': [0], 'a': [0],
                                        'string': [0, 1, 3], 'test': [1, 2]}

assert get_word_indices(['Look at my horse',
                         'my horse',
                         'is amazing']) == {'look': [0], 'at': [0], 'my': [0, 1],
                                            'horse': [0, 1], 'is': [2], 'amazing': [2]}

assert get_word_indices([]) == {}

assert get_word_indices(['Avada Kedavra',
                         'avada kedavra',
                         'AVADA KEDAVRA']) == {'avada': [0, 1, 2],
                                               'kedavra': [0, 1, 2]}

