


def solve(s):
    if len(s) == 0:
        return 0
    if len(s) % 2 == 1:
        return -1
    
    n = 0
    cnt = 0
    for v in s:
        if v == '(':
            cnt += 1
        if v == ')':
            cnt -= 1
        if cnt < 0:
            n += 1
            cnt = 1
    

    return n + cnt/2
    









from my_test import test
test(solve, ")()(",2)
test(solve, "((()",1)
test(solve, "(((",-1)
test(solve, "())(((",3)
test(solve, "())()))))()()(",4)

