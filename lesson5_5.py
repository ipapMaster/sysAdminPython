# Словари: ключ(key): значение(value)
d = {'apple': 'яблоко',
     'plum': 'слива',
     'pineapple': 'ананас',
     'list': ['Фрукты', 'Овощи'],
     36.6: 'Нормальная температура',
     'ш': 'sh',
     }

length = len(d)
print(length)
keys = d.keys()  # keys_list
values = d.values()
for k, v in d.items():
    print(f'Ключ:{k} Значение: {v}')
