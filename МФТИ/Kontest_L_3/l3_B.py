x0, y0, x1, y1 = int(input()), int(input()), int(input()), int(input())

if x0 == x1 or y0 == y1 or x0 - y0 == x1 - y1 or x0 + y0 == x1 + y1:
    print('YES')
else:
    print('NO')
