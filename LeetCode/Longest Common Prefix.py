def longestCommonPrefix(A):
    if len(A) == 0 or '' in A:
        return ''
    res = ''
    for i in range(len(A[0])+1):
        temp = A[0][:i]
        for s in A:
            if s[:i] != temp:
                return res
        res = temp
    return res

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["", "dog","doggy","dogs"]))
print(longestCommonPrefix(['']))
