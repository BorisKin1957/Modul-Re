'''Преобразуйте CamelCase «Верблюжий регистр» в snake_case «Змеиный регистр».'''


import re

def get_snake_case(string):
    regex = re.compile(r'(\d+)')
    new_string = regex.sub(r'_\1_', string).rstrip('_')
    result = result = re.sub(r'\w', lambda x: f'_{x.group().lower()}' if x.group().isupper() else x.group(), new_string)
    return result.lstrip('_')

print(get_snake_case(input()))