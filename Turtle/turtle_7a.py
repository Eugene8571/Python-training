import turtle as t
t.shape('arrow')
import math as m

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
pi=m.pi
print(pi)
k=a/(2*m.pi)
f=0
dl=1


for i in range(1000):
    df=dl*100/(k*m.sqrt(1+f**2))
    t.left(df)
    f+=df
    t.forward(dl)

t.penup()
t.forward(1000)

    
    