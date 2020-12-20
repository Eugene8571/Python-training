def grasshooper(N, s):
    
    A = [int(i) for i in s.split()]
    K = [0] + A + [0] * (N - len(A))
    
    for i in range(2, N + 1):
        print(K)
        K[i] = K[i-1] 
        for m in range(i):
            if K[m] == i - 1 - (i - m) and K[m] != 1:
                K[i] += K[m]

    return K[N]

print(grasshooper(10, '1 1 1 1 1 1 1 1 1 1'))
print(grasshooper(3, '2 2 1'))


