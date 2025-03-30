'''Нужно найти последовательности, подходящие по следующим условиям:

    Начинается с Категория:
    Потом идёт последовательность из кириллических символов обоих регистров и пробелов
    Минимальная длина последовательности 1 символ
    Заканчивается на \n
'''

import re

regex = r'(?i)категория:[\w\s]+\\n'

print(re.split(regex, input()))