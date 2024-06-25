# Операции с файлами и каталогами (высокий уровень)
# Ctrl + Alt + O - optimize import
import os
from datetime import datetime

from transliterate import translit

now = datetime.now()
timestamp = now.strftime('_%m_%Y')

root = os.getcwd()  # в какой директории запущен скрипт
company_dir = 'companies'  # директория для размещения каталогов

temp = os.path.join(root, company_dir)  # куда заглубляемся

if not os.path.exists(company_dir):
    os.mkdir(company_dir)

try:
    with open('companies.txt', encoding='utf-8') as fo:
        lines = fo.readlines()  # прочитали все строки из файла в список
        for line in lines:  # перебираем список в цикле
            s_line = line.rstrip('\n')  # удаляем ненужный \n
            t_line = translit(s_line, reversed=True)  # транслитерируем
            result = t_line + timestamp
            ttt = os.path.join(temp, result)
            if not os.path.exists(ttt):
                os.mkdir(ttt)
except FileNotFoundError:
    print(f'Файл companies.txt не найден!')
