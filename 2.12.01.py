import re

regex = r'JavaScript|C\+\+|Python'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')