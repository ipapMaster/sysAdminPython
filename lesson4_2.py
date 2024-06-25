# Кортежи - tuple
# неизменяемый
# занимает меньше места в памяти
# обращение к нему быстрее
# распаковка коллекций (взаимное присвоение)

fruits = ['слива', 'арбуз', 'груша', 'яблоко']

print('Фрукты:')
for index, value in enumerate(fruits):
    print('\t', index + 1, '-', value)

# carts = [('7', 'heart'), ('10', 'spades')]
# cart_7 = carts[0]
# value, suit = cart_7
# print(value, suit)
