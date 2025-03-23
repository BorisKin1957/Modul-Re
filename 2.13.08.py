import re

regex = r'\b[Тт]ы\b'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')