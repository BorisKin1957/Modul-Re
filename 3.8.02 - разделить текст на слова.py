'''Нужно разделить текст на слова по следующим символам: .?! , '''


import re

regex = r'[\.?!,\s]'

print(re.split(regex, input()))