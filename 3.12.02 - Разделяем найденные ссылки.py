'''Напишите программу, которая будет находить ссылки и разделять их на части: протокол, адрес, параметры, якорь. Протокол и адрес у ссылок есть всегда.
Что нужно найти:

Нужно найти ссылки, подходящие по следующим условиям:

    Протокол https или http
    После протокола идёт ://
    Домен состоит из символов a-z, .
    Путь состоит из символов a-z, 0-9, -, _, /
    Параметры начинаются с ? и состоят из a-z, =, &, 0-9
    Якорь начинается с # и состоит из a-z
    Протокол и адрес у ссылок есть всегда, остальных частей может не быть
    Ссылка не может быть подпоследовательностью

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка текста.
Выходные данные:

Выведите в консоль ссылку, протокол, домен, параметры, якорь найденных совпадений в следующем виде:

Полная ссылка: https://example.com/test/42523/step/2?q=query&s=search#test
Протокол: https | Домен: example.com | Параметры: ?q=query&s=search | Якорь: #test

Если группа ничего не нашла, то вместо совпадения нужно вывести None.'''

import re

regex = r'https?://[a-zA-Z0-9\-\.]+(?:\.[a-zA-Z]{2,})?(?:/[^\s]*)?(?!\S)'
urls = re.findall(regex, input())

reg_pro = r'(?<!\S)(https?)(?=://)'
reg_dom = r'(?<=://)([a-z\.]+?)(?=\/)'
#reg_par = r'(\?[a-zA-Z0-9_=&]+?)(?=#)'
reg_par = r'(\?[a-z0-9_=&]+)'
reg_yak = r'(#[a-z]+)'

for url in urls:
    print(f'Полная ссылка: {url}')
    match = re.search(reg_pro, url)
    if match:
        pro = match.group()
    else:
        pro = None
    match = re.search(reg_dom, url)
    if match:
        dom = match.group()
    else:
        dom = None
    match = re.search(reg_par, url)
    if match:
        par = match.group()
    else:
        par = None
    match = re.search(reg_yak, url)
    if match:
        yak = match.group()
    else:
        yak = None
    print(f'Протокол: {pro} | Домен: {dom} | Параметры: {par} | Якорь: {yak}\n')
