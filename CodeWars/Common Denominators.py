def convertFracts(L):
    for i in range(len(L)):
        for n in range(1, L[i][1]):
            n = L[i][1] - n
            if L[i][0] % n == 0 and L[i][1] % n == 0:
                L[i][0] = int(L[i][0] / n)
                L[i][1] = int(L[i][1] / n)
    #print(L)

    D = 1
    A = []
    for pair in L:
        A.append(pair[1])
        D *= pair[1]

    D = int(D)
    R = D
    #print(D, A)
    for i in range(1, D//2+1):
        if R % i == 0:
            temp = 0
            for x in A:
                if (R / i) % x == 0 :
                    temp += 1
            if temp == len(A):
                R = int(R/i)
            #print(D, i)

    for i in range(len(L)):
        up = int(R / L[i][1])
        L[i][0] *= up
        L[i][1] *= up

    return L

print(convertFracts([[5, 10], [1, 3], [1, 4]]))
#print(convertFracts([[10, 4465465], [200, 100054621]]))
print(convertFracts([[15, 60], [1, 5]]))