# Методы строк и списков: практикум
string = 'Теливизор'

letter = 'е'
count = 0
pos = []

if string.startswith('Тел'):
    print('Да')

# print(''.join(string.split()))
# print(string.rstrip())
# temp = string.replace('и', 'е', 2)
# print(temp)

# if letter in string:
#     count = string.count(letter)
#     print(f'Буква {letter} в слове {string} встречается {count} раз(а).')
#     for index in range(len(string)):
#         if string[index] == letter:
#             pos.append(index + 1)
#     print(f'Буква {letter} в слове {string} встречается на позициях',
#           end=': ')
#     print(*pos, sep=', ')
# else:
#     print(f'Буква {letter} не найдена в слове {string}.')

