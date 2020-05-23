def parts_sums(ls):

    temp = sum(ls)
    A = [temp]
    for n in range(len(ls)):
        temp -= ls[n]
        A.append(temp)
    return A

print(parts_sums([0, 1, 3, 6, 10]))
