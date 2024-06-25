# Архивирование файлов: высокий уровень
from datetime import datetime
import shutil  # shell utilities
import os

root = os.getcwd()  # в какой директории запущен скрипт

list_dir = os.listdir(root)
result = []

for item in list_dir:
    if not os.path.isdir(item) and not item.endswith('.txt'):
        result.append(item)

print(result)
# temp = os.path.join(root, 'temp')
# dest = os.path.join(root, 'backup')
# # if not os.path.exists(temp):
# #     os.mkdir(temp)
# if not os.path.exists(dest):
#     os.mkdir(dest)
# shutil.copytree(root, temp,
#                 ignore=shutil.ignore_patterns('.venv',
#                                               '.idea',
#                                               '__pycache__'))
# shutil.make_archive('archive', 'zip', temp)
# shutil.move('archive.zip', dest)
# if os.path.exists(temp):
#     shutil.rmtree(temp)



