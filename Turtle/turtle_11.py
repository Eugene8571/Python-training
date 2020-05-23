import turtle as t
t.shape('arrow')

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


a=5
b=0

t.left(90)
for i in range(a):
    
    
    b=i+1
    for i in range(180):
        t.forward(2*b)
        t.left(2)
    
    for i in range(180):
        t.forward(2*b)
        t.right(2)
    
    