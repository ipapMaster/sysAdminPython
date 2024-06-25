# Архивирование файлов: низкий уровень
from datetime import datetime
import shutil  # shell utilities
import os

now = datetime.now()
temp = datetime.fromtimestamp(os.path.getmtime('какой-то'))
mtime = (now - temp).days


# root = os.getcwd()  # в какой директории запущен скрипт
# if os.path.exists('reserve'):
#     os.mkdir('reserve')
#
# dest = os.path.join(root, 'reserve')
#
# os.system(f'robocopy {root} {dest} /Mov /maxage:2 /minage:1')


