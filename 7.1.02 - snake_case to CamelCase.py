'''реобразуйте snake_case «Змеиный регистр» в CamelCase «Верблюжий регистр».'''

import re

def get_CamelCase(string):
    regex = re.compile(r'((_[a-z])|^[a-z])')
    result = re.sub(regex, lambda x: x.group(0).upper(), string)
    return result.replace('_', '')

print(get_CamelCase(input()))