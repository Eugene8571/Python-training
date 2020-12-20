def fac(n):
    f = 1
    x = 2
    while x <= n:
        f *= x
        x += 1

    return f





def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)
fac(5)


print(sys.getrecursionlimit(-5))

