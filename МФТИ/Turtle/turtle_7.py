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
f=1
df=1


dl=m.sqrt((df/k)**2+k*f*df)

for i in range(1000):
    t.forward(dl)
    
    #t.left(df)
    f+=df

t.penup()
t.forward(1000)

    
    