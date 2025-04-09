'''В тексте могут использоваться дюймы и доллары. Дюймы нужно перевести в сантиметры, а доллары - в рубли.

Примечание 1 :

1 дюйм  = 2,54 см, курс доллара считайте равным 59,5 рублей за один доллар

Примечание 2:

Если полученное число целое - округлите его до 0 знаков после запятой, если нет - до двух знаков после запятой.
Автор
Комментарий с задачей

Sample Input 1:

GROHE Aria 25081000 - Смеситель для ванны (хром) - $558

Sample Output 1:

GROHE Aria 25081000 - Смеситель для ванны (хром) - 33201 руб

Sample Input 2:

SCBRHMI Серийный ЖК-дисплей HMI TFT с сенсорной панелью 10,4 дюйма - $95,25

Sample Output 2:

SCBRHMI Серийный ЖК-дисплей HMI TFT с сенсорной панелью 26,42 см - 5667,38 руб

Sample Input 3:

Кран шаровый 1" наружная резьба - нет в продаже

Sample Output 3:

Кран шаровый 2,54 см наружная резьба - нет в продаже

'''

import re

def get_rus_unit(match):
    if match.group(0)[0] == '$':
        total = str(round(float(match.group(0)[1:].replace(',', '.')) * 59.5, 2)).replace('.', ',')
        if total[-2:] == ',0':
            return total[:-2] + ' руб.'
        return total + ' руб'
    elif match.group(0)[-1] == '"':
        total = str(round(float(match.group(0)[:-1].replace(',', '.')) * 2.54, 2)).replace('.', ',')
    else:
        index = match.group(0).find(' ') + 1
        total = str(round(float(match.group(0)[:-index].replace(',', '.')) * 2.54, 2)).replace('.', ',')
    if total[-2:] == ',0':
        return total[:-2] + ' см.'
    return total + ' см.'

regex = r'\$[\d\.,]+|[\d\.,]+\"|[\d\.,]+ дюйм\w*'
result = re.sub(regex, get_rus_unit, input())

print(result)