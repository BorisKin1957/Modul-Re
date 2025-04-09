'''Найдите все арабские числа и замените их на римские с помощью функции SPQR.

В римских числах не существует числа 0, его нужно игнорировать.'''

import re

def SPQR(m):
    num = int(m[0])
    result = ''
    lst = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    for arabic, roman in lst:
        result += num // arabic * roman
        num %= arabic
    return result

regex = re.compile(r'(?a)[^0 .]\d*')

print(re.sub(regex, SPQR, input()))