# Исключения
# try - попытаться
# except - исключение
# finally - в любом случае
# else - исключения не было
# camel case
# snake case
from datetime import datetime

f_name = 'info.txt'
err_file = 'errors.txt'

try:
    with open(f_name, encoding='utf-8') as fo:
        text = fo.read(4)
        print(text)
except FileNotFoundError:
    now = datetime.now()
    timestamp = now.strftime('%d.%m.%Y %H:%M:%S')
    with open(err_file, 'at', encoding='utf-8') as fe:
        print(f'{timestamp}: Файл {f_name} отсутствует.',
              file=fe)
