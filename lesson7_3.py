# Декораторы

def decorator(func):
    def wrapper():
        print('Это работает обёртка')
        print(f'Мы передали на вход {func}')
        print('Выполняем обёрнутую функцию')
        func()
        print('Покидаем обёртку')

    return wrapper


@decorator
def say_hello():
    print('Привет всем!')


say_hello()
