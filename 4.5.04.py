


import re

def is_divisible_by_3(match):
    if int(match[0]) % 3 == 0:
        return str(int(match[0]) // 3)
    return match[0]

regex = r'[0-9]+'

result = re.sub(regex, is_divisible_by_3, input())

print(result)
