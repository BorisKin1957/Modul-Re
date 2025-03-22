'''Найдите все слова да, нет, наверное в тексте. Они могут начинаться с букв разных регистров.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Это последовательность да, нет, наверное
    Не является подпоследовательностью

Sample Input 1:

«Да нет наверное» - фраза непонятная многим иностранцам. Это означает как бы "нет", только с сомнением "а вдруг?!"

Sample Output 1:

Да нет наверное нет'''

import re
regex = (r'(?<![А-Яа-яёЁA-Za-z])[Дд]а(?![А-Яа-яёЁA-Za-z])|(?<![А-Яа-яёЁA-Za-z])'
         r'[Нн]ет(?![А-Яа-яёЁA-Za-z])|(?<![А-Яа-яёЁA-Za-z])[Нн]аверное(?![А-Яа-яёЁA-Za-z])')

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')


