def median(A, B):
    LA = len(A)
    LB = len(B)
    C = A + B
    C.sort()
    LC = len(C)
    if LC % 2 == 0:
        
        return round((C[LC // 2 - 1] + C[LC // 2]) / 2, 1)
    else:
        return C[LC//2]


print(median([1,2],[3,4]))