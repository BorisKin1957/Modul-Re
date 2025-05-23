'''Скомпилируйте регулярное выражение, которое находит mac-адреса, и присвойте его переменной pattern. Мак-адрес - специальный идентификатор, который присваивается сетевому адаптеру.

Данные выводить никуда не нужно.
Что нужно сделать:

Скомпилировать регулярное выражение, которое находит все mac-адреса: nn:nn:nn:nn:nn:nn, где n это 16-ричное число от 0 до F, и записать его в переменную pattern.
Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Ничего выводить не нужно. Нужно сохранить скомпилированное выражение в переменную.

Sample Input 1:

Мак-адрес моего друга:F0:98:9D:1C:93:F6. Мой мак-адрес: 0F:70:DE:55:60:19.

Sample Output 1:

['F0:98:9D:1C:93:F6', '0F:70:DE:55:60:19']'''


import re

pattern = re.compile('((?:[0-9A-F]{2}:){5}[0-9A-F]{2})')