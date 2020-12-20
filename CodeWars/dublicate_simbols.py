def is_contains_dublicate_0(A):
    if A == []:
        return False
    for sim in A:
        if A.count(sim) > 1:
            return True
    return False


def is_contains_dublicate(A):
    return len(A) != len(set(A))




A = [1,2,3,1]
#print(is_contains_dublicate(A) == True)
A = [1,2,3,4]
#print(is_contains_dublicate(A) == False)
A = []
#print(is_contains_dublicate(A) == False)


def sum_digits(n):
    res = 0
    for digit in str(abs(n)):
        res += int(digit)
    return res


n = 123
#print(sum_digits(n) == 6)

n = -10
#print(sum_digits(n) == 1)


def sum_digits_LC(n):
    return sum([int(i) for i in str(abs(n))])


#print(sum_digits(n) == sum_digits_LC(n), sum_digits_LC(n))


def get_first_dublicate_0(A):
    for sim in A:
        if A.count(sim) > 1:
            return sim
    return None

def get_first_dublicate_1(A):
    pair = [0, 0]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] == A[j]:
                if pair[1] == 0 or pair[1] > j:
                    pair = [i, j]
    return A[pair[0]]

def get_first_dublicate(A):
    list_ = []
    for elem in A:
        if elem in list_:
            return elem
        list_.append(elem)
    return None

A = [1,2,3,4,2,1]
print(get_first_dublicate(A) == 2)