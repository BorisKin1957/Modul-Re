'''Разделите текст на предложения. Делите по знакам препинания .?!.'''

import re

regex = r'[\.?!]'

print(re.split(regex, input()))