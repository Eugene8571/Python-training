def my_atoi(s: str) -> int:
    if len(s) == 0:
        return 0

    import re

    n = re.match(r' *(\+|\-)?\d+', s)
    if n:
        n = n.group().strip()
    else:
        return 0

    n = int(n)

    if -2147483648 >= n:
        return -2147483648

    if n >= 2147483647:
        return 2147483647

    return n


print(my_atoi('--'))
print(my_atoi("  -123.gjhj -42 hjhj"))
