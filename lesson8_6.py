# Квантификаторы (жадный и минорный)
"""
{m} - ровно m раз
{m,} - m раз и более
{,n} - не более, чем n
? - {0,1}
* - {0,}
+ - {1,}
"""
import re

# Wildcard - *.txt

# pattern = r'<img.*>' # greedy quantifier ("жадный")
# pattern = r'<img.*?>'  # minor quantifier ("не жадный")
pattern = r'http://[\S]+'  # minor quantifier (без угловых скобок)
string = 'Информация находится в http://google.com'

# result = re.match(pattern, string)  # ищет лишь в начале строки
# result = re.search(pattern, string)  # ищет в любой части строки
# result = re.findall(pattern, string)  # все вхождения по образцу
result = re.findall(pattern, string)
# print('Да, цифры есть') if result else print('Цифр нет')
print(result)
