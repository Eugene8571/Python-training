def thue_morse(N):
    up = [0]
    down = []
    n = 0
    while n < N:
        for i in range(len(up)):
            down.append(1 if up[i] == 0 else 0)
        up.extend(down)
        n = len(up)
        
    return ''.join(str(d) for d in up[:N])

#print(thue_morse(2))
#print(thue_morse(5))


def thue_morse_2(N):
    up = '0'
    down = ''
    n = 0
    while n < N:
        for i in range(len(up)):
            down += '1' if up[i] == '0' else '0'
        up += down
        down = ''
        n = len(up)
        
    return up[:N]

print(thue_morse_2(10))