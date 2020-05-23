def fib(n):
    if n < 0:
        n = -n 
    if n in (0, 1):
        return n
    '''
    A = [0, 1]
    for k in range(2, n + 1):
        temp = A[0] + A[1]
        A = A[1:]
        A.append(temp)
    '''
    t_0 = 0
    t_1 = 1
    for x in range(1,n):
        t_3 = t_0 + t_1
        t_0, t_1 = t_1, t_3

        
    return t_1 #, A.pop()


print(fib(1000))
