def count_sort(A):
    C = [0] * (max(A) + 1)
    Z = 0
    for element in A:
        C[element] += 1
        if element == 0:
            Z += 1

    res = [0] * Z
    for i in range(len(C)):
        res += [i] * C[i]

    return res


A = [1,2,5,5,1,5,6,0,0,3,0]
print(count_sort(A)) 
{A:1}

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

count_sort(a)
A.append()