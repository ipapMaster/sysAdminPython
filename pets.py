# Класс для питомцев
class Cat:
    # static properties
    family = 'Семейство кошачьих'
    counter = 0

    def __init__(self, name='noname', age=0):
        self.__name = name
        self.__age = age
        Cat.counter += 1

    def say_meow(self):
        return f'{self.__name} сказал "Мяу"'

    def get_name(self):  # getter
        return self.__name

    def set_name(self, new_name):  # setter
        self.__name = new_name

    def set_age(self, new_age):  # setter
        if new_age < 0:
            new_age *= -1
        self.__age = new_age
        return 0

    def get_age(self):  # getter
        return self.__age

    @staticmethod
    def get_counter():
        return Cat.counter

    # str(object) -> __str__(object)
    def __str__(self):
        return f'Это экземпляр класса Cat с именем {self.__name}'

    def __repr__(self):
        return f'<Cat({self.__name}, {self.__age})>'

    # a + b -> a.__add__(b)

    def __add__(self, other):
        return Cat(self.__name + other.__name, self.__age + other.__age)

    """
    __eq__ - сравнение
    __gt__ - больше ли
    __sub__ - вычитание
    __mul__ - умножение
    __len__ - len()
    """

    def __del__(self):
        print(f'Вызван сборщик мусора для {self.__name}')

class Dog:
    # static properties
    family = 'Собаки'
    counter = 0

    def __init__(self, name='noname', age=0):
        self.__name = name
        self.__age = age
        Cat.counter += 1

    def say_bark(self):
        return f'{self.__name} гафкнул'

    def get_name(self):  # getter
        return self.__name

    def set_name(self, new_name):  # setter
        self.__name = new_name

    def set_age(self, new_age):  # setter
        if new_age < 0:
            new_age *= -1
        self.__age = new_age
        return 0

    def get_age(self):  # getter
        return self.__age

    @staticmethod
    def get_counter():
        return Cat.counter

    # str(object) -> __str__(object)
    def __str__(self):
        return f'Это экземпляр класса Dog с именем {self.__name}'

    def __repr__(self):
        return f'<Dog({self.__name}, {self.__age})>'

    # a + b -> a.__add__(b)

    def __add__(self, other):
        return Cat(self.__name + other.__name, self.__age + other.__age)

    """
    __eq__ - сравнение
    __gt__ - больше ли
    __sub__ - вычитание
    __mul__ - умножение
    __len__ - len()
    """

    def __del__(self):
        print(f'Вызван сборщик мусора для {self.__name}')
