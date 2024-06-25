# Модуль высокоуровневых операций с файлами
import shutil  # shell utilities
import os


root = os.getcwd()  # в какой директории запущен скрипт
company_dir = 'companies'  # директория для размещения каталогов
directory_to_remove = os.path.join(root, company_dir)

question = input(f'Вы правда хотите удалить {directory_to_remove}?'
                 f'"Да" или "Нет": ')
if question == 'Да':
    shutil.rmtree(directory_to_remove)
