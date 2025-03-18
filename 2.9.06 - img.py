'''Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Начинается с <img
    Заканчивается на >
    Между началом и концом могут находиться последовательности из любых символов
 Sample Input 1:

<picture><source srcset="/static/frontend/new-year/2022/topbar_logo_small.svg" media="(max-width: 1024px)"><img class="navbar__logo" alt="Stepik" src="/static/frontend/new-year/2022/topbar_logo.svg"></picture>

Sample Output 1:

<img class="navbar__logo" alt="Stepik" src="/static/frontend/new-year/2022/topbar_logo.svg">'''

import re

regex = r'<img.*?>'

print(re.findall(regex, input()))