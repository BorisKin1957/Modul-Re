'''Напишите регулярное выражение, которое найдёт все повторяющиеся последовательности из двух цифр, которые идут друг за другом. Используйте нумерованные группы.
Что нужно найти:

Нужно найти последовательности из 2 одинаковых арабских цифр

Sample Input 1:

6996966969

Sample Output 1:

9696 6969

Sample Input 2:

534535345377777753453

Sample Output 2:

5353 7777'''

import re

regex = r'([0-9]{2})\1'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')