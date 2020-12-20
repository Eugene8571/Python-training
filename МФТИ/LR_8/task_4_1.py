import turtle as t
t.speed('fastest')



def koch_snowflake(m ,n):
    
    if n==0:
        t.forward(m)
        t.left(60)
        t.forward(m)
        t.right(120)
        t.forward(m)
        t.left(60)
        t.forward(m)


    elif n==1:
        m=m/(n*4/3)
        n-=1
        koch_snowflake(m, n)
        t.left(60)
        koch_snowflake(m, n)
        t.right(120)
        koch_snowflake(m, n)
        t.left(60)
        koch_snowflake(m, n)

    elif n:
        m=m/(n*4/3)
        n-=1
        koch_snowflake(m, n)
        t.left(60)
        koch_snowflake(m, n)
        t.right(120)
        koch_snowflake(m, n)
        t.left(60)
        koch_snowflake(m, n)



for x in range(3):
    koch_snowflake(100, 4)
    t.right(120)


