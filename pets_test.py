# Полиморфизм
import pets

cat = pets.Cat('Tom', 1)
dog = pets.Dog('Rex', 5)

if isinstance(dog, (pets.Cat,)):
    print('Речь о коте')
else:
    print('Речь о собаке')

print(cat.get_name())
print(dog.get_name())
