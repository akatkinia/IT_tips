# В этой задаче вам необходимо раскодировать текст, находящийся в данном текстовом файле Abracadabra__1_.txt. 
# Ключ для декодирования располагается в json-файле. 
# В качестве ответа нужно просто отправить получившийся текст.  
# И обратите внимание, что раскодировать нужно только лишь буквы
# Все остальные символы(цифры, знаки пунктуации и т.д.) необходимо выводить как есть.

import json

# откроем файл и запишем ему в переменную data
with open('Abracadabra__1_.txt', 'r') as file:
    text = file.read()

with open('Alphabet.json', 'r') as file:
    alphabet = json.load(file)

# получим декодированный текст
decoded_text = ''
for char in text:
    if char in alphabet:
        decoded_text += alphabet[char]
    else:
        decoded_text += char

print(decoded_text)


with open('result.txt', 'w') as file:
    file.write(decoded_text)


########## Ещё вариант
# import json

# with open('Abracadabra.txt', encoding='utf-8') as abra, open('Alphabet.json', encoding='utf-8') as alph:
#     data = json.load(alph)
#     text = abra.read()
#     for i in text:
#         print(data.get(i, i), end='')

# i - это ключ, который вы передаете в функцию get. В вашем случае i - это текущий символ, который вы ищете в словаре.
# i (после запятой) - это значение, которое будет возвращено, если ключ i отсутствует в словаре data.



########## Ещё вариант
# import json

# with open("Alphabet.json") as f:
#     key = json.load(f)
# with open("Abracadabra.txt", encoding="utf-8") as f:
#     txt = f.read()
# print(txt.translate(txt.maketrans(key)))