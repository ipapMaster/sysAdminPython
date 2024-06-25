# Функции
# Модульность, конфигурационные файлы
# Отправка E-mail

def say_hello(name: str = 'Владимир', age: int = 35) -> str:
    """
    Функция, которая здоровается с указанием
    :param name: Тип str - имя
    :param age:
    :return: str
    """
    return f'Привет, {name}!\nВам {age} лет.'


# else после return, обычно, не пишется
def even_odd(num: int = 0) -> bool:
    return num % 2 == 0


def pow_2(x):
    return x ** 2  # local scope


def sq_eq(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    if d == 0:
        return -b / (2 * a)
    return (-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)


if __name__ == '__main__':
    pass
