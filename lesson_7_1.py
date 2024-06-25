# Функции высшего порядка
strs = ['Яблоко\n', 'Груша\n', 'Слива\n']

temp = map(lambda x: x.rstrip('\n'), strs)

print(list(temp))
