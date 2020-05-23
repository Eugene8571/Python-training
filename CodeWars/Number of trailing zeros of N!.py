def a_zeros(N):
    return N // 5 + a_zeros(N // 5) if N >= 5 else 0


def b_zeros(N):
    p = 1
    count = 0
    while 5 ** p <= N:
        count += N // (5 ** p)
        p += 1
    return count



print(a_zeros(0) == 0, a_zeros(6) == 1, a_zeros(30) == 7, \
    a_zeros(100) == 24, 'a_zeros')

# print(c_zeros(12345), 'b_zeros')

print(b_zeros(0) == 0, b_zeros(6) == 1, b_zeros(30) == 7, \
    b_zeros(100) == 24, 'b_zeros')

