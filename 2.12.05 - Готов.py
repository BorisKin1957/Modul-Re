'''Напишите регулярное выражение, которое найдёт следующие последовательности в тексте:

я готов
я готова
ты готов
ты готова
он готов
она готова
мы готовы
вы готовы
они готовы

Sample Input 1:

я готова я готов ты готова ты готов

Sample Output 1:

я готова я готов ты готова ты готов

Sample Input 2:

он готов она готова они готовы мы готовы вы готовы

Sample Output 2:

он готов она готова они готовы мы готовы вы готовы'''

import re

regex = r'(?i)(?:(?:я|он|ты) готов\b)|(?:(?:я|она|ты) готова\b)|(?:(?:вы|они|мы) готовы\b)'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')