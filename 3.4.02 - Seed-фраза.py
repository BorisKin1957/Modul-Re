'''Напишите программу, которая будет проверять, может ли текст содержать в себе seed фразу или нет.
Что нужно сделать:

 Нужно проверить, может ли текст содержать seed-фразу:

    Seed-фраза - это последовательность из 12, 18 или 24 случайных слов
    В данном случае нужно проверять, что текст начинается как минимум с 12 слов
    Слова состоят из букв латинского алфавита нижнего регистра
    Между словами могут стоять только пробелы

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Если строка походит по условиям, то нужно вывести: возможно, это seed-фраза.'''

import re

regex = r'(?:[a-z]+\s){11}[a-z]+'
match = re.match(regex, input())

print('возможно, это seed-фраза' if match else '')