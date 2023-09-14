# Задача
# К вам в руки попал файлик формата json , в котором содержится информация одного автосалона о продажах менеджеров. В файле указано для каждого менеджера список проданных им автомобилей, а также проставлена цена продажи каждого автомобиля.
# Ваша задача скачать файлик и самостоятельно найти самого успешного менеджера по итоговой сумме продаж. В качестве ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж.

import json


# десериализуем файл, хранящий JSON-строку, в питоновский объект dict
with open('manager_sales.json', 'r') as file:
    data = json.load(file)

# преобразуем объект в строку в формате js`on с отступами и выведем на экран, чтобы было удобно читать файл
data1 = json.dumps(data, ensure_ascii=False, indent=2)
# print(data1)
# print(type(data1))

# сохраним dict (который получили в переменной data) в файл, но уже с отступами. Т.е. сериализуем объект питона в JSON
with open('manager_sales2.json', 'w') as file:
    data2 = json.dump(data, file, ensure_ascii=False, indent=4)


# Теперь, проанализировав файл, можем приступить к решению задачи. Пройдёмся по нашему списку

# Для расчёта максимума создадим переменную (кто продал больше)
maximum = 0
max_first_name = ''
max_last_name = ''

for i in data:
    first_name = i['manager']['first_name']
    last_name = i['manager']['last_name']
    total = 0
    # price = i['cars'][0]['price']

    for car in i['cars']:
        total += car['price']

    # print(first_name, last_name, total)

    if total > maximum:
        maximum = total
        max_first_name = first_name
        max_last_name = last_name

print(max_first_name, max_last_name, maximum)




# Ещё одно решение

# import json

# with open('manager_sales.json', 'r') as file_json:
#     data = json.load(file_json)
# a = []
# for i in data:
#     a.append((i['manager']['first_name'], i['manager']['last_name'], sum(s['price'] for s in i['cars'])))

# print(*sorted(a, key=lambda x: x[2], reverse=True)[0])