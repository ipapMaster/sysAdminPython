# Функция print
# scope
a = 1
b = 2
c = 3

print(a, b, c, sep='+', end='=6\n')  # PEP8
print(a, b, c, sep='+', end='=6\n\n\n')

print(f'{c} - {b} = {c - b}')

# r-строка - raw string
path = r'C:\Users\teacher\AppData\Local\Microsoft\WindowsApps\mspaint.exe'
