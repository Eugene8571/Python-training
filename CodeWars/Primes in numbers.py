def primeFactors(n):
    S = ''
    multipl = 1
    temp = n
    for i in range(2, n + 1):
        if multipl == n:
            return S
        p = 0
        if temp % i == 0:
            while temp % i == 0:
                temp /= i
                p += 1
            multipl *= (i ** p)
            if p > 1:
                S += '(' + str(i) + '**' + str(p) + ')'
            else:
                S += '(' + str(i) + ')'
    return S


X = primeFactors(7775460)

if X == '(2**2)(3**3)(5)(7)(11**2)(17)':
    print('OK')

print(X)

'''1.4





'''