# public - открытый для всех: var
# private - закрытый снаружи: __var
# protected - только для наследников: _var
class Cat:
    def __init__(self, name='noname', age=0):
        self.name = name
        self.age = age

    def say_meow(self):
        return f'{self.name} сказал мяу'

    def get_name(self):  # getter
        return self.name

    def set_name(self, new_name):  # setter
        self.name = new_name

    def set_age(self, new_age):  # setter
        if new_age < 0:
            new_age *= -1
        self.age = new_age
        return 0

    def get_age(self):  # getter
        return self.age

    def __del__(self):
        print(f'Вызван сборщик мусора для {self.name}')


cat = Cat('Мурзик', 1)  # вызов конструктора
cat.set_age(-8)
print('Возраст кота', cat.get_age())
cat2 = Cat('Барсик', 2)
cat3 = Cat()

print(cat.say_meow())
print(cat2.say_meow())
print(cat3.say_meow())
