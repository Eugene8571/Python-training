import turtle as t

t.shape('turtle')

#forward(X)	Пройти вперёд X пикселей
#backward(X)	Пройти назад X пикселей
#left(X)	Повернуться налево на X градусов
#right(X)	Повернуться направо на X градусов
#penup()	Не оставлять след при движении
#pendown()	Оставлять след при движении
#shape(X)	Изменить значок черепахи (“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”)
#stamp()	Нарисовать копию черепахи в текущем месте
#color()	Установить цвет
#begin_fill()	Необходимо вызвать перед рисованием фигуры, которую надо закрасить
#end_fill()	Вызвать после окончания рисования фигуры
#width()	Установить толщину линии
#goto(x, y)	Переместить черепашку в точку (x, y)

a=10

for i in range(10):
    
    a+=10
    
    for i in range(4):
        t.forward(a)
        t.left(90)
    
    t.penup()
    t.left(180)
    t.forward(5)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.pendown()