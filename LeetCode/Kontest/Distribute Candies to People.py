def distr_candies(candies, num_people):
    A = [0] * num_people
    n = candies
    m = 0
    for i in range(1, n + 1):
        j = i % num_people
        if m + i >= n:
            A[j] = A[j] + (n - m)
            B = A[1:]
            B.append(A[0])
            return B
        A[j] = A[j] + i
        m += i
    B = A[1:]
    B.append(A[0])
    return A


print(distr_candies(7,4))
print(distr_candies(10,3))
