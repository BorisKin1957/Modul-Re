'''Найдите все последовательности, состоящие из символов x, длина которых простое число.'''


import re

def get_simple_digits(string):
    n = len(string.split())
    regex = ''
    for i in range(n):
        regex += '\\b' + 'x' '{' + str(simple_digits[i]) + '}' + '\\b' + '|'
    regex = regex.strip('|')
    match = re.finditer(f'{regex}', string)
    if match:
        for i in match:
            print(i.group(), end=' ')

simple_digits = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
simple_digits.sort()

get_simple_digits(input())