def play(num, p):
    N = 0
    for d in str(num):
        N += int(d) ** p
        p += 1

    if N % num != 0:
        return -1
    return int(N / num)


print(play(46288, 3))