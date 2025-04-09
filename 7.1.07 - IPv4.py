'''Проверьте валидность IPv4 адресов (от 0.0.0.0 до 255.255.255.255) с помощью регулярных выражений.

Если валидный - выведите True, иначе - False.'''


import re

triad = r'(?:1[0-9][0-9]|[1-9][0-9]|2[0-5][0-5]|[1-9][0-9]|[0-9])'
regex = f'^{triad}.{triad}.{triad}.{triad}$'

print(bool(re.search(regex, input())))

