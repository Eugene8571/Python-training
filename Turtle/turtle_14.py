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
b=11


x=a

angle=int(360/x*3)
for i in range(x):
    t.left(360-angle)
    t.forward(100)



t.penup()
t.goto(300, 0)
t.pendown()

x=b

angle=int(360/x*3)
for i in range(x):
    t.left(360-angle)
    t.forward(100)
    
t.forward(500)
    
    
    
    
    
    