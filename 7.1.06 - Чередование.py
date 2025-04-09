'''На вход программе подается строка текста с разными словами на английском языке. Найдите такие слова, в которых постоянно чередуются гласные и согласные. Так как y может быть как и гласной, так и согласной, то добавим её сразу во все строчки.

Согласные:

BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz

Гласные:

AEIOUYaeiouy'''

import re

a = r'AEIOUYaeiouy'
b = r'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'

regex_b_a_b = fr'\b([{b}]?(?:[{a}][{b}])+[{a}]?)\b'
regex_a_b_a = fr'\b([{a}]?(?:[{b}][{a}])+[{a}]?)\b'
regex = fr'{regex_a_b_a}|{regex_b_a_b}'

for match in re.finditer(regex, input()):
    print(match[0], end=' ')

