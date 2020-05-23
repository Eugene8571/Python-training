def sum_pairs(ints, s):
    B=[]
    A=ints
    for i in range(len(A)):
        for j in range(i):
            if A[i] + A[j] == s:
                if i<=j:
                    B=[A[i], A[j]]
                if i>j:
                    B=[A[j], A[i]]
                return B
    if B==[]:            
        return None 




print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
print(sum_pairs([1, 2, 3, 4, 1, 0], 2))