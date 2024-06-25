# Работа с файлами
# режимы (mode) r-read, w-write, a-append (t - text)
from datetime import datetime

current_time = datetime.time(datetime.now())  # сырое время
timestamp = current_time.strftime('%H:%M')

fo = open('info.txt', 'at', encoding='utf-8')
# обращаемся к файловому объекту (читаем свойства)
print(fo.name)
print(fo.mode)
print(fo.encoding)  # run-time
# запись в файл
# length = fo.write("Эта строка будет записана в файл.")
# print(f'В файл записано {length} байт')
# text = fo.read(3)
# fo.read(1)
# text += fo.read(6)  # конкатенировать
# garbage collector - сборщик мусора
print(f'{timestamp} Событие №3', file=fo)
fo.close()
