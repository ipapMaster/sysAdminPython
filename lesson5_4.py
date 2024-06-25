# Случайный выбор
import random as r

lst = list(range(26))
print(lst)
r.shuffle(lst)
print(lst)
temp = r.choices(lst, k=5)
print(temp)