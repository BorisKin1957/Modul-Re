'''Найдите первое слово, которое содержится в определённом диапазоне.
Что нужно сделать:

Найти первое слово, состоящее из a-z в определённом диапазоне. Слово не может являться подпоследовательностью.
Тестовые данные:
Входные данные:

На вход программе подаётся 3 строки:

    Текст
    Начальная позиция для поиска
    Конечная позиция для поиска

Выходные данные:

Если в полученном диапазоне есть слово, то нужно его вывести.

Sample Input 1:

soda senior tuition library task tone few torch vacuum
2
29

Sample Output 1:

senior'''


import re

pattern = re.compile(r'\b(?P<word>[a-zA-Z]+)\b')
match = pattern.search(input(), int(input()), int(input()))

if match:
    print(match.group('word'))