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

print(sieve(100))