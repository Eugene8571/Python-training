import turtle

turtle.shape('turtle')



x=0
for i in range(10):
    x+=10
    
    for i in range(4):
        
        turtle.forward(x)
        turtle.left(90)
        
    turtle.penup()
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(180)
    turtle.pendown()
    
    
    