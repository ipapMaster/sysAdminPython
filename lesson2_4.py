# Подключение модулей и способы
# 1. Просто подключаем
import turtle

# 2. Используя псевдоним
import turtle as t

# 3. Подключаем библиотеку полностью
from turtle import *

# 4. Подключаем адресно
from datetime import datetime

current_time = datetime.time(datetime.now())  # сырое время
# %H - часы в 24-м формате
# %M - минуты
# %S - секунды
print(current_time.strftime('%H часов'))
