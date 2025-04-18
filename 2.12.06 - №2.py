'''Найдите трёхзначные номера, перед которыми идёт №, Номер, или Number.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из 3 арабских цифр
    Слева от последовательности стоит №, Номер, или Number

Sample Input 1:

№ 123 893 Номер 983 432 Number 948 481

Sample Output 1:

123 983 948

Sample Input 2:

3№4324Номер23423Number42342

Sample Output 2: '''

import re

regex = r'(?:(?<=№\s)|(?<=Number\s)|(?<=Номер\s))[0-9]{3}'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')