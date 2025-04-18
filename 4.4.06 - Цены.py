'''Напишите программу, которая находит в строке первую попавшуюся цену, и выводит её в следующем виде: Цена данного товара x. Если цены нет в тексте - ничего выводить не нужно.
Что нужно сделать:

Нужно найти первую цену в тексте:

    Любая числовая последовательность
    В конце стоит ₽$

и подставить её в строку Цена данного товара x.'''

import re

match = re.search(r'\b(\d+)([₽$])', input())

if match:
    print(match.expand(r'Цена данного товара \1\2'))