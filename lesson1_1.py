# отступы - indents - 4 пробела
# объект: свойства, методы
# точечная нотация
# DRY - do not repeat yourself
# while - пока что...
import turtle

sides = 8  # число сторон
dist = 155
angle = 360 / sides  # вычисляем угол
counter = 0  # обнуляем счётчик

while counter < sides:
    turtle.forward(dist)
    turtle.right(angle)
    counter += 1  # то же, что и counter = counter + 1

turtle.mainloop()
