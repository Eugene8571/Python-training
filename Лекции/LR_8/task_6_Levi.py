import turtle as t
t.speed('fastest')

t.penup()
t.goto(-500, -200)
t.pendown()

def levi(l, n):
    if n==0:
        t.forward(l)
    
    elif n==1:
        
        t.left(45)
        t.forward(l)
        t.right(90)
        t.forward(l)
        t.left(45)

    elif n>1:
        n-=1
        

        t.left(45)
        levi(l, n)
        t.right(90)
        levi(l, n)
        t.left(45)







levi(5, 20)




"""

def mink(l, n):
    if n==0:
        t.left(90)
        t.forward(l)
        t.right(90)
        t.forward(l)
        t.right(90)
        t.forward(l)
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.right(90)
        t.forward(l)

    elif n==1:
        l/=8
        n-=1
        mink(l, n)
        t.left(90)
        mink(l, n)
        t.right(90)
        mink(l, n)
        t.right(90)
        mink(l, n)
        mink(l, n)
        t.left(90)
        mink(l, n)
        t.left(90)
        mink(l, n)
        t.right(90)
        mink(l, n)

    elif n>1:
        l/=n
        n-=1
        mink(l, n)
        t.left(90)
        mink(l, n)
        t.right(90)
        mink(l, n)
        t.right(90)
        mink(l, n)
        mink(l, n)
        t.left(90)
        mink(l, n)
        t.left(90)
        mink(l, n)
        t.right(90)
        mink(l, n)

mink(100, 3)


"""
"""

def koch_curve(m ,n):
    if n==0:
        t.forward(m)
        t.left(60)
        t.forward(m)
        t.right(120)
        t.forward(m)
        t.left(60)
        t.forward(m)

    elif n>=1:
        m=m/(3*n)
        n-=1
        koch_curve(m, n)
        t.left(60)
        koch_curve(m, n)
        t.right(120)
        koch_curve(m, n)
        t.left(60)
        koch_curve(m, n)









        

            
koch_curve(1000, 3)

"""


