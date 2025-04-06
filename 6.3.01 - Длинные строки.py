'''Из всех строк в переменной text найти только те, которые полностью состоят из символов ^$'''


import re, sys

text = ''.join(sys.stdin.readlines())
regex = r'(?m)^[\^$]+$'
result = re.findall(regex, text)

print(result)

