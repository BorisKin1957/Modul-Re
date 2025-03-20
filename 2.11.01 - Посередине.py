'''Напишите регулярное выражение, которое получит последовательность из любых символов от [^START] до {(END.)}.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Слева от неё стоит [^START]
    Справа от неё стоит {(END.)}
    Состоит из любых символов, кроме символа перехода на новую строку

Sample Input 1:

[^START]Text{(END.)}

Sample Output 1:

Text

Sample Input 2:

[^START]{(END.)}

Sample Output 2: '''

import re

regex = r'(?<=\[\^START\]).*(?=\{\(END\.\)\})'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')