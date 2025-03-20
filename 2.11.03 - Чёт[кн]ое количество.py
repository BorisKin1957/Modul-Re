'''Напишите регулярное выражение, которое найдёт все последовательности x с чётной длиной.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из символов x
    Длина последовательности чётная
    Последовательность не может быть подпоследовательностью

Sample Input 1:

x xx xxx xxxx xxxxx xxxxxx xxxxxxx xxxxxxxx xxxxxxxxx xxxxxxxxxx xxxxxxxxxxx xxxxxxxxxxxx xxxxxxxxxxxxx

Sample Output 1:

xx xxxx xxxxxx xxxxxxxx xxxxxxxxxx xxxxxxxxxxxx'''

import re

regex = r'\b(?:xx)+\b'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')