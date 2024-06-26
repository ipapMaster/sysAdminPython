import re
import requests

rhtml = requests.get('https://ipap.ru')

result = re.findall(r'\w+@\w+-\w+\.|\w+@\w+\w+\.\w+', rhtml.text)

print(set(result))