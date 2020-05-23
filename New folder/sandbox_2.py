A = [1,2,3,4,5,66,7]


def in_circle(s):
    A = [int(i) for i in s.split()]
    return 'YES' if A[0] ** 2 + A[1] ** 2 <= A[2] ** 2 else 'NO'

#print(in_circle(input()))


def deposite(s):
    A = [int(i) for i in s.split()]
    x = A[0]
    p = A[1]
    y = A[2]
    for i in range(1000):
        if x >= y:
            return i
        temp = x
        x = round((x + x / 100 * p), 2)
        if x == temp:
            x += 0.01

#print(deposite(input()))

'''
print(deposite('1 1 2'), 100)
print(deposite('10 50 50'))
print(deposite('100 10 200'))
'''

def sequence():
    count = 0
    temp = 0
    for m in range(int(input())):
        n = int(input())
        if n == 1:
            temp += 1
            if temp > count:
                count = temp
        else:
            temp = 0
    return count

#print(sequence())


def av_max_min_mod():
    A = []
    B = [0] * 4
    M = []
    while True:
        x = input()
        if x == '#':
            break
        A.append(int(x))
        M.append(int(x))
        if len(M) == 3:
            B[3] += sum(M) % M[2]
            M = []

    B[0] = round(sum(A) / len(A), 3)
    B[1] = max(A)
    B[2] = min(A)

    return ' '.join(str(k) for k in B)

#print(av_max_min_mod())


def task_E():
    A = []
    N = int(input())
    #N = 3
    B = []

    while True:
        INP = input()
        if INP == '#':
            break
        pair = [int(i) for i in INP.split()]
        A.append(pair)
    #A = [[0, 3], [0, 10], [2, 3], [2, 2], [2, 4]]
    for i in range(N):
        student = []
        for k in A:
            if k[0] == i:
                student.append(k[1])

        if len(student) > 0:
            student = sorted(student, reverse = True)
            B.append(student)
    B.sort(key = lambda x: -sum(x))

    return ' '.join(str(i) for j in B for i in j)

print(task_E())


def deposite(s):
    A = [int(i) for i in s.split()]
    x = A[0]
    p = A[1]
    y = A[2]
    for i in range(10000):
        if x >= y:
            return i
        temp = x
        x = round((x + x / 100 * p), 2)
        if x == temp:
            x += 0.01

print(deposite(input()))


def str_power(s, p):
    if p == 0:
        return 1
    if p > 0:
        return s * p
    if p < 0:
        if len(s) % p != 0:
            return 'NO SOLUTION'
        k = int(len(s) / abs(p))
        if s[:k] * abs(p) == s:
            return s[:k]
    return 'NO SOLUTION'

print(str_power(input(), int(input())))

print(str_power('abcd', -4))
print(str_power('abc', 3))
print(str_power('abcdabcd', -2))

for x in xrange(1,10):
    pass

for i in range():
        pass
for x in range():
        pass
for x in range():
        pass
