'''Нужно разделить строку по символвам ? и &, оставив эти символы в полученном списке.'''

import re

regex = re.compile(r'([?&])')

match = re.split(regex, input())

print(match)