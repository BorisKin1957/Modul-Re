'''Напишите регулярное выражение, которое найдёт все адреса биткоин кошельков.
Что нужно найти:

Адрес представляет собой набор из префикса (1, или 3, или bc1) и основной части длиной от 27 до 34 символов.

В основной части используются:

    Весь латинский алфавит, кроме: O, I, l.
    Все арабские цифры, кроме 0.
 Sample Input 1:

FDSF WDFSWD9FSD DFSD9FSD9F 33aGVnZCm9hmJDqoRDJFTQm7B2VsESFa8a DSFSDFS4fdsds4Wsd 1LxYHh12ysPTrYqanvSwFU4SQQA5NsmNdG sgsfsdsdfsds 1vj8Q9w16Ats5wSGjG6vbmFofr9x9Kz2M 1NT6cJZaDY7TDwRZ2NiVDTG6wfS1gue3gV sdfsdfsdfsdfsdf sdf sdfsdfsdfs 1MAJzPUS2JwQ9T4Gya9knokpsEMn3hqG6L 1M6TdG68oGCTzU1HCSMNMppKbWbsMsgevf 1NatRaPvbVjqoWP8W3bXV9rmY1SjnAF7ER 1Pki745E2oZxsBzQWfyyYocKzKEiARufcq 1Mz3aXtGBgWQyVzuysVC6Dti4uy8ifMZDZ 1N8nBtfvFXfSzDYyVFsae5zeSgQpt4mEfz

Sample Output 1:

33aGVnZCm9hmJDqoRDJFTQm7B2VsESFa8a 1LxYHh12ysPTrYqanvSwFU4SQQA5NsmNdG 1vj8Q9w16Ats5wSGjG6vbmFofr9x9Kz2M 1NT6cJZaDY7TDwRZ2NiVDTG6wfS1gue3gV 1MAJzPUS2JwQ9T4Gya9knokpsEMn3hqG6L 1M6TdG68oGCTzU1HCSMNMppKbWbsMsgevf 1NatRaPvbVjqoWP8W3bXV9rmY1SjnAF7ER 1Pki745E2oZxsBzQWfyyYocKzKEiARufcq 1Mz3aXtGBgWQyVzuysVC6Dti4uy8ifMZDZ 1N8nBtfvFXfSzDYyVFsae5zeSgQpt4mEfz
'''


import re

regex = r'\b(1|3|bc1)[A-HJ-NP-Za-km-z1-9]{27,34}\b'

result = re.finditer(regex, input())

for match in result:
    print(match.group(), end=' ')