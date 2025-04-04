'''Напишите программу, которая найдёт все am и pm в тексте и заменит их друг на друга.
Что нужно сделать:

Нужно заменить все am на pm, а pm на am.
Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Строка с am, заменённым на pm, и pm, заменённым на am.

Sample Input 1:

It's already 12:00am and I still don't want to sleep.'''



import re

regex = r'(am)|(pm)'

result = re.sub(regex, lambda match: 'am' if match.group(2) else 'pm', input())

print(result)