# Измерить время работы функции

def measure(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения {end - start} секунд')

    return wrapper

@measure
def list_fill():
    a = [x for x in range(10000000)]


list_fill()
