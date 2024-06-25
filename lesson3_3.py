min_val = 1
max_val = 10

try:
    cur_val = int(input(f'Введите число от {min_val} до {max_val}: '))
    if not min_val <= cur_val <= max_val:
        raise ValueError('введенное число вне диапазона')
except ValueError as e:
    print('Будьте внимательны:', e)
else:
    print('Вы поступили верно')
