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
