def convertFracts(L):
    for i in range(len(L)):
        for n in range(1, L[i][1]):
            n = L[i][1] - n
            if L[i][0] % n == 0 and L[i][1] % n == 0:
                L[i][0] = int(L[i][0] / n)
                L[i][1] = int(L[i][1] / n)

    A = []
    for pair in L:
        A.append(pair[1])

    C = [[] * i for i in range(len(A))]
    #print(A)
    for i in range(len(A)):
        for multiplier in range(2, A[i] + 1):
            if A[i] % multiplier == 0:
                while A[i] % multiplier == 0:
                    C[i].append(multiplier)
                    A[i] = int(A[i] / multiplier)

    #print(C)
    Denom = []
    for i in range(len(C)):
        for n in C[i]:
            while C[i].count(n) > Denom.count(n):
                Denom.append(n)

    R = 1
    for x in Denom:
        R *= x

    for i in range(len(L)):
        up = int(R / L[i][1])
        L[i][0] *= up
        L[i][1] *= up

    return L





print(convertFracts([[5, 10], [1, 3], [1, 8]]))