import turtle
import math as m
turtle.shape('arrow')





for i in range(10):
    n=i+3
    a=50
    R0=a/(2*m.sin(m.radians(360/(2*n))))
    m.fabs(R0)
    print(R0)
    R1=a/(2*m.sin(m.radians(360/(2*n+1))))
    m.fabs(R1)
    print(R1)
    r1=a/(2*m.tan(m.radians(360/(2*n+1))))
    D=R1-R0
    print(D)
    
    
    
    
    
    angle=360/n
    st_angle=angle+(180-angle)/2
    
    
    
    
    turtle.left(st_angle)
    for i in range(n):
        turtle.forward(a)
        turtle.left(angle)
        
    turtle.right(st_angle)
    turtle.penup()
    turtle.forward(D/2)   
    turtle.pendown() 
    
    
    