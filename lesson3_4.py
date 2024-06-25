# Утверждение
try:
    text = input('Введите текст: ')
    assert len(text) > 3  # Утверждение
except AssertionError:
    print('Текст слишком короткий...')
