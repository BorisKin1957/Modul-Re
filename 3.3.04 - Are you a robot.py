'''Даны данные в формате JSON. С помощью регулярных выражений нужно получить ключ t и его значение.
Что нужно сделать:

 Нужно найти ключ t и его значение:

    Значением является последовательностью из арабских цифр, символов . и +
    Перед значением стоит t=

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка с данными в формате JSON.
Выходные данные:

Выведите в консоль ключ t и его значение.

Sample Input 1:

{"errorCode":909,"errorMessage":"Are you a robot? Please enter the captcha below","errorDescription":null,"logStatus":null,"captcha":"\/captcha\/view?_CAPTCHA&amp;t=0.555555+11232131"}

Sample Output 1:

t=0.555555+11232131'''

import re

regex = r't\=0\.[0-9]+\+[0-9]+'

match = re.search(regex, input())

print(match.group() if match else '')
