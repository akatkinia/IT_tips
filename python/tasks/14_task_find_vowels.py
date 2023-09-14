# Задача
# Найти все пары гласных в тексте, которые идут подряд

vowels = 'aeiou'
text = 'aedsfiusdooass,cmsaa'

n = len(text)

for i in range(n - 1):
    if text[i] in vowels and text[i + 1] in vowels:
        print(text[i], text[i + 1])