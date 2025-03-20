'''Напишите регулярное выражение, которое найдёт все символы /, слева и справа от которых ничего нет или стоят другие символы, не равные /.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Слева от неё не стоит /
    Справа от неё не стоит /
    Последовательность состоит из одного слеша: /

Sample Input 1:

k}e09lQS>:)*N\/OYp+N//;Oy6///hS/.T//O/n/(_oR///////eD?/nxeZOg2=j-Zw+-z}>5Sl[VX:}zaB:sL7fe</3>tgqk(8vP701}bcWnT~a/MR0

Sample Output 1:

/ / / / / / /

Sample Input 2:

/text/

Sample Output 2:

/ /
'''

import re

regex = r'(?<!/)/(?!/)'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')