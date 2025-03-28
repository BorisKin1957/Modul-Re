'''Найдите все слова, которые начинаются на n или N.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из букв латинского алфавита нижнего и верхнего регистров, -
    Начинается на n или N
    Не может быть подпоследовательностью
'''

import re

# Напиши регулярное выражение в regex \(❤‿❤)/
regex = r'(?i)(?<=\s)n[a-z-]*(?=\s)|^n[a-z-]*(?=\s)|(?<=\s)n[a-z-]*$'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')