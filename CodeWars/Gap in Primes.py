def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True


def gap(g, m, n):

    M = 0
    for i in range(m, n):
        if is_prime(i):
            M = i
            break
    if M == 0:
        return None

    for i in range(M, n):
        if is_prime(i):
            if i - M == g:
                return [M, i]
            M = i

    return None

print(gap(10,300,400))