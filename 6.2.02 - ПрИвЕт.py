'''Найдите все слова привет. Регистр учитывать не нужно.
Что нужно сделать:

Нужно найти слова привет в разном регистре.'''


import re

regex = re.compile(r'(?i)Привет')
result = re.findall(regex, input())

if result:
    print(result)

