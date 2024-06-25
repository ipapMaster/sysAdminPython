# Составные условия
# not, or, and

a = 8  # 3 ... 6
left = 3
right = 6

if left <= a <= right:
    print(f'Число {a} лежит в диапазоне от {left} до {right}.')
else:
    print(f'Число {a} не лежит в диапазоне от {left} до {right}.')
