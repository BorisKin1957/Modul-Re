'''Напишите программу, которая делит на 3 все числа, кратные 3.
Что нужно сделать:

Найти все числа в тексте, и проверить, кратно число 3 или нет:

    Если кратно, то заменить его на это же число, разделённое на 3
    Если нет - оставить его как есть
'''


import re

def is_divisible_by_3(match):
    if int(match[0]) % 3 == 0:
        return str(int(match[0]) // 3)
    return match[0]

regex = r'[0-9]+'

result = re.sub(regex, is_divisible_by_3, input())

print(result)
