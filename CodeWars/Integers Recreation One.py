def list_squared(a, b):
    A = []
    for n in range(a, b + 1):
        sq_div_summ = 0
        for i in range(1, n + 1):
            if n % i == 0:
                sq_div_summ += i ** 2
        x = sq_div_summ ** 0.5
        if x == int(x):
            A.append([n, sq_div_summ])
    return A

print(list_squared(1, 5000)) # 10000 3,4c



def list_squared_2(a, b):

    pass

def sieve(N):
    A = [True] * N
    #A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(k * k, N, k):
                A[m] = False
    res = ''
    for k in range(N):
        if A[k]:
            res += ' ' + str(k)

    return res.strip()

print(sieve(200))