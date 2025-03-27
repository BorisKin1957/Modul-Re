'''Нужно найти последовательности, подходящие по следующим условиям:

    Cостоит из символов латинского алфавита обоих регистров, цифр, а также _
    Перед последовательностью стоит v=

Sample Input 1:

https://youtu.be/watch?v=dQw4w9WgXcQ&list=PLi9drqWffJ9FWBo7ZVOiaVy0UQQEm4IbP

Sample Output 1:

dQw4w9WgXcQ'''

import re

# Напиши регулярное выражение в regex \(❤‿❤)/
regex = r'(?i)(?<=v=)[a-z-0-9]+'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')