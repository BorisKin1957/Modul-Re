'''В переменной match записан объект Match. Выведите на экран:

    Его нулевую группу
    Начало вхождения нулевой группы
    Конец вхождения нулевой группы
    Атрибут pos
    Атрибут endpos
    Атрибут re
    Атрибут string

На входные данные и функцию re.match() не обращайте внимания.

Sample Input 1:

I
I love regex!

Sample Output 1:

I
0
1
0
13
re.compile('I')
I love regex!'''


import re

match = re.match(input(), input())
# Код писать сюда \(❤‿❤)/

print(match.group(), match.start(), match.end(0), match.pos, match.endpos, match.re, match.string, sep='\n')