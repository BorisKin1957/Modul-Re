'''Напишите регулярное выражение, которое найдёт все переменные, записанные в стиле lowerCamelCase.
Что нужно найти:

Нужно найти переменные, записаные в стиле lowerCamelCase, который включает в себя следующее:

    Первое слово начинается всегда с буквы нижнего регистра
    Последующие слова начинаются с букв в верхнем регистре
    Больше верхний регистр нигде не используется
    Используются буквы латинского алфавита
    Цифры в переменных из тестовых данных находятся только в конце

Примеры использования:

    variable
    quiteLongVariable
    twoWords

Sample Input 1:

get_id sendMessage echo_all canvas wrapper RegularExpression vUpperCase nice_Flick_SHOT that_was_bad getLink

Sample Output 1:

sendMessage canvas wrapper vUpperCase getLink'''

import re

# Напиши регулярное выражение в regex \(❤‿❤)/
regex = r'\b[a-z]+(?:[A-Z]?[a-z]+)*\d*\b'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')