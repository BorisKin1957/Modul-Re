

import re

regex = r'(?i)категория:[\w\s]+\\n'

print(re.split(regex, input()))