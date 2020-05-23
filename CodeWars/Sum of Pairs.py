
def sum_pairs(A, s):
    if A==[]:            
        return None
    
    for i in range(len(A)):
        if s-A[i] in A:
            B=A
            B=A[i+1:]
            B=B[slice(B.index(s-A[i]))]
            #print(B)
            for j in range(len(B)):
                #print(s-B[j])
                if s-B[j] in B:
                    sum_pairs(B, s)
            return [A[i], A[A.index(s-A[i])]]







print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
print(sum_pairs([1, 2, 3, 4, 1, 0], 2))
print(sum_pairs([1, 4, 8, 7, 3, 15], 8))

'''
def sum_pairs(A, s):
    if A==[]:            
        return None
    if len(A) <= 100000:
        for i in range(len(A)):
            if s-A[i] in A:
                B=A
                B=A[i+1:]
                B=B[slice(B.index(s-A[i]))]
                #print(B)
                for j in range(len(B)):
                    #print(s-B[j])
                    if s-B[j] in B:
                        sum_pairs(B, s)
                return [A[i], A[A.index(s-A[i])]]
    if len(A) > 100000:
        for i in range(10000):
            if s - i in A:
                return [A[A.index(i)], A[A.index(s-i)]]
'''