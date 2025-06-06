'''Нужно вывести все электронные почты, которые есть в тексте.
Что нужно сделать:

Нужно найти последовательности, подходящие по следующим условиям:

    Начинается как минимум с одного из следующих символов: a-z, A-Z, 0-9, -, _
    Потом идёт @
    После @ снова идёт как минимум один из следующих символов: a-z, A-Z, 0-9
    Потом идёт .
    После . снова идёт как минимум один из следующих символов: a-z, A-Z, 0-9

Адрес почты не может быть подпоследовательностью.'''

import re

regex = r'(?i)(?<!\S)[a-z0-9_-]+@[a-z0-9]+\.[a-z0-9]+'

result = re.findall(regex, input())

print(*result, sep='\n')