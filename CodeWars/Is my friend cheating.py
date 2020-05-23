def solution(n):
    # a * b = n
    A = []
    for i in range(1, n):
        if n % i == 0 and i != int(n / i):
            print(n%i, i, n/i)
            a = i
            b = int(n / i)
            print(a,b)
            if a < b:
                a, b = b, a
            sub_summ = 0
            for k in range(a + 1, b):
                sub_summ += k
                print(sub_summ, a*b)
            if sub_summ == a * b:
                A.append([a, b])
                A.append([b, a])


    return A

#print(solution(100))
print(solution(26)) #[(15, 21), (21, 15)]

