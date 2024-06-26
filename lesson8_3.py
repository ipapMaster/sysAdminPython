# Регулярные выражения (разделение по образцу - pattern)
import re

string = 'word1, word2; word3 word4'
pattern = r'[,;\s]+'

result = re.split(pattern, string)
# result = filter(lambda x: x != '', result)
print(list(result))
