# Регулярные выражения (поиск по образцу - pattern)
import re

# Wildcard - *.txt

pattern = r'\((.+?)\)'
string = 'поиск по образцу (pattern)'

# result = re.match(pattern, string)  # ищет лишь в начале строки
# result = re.search(pattern, string)  # ищет в любой части строки
# result = re.findall(pattern, string)  # все вхождения по образцу
result = re.findall(pattern, string)
# print('Да, цифры есть') if result else print('Цифр нет')
print(result)
