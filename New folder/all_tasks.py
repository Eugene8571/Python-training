def comp():
    a = str(input())
    a = a.strip()
    A = [int(i) for i in a.split(' ')]
    if A[0] > A[1]:
        return '1'
    if A[1] > A[0]:
        return '2'
    return '0'


print(comp())


def high_year():
    Y = int(input())
    if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
        return 'YES'
    return 'NO'


print(high_year())


def sq_sequence():
    N = int(input())
    B = 0
    x = 1
    A = []
    while B < N:
        B = x**2
        x += 1
        A.append(B)

    if A[len(A) - 1] > N:
        A = A[:-1]

    return '  '.join(str(i) for i in A)


print(sq_sequence())


def power_of_two():
    n = int(input())
    x = n
    while x > 1:

        if x == 2:
            return 'YES'
        if x < 2:
            return 'NO'
        x /= 2


print(power_of_two())


def gcd(a, b):

    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    if a < b:
        return gcd(a, b - a)


print(gcd(int(input()), int(input())))


def simple_num(a):

    for i in range(2, a):
        if a // i == a / i:
            return 0
    return 1


print(simple_num(int(input())))


def max_even():
    n = -1
    M = 0
    while n != 0:
        n = int(input())
    if n % 2 == 0 and n > M:
        M = n
    return M


print(max_even())


def max_repeat():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    loc_max = 0
    n = 0
    for i in range(N):
        if A.count(A[i]) > loc_max:
            loc_max = A.count(A[i])
            n = A[i]
    return n


print(max_repeat())


def grasshooper():
    N = int(input())
    A = [int(i) for i in input().split()]
    K = [0] + A + [0] * (N - len(A))
    for i in range(2, N + 1):
        K[i] = K[i-1] 
        for m in range(i):
            if K[m] == i - (i - m) - 1 and K[m] != 1:
                K[i] += K[m]

    return K[N]

print(grasshooper())
