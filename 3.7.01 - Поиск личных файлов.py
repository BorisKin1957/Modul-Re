'''Нужно найти последовательности, подходящие по следующим условиям:

    Начинается с https://imgur.com/
    Потом идёт 7 симолов из следующего диапазона: a-z, A-Z, 0-9

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Ваша задача вывести все ссылки в тексте.

 Sample Output 1:

https://imgur.com/pecSvGK
https://imgur.com/LHbcwKW'''

import re

regex = r'(?i)(?:https://imgur.com/)[a-z0-9]{7}'
result = re.findall(regex, input())

print(*result, sep='\n')