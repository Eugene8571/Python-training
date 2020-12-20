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


x=0
y=0

t.width(3)
t.color('black', 'yellow')
t.begin_fill()
for i in range(120):
    t.left(3)
    t.forward(3)
t.end_fill()








t.penup()    
t.goto(-25, 60)
t.pendown()
t.color('black', 'black')
t.begin_fill()
for i in range(90):
    t.left(4)
    t.forward(1)
t.end_fill()

t.penup()    
t.goto(25, 60)
t.pendown()
t.begin_fill()
for i in range(90):
    t.left(4)
    t.forward(1)
t.penup() 
t.end_fill()
   
t.goto(-20, 35)
t.pendown()
t.width(10)
t.forward(40)
t.penup()    
t.forward(500)
