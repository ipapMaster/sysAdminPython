# Списки
# iterable object - итерируемый объект
# mutable - изменяемый
# immutable - неизменяемый
# list() - преобразует аргумент в список

string = 'Python'
lst = []  # пустой список
lst2 = [3, 4]  # список c двумя значениями типа int
fruits = ['слива', 'арбуз', 'груша', 'яблоко']
symbols = list('python')

# if 'th' in string:
#     print('th - есть')
#
# if 'слива' in fruits:
#     print('Да')

for item in fruits:  # for each
    print(item)

for letter in string:  # for each
    print(letter, end='')
print()
print(*fruits, sep=';\n')
