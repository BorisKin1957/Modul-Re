'''Замените все цифры на X. Выведите полученную строку и количество совершённых замен.'''

import re

old = r'\d'
new = 'X'

print(re.subn(old, new, input()))