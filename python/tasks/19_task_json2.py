# В json-файле group_people.json содержится информация о нескольких группах людей, при этом у каждой группы есть свой идентификатор. 
# Ваша задача скачать файлик и самостоятельно найти идентификатор группы, в которой находится самое большое количество женщин, рожденных после 1977 года. В качестве ответа необходимо указать через пробел идентификатор найденной группы и сколько в ней было женщин, рожденных после 1977 года.

import json

with open('group_people.json') as file:
    data = json.load(file)

maximum = 0
max_group = None

for group in data:
    id_group = group['id_group']
    count = 0

    for person in group['people']:
        gender = person['gender']
        year = person['year']

        if gender == 'Female' and year > 1977:
            count += 1

        if count > maximum:
            maximum = count
            max_group = id_group
            gender1 = gender
            
print(max_group, maximum, gender1)




    # print(group['people'][0])