'''Замените в строке последние 5 символов на первые 5.'''

import re

def get_new_end(match):
    new_end = match.group()[:-5]
    return new_end + match.group(2)

regex = re.compile('^((.{5}).*)$')

print(re.sub(regex, get_new_end, input()))