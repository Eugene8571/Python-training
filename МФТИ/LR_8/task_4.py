import turtle as t
#t.speed('fastest')



def koch_snowflake(m ,n):
    
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
        for x in range(3):
        
            koch_snowflake(m, n)
            t.left(60)
            koch_snowflake(m, n)
            t.right(120)
            koch_snowflake(m, n)
            t.left(60)
            koch_snowflake(m, n)
            t.right(120)





koch_snowflake(100, 1)






