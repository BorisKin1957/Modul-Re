'''Нужно найти последовательности, подходящие по следующим условиям:

    В начале стоит #
    Потом идёт последовательность из 6 шестнадцатеричных цифр верхнего и нижнего регистров: 0123456789abcdefABCDEF
    Последовательность не может быть подпоследовательностью

Примеры валидных цветов:

#9370DB
#E6E6FA
#af84f5
#3138f7
'''

import re

# Напиши регулярное выражение в regex \(❤‿❤)/
regex = r'(?i)#\b[0-9A-F]{6}\b'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')
