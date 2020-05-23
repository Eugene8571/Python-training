import math as m

N = int(input())

s = ''
for i in range(int(m.sqrt(N))):
    a = (i + 1) ** 2
    s += str(a) + ' '
    # s+=

print(s)
