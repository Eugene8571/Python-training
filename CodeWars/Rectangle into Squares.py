
def sqInRect(a, b):
    if a == b:
        return None
    if a < b:
        a, b = b, a
    if a % b == 0:
        C = [b] * int(a / b)
        return C

    a = a - b
    return [b] + sqInRect(a, b)


print(sqInRect(37, 141))
