'''Дан большой текст, который состоит из нескольких строк, он находится в переменной text.

Найдите в нём текст от start до end.

 Sample Input 1:

start
Каждое
Слово
На
Новой
Строке
end

Sample Output 1:

['\nКаждое\nСлово\nНа\nНовой\nСтроке\n']'''

import re, sys

text = ''.join(sys.stdin.readlines())
regex = r'(?s)(?<=start).*(?=end)'
result = re.findall(regex, text)

print(result)

