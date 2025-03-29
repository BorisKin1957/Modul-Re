'''Найдите все последовательности цифр, которые начинаются от 13 цифр включительно.'''


import re

regex = r'[0-9]{13,}'
match = re.fullmatch(regex, input())

print(bool(match))