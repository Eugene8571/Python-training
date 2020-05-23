def unique_in_order(S):
    if len(S) == 0:
        return []
    A = [S[0]]
    for char in S:
        if char != A[-1]:
            A.append(char)
    return A


print('OK' if unique_in_order('') == [] else 'FAIL')
print('OK' if unique_in_order('AAAABBBCCDAABBB') == ['A','B','C','D','A','B'] else 'FAIL')






A = [1,2,3,4]
print(A[len(A)-1])
print(A[-1], A)


'''
def unique_in_order(S):
    if len(S) == 0:
        return []
    A = [S[0]]
    for char in S:
        if char != A[-1]:
            A.append(char)
    return A
'''