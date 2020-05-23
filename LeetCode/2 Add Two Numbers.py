def weird_script(A, B):
    a = ''
    b = ''
    
    for i in range(3)[::-1]:
        a += str(A[i])
        b += str(B[i])

    return int(a) + int(b)

