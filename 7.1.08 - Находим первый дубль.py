'''Напишите функцию find_repeated, принимающую строку, состояющую из слов, разделённых пробелом.
Функция должна вернуть первое слово, у которого существуют повторения в строке.
Если такого слова нет - функция возвращает None.

print(find_repeated("ap fl hk ap hk fl")) # ap
print(find_repeated("abc def apc def"))   # def'''

import re

def find_repeated(string):
    match = re.search(r'.*?\b(\w+)\b.*\b\1\b', string)
    if match:
        return match[1]
    return None

print(find_repeated(input()))