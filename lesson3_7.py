# Методы строк

string = 'яЗык pyThon'  # Python - язык

print(string.lower())  # все буквы маленькие
print(string.upper())  # все буквы большие
print(string.capitalize())  # первая буква предложения заглавная
print(string.title())  # все слова с заглавной

lst = string.lower().split()  # по любому кол-ву пробелов
revers = lst[::-1]  # разворот срезом

result = ' - '.join(revers)

print(result.capitalize())
