'''Нужно найти первый попавшийся ключ. Нужные ключи в чате всегда отправляют в виде:

Activation key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX

    X - любая цифра или латинская буква в верхнем регистре
    Перед нужным ключом должна стоять строка Activation key:

Тестовые данные:
Входные данные:

На вход программе подаётся 5 строк. Гарантируется, что в этих строках есть как минимум 1 ключ.
Выходные данные:

Выведите в консоль ключ, который был найден. Только ключ. Другие данные не нужны.

Sample Input 1:

Hi
Here is my Activation key: PKRHK-6622Q-T49PV-CC3PX-TRX2Y
Bye
Test
Lmao

Sample Output 1:

PKRHK-6622Q-T49PV-CC3PX-TRX2Y

'''

import re

regex = r'(?<=Activation key: )(?:[A-Z0-9]{5}-){4}[A-Z0-9]{5}'

for i in range(5):
    match = re.search(regex, input())
    if match:
        print(match.group())
        break
