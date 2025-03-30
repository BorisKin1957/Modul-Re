'''Работникам компании надоело заменять каждый день ФИО одного человека на другого. Напишите программу, которая будет заменять нужное ФИО на строку ФИО.
Что нужно сделать:

Нужно найти все ФИО в тексте и заменить их на строку ФИО.

ФИО могут быть двух видов:

    Фамилия Имя Отчество
    Фамилия И. О.

Также ФИО могут склоняться.  Генерируйте регулярное выражение "на ходу".'''


import re

fio = input().split()
f, i, o = fio[0], fio[1][:-1], fio[2]

f_ = f + r'\w{,2}?\s'
i_ = f"(({i}" + r'\w{1,2}?\s)' + f"|({i[0]}" + r'\.\s))'
o_ = f"(({o}" + r'\w{,2})' + f"|({o[0]}" + r'\.))'

old = f_ + i_ + o_
new = 'ФИО'

print(re.sub(old, new, input()))