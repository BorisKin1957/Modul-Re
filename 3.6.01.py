'''Найдите все последовательности, используя \w.
Что нужно сделать:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из \w
    Длина - максимально возможная

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Все найденные последовательности, каждая на новой строке.

'''

import re

result = re.finditer(r'\w+', input())

for match in result:
    print(match.group())